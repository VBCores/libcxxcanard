#pragma once

#if defined(STM32G0)
#include "stm32g0xx_hal.h"
#elif defined(STM32G4)
#include "stm32g4xx_hal.h"
#endif
#if defined(HAL_FDCAN_MODULE_ENABLED)

#include <functional>

#include <cyphal/node/node_info_handler.h>
#include <cyphal/node/registers_handler.hpp>
#include <cyphal/providers/G4CAN.h>
#include <cyphal/allocators/o1/o1_allocator.h>

#include <uavcan/diagnostic/Record_1_1.h>
#include <uavcan/node/Heartbeat_1_0.h>
#include <uavcan/node/Health_1_0.h>
#include <uavcan/node/Mode_1_0.h>

TYPE_ALIAS(DiagnosticRecord, uavcan_diagnostic_Record_1_1)
TYPE_ALIAS(HBeat, uavcan_node_Heartbeat_1_0)

// NOTE: MUST be implemented by user
millis millis_32();
micros micros_64();

template<size_t QUEUE_SIZE, millis DELAY_ON_ERROR, size_t REGISTERS_COUNT>
class EmbeddedCyphal {
protected:
    bool _is_cyphal_on = false;
    uint8_t _health_status = uavcan_node_Health_1_0_NOMINAL;
    uint8_t _mode = uavcan_node_Mode_1_0_INITIALIZATION;
    millis _delay_cyphal_until_millis = 0;

    FDCAN_HandleTypeDef* hfdcan;
    UtilityConfig utilities;
    std::shared_ptr<CyphalInterface> cyphal_interface;
    std::byte cyphal_bss_buffer[
        sizeof(CyphalInterface) + sizeof(G4CAN) + sizeof(O1Allocator)
    ] __attribute__((aligned(4)));
    static const size_t CYPHAL_BUFFER_SIZE = QUEUE_SIZE * sizeof(CanardTxQueueItem);
    static inline std::byte cyphal_queue_buffer[CYPHAL_BUFFER_SIZE] __attribute__((aligned(O1HEAP_ALIGNMENT)));

    NodeInfoReader node_info_reader;
    RegistersHandler<REGISTERS_COUNT> registers_handler;

    void heartbeat() {
        static CanardTransferID hbeat_transfer_id = 0;
        HBeat::Type heartbeat_msg = {
            .uptime = (uint32_t)std::floor(millis_32() / 1000.0f),
            .health = {_health_status},
            .mode = {_mode},
            .vendor_specific_status_code = static_cast<uint8_t>(cyphal_interface->queue_size())
        };

        if (_is_cyphal_on) {
            cyphal_interface->send_msg<HBeat>(
                &heartbeat_msg,
                uavcan_node_Heartbeat_1_0_FIXED_PORT_ID_,
                &hbeat_transfer_id,
                MICROS_S * 2
            );
        }
    }

    void cyphal_error_handler() {
        _is_cyphal_on = false;
        cyphal_interface->clear_queue();
        // delay for half a second
        _delay_cyphal_until_millis = millis_32() + DELAY_ON_ERROR;
    }

    void restart_cyphal() {
        cyphal_interface->clear_queue();

        static CanardTransferID record_transfer_id = 0;
        DiagnosticRecord::Type record;
        record.severity.value = uavcan_diagnostic_Severity_1_0_ERROR;
        sprintf(reinterpret_cast<char*>(record.text.elements), "cyphal_error_handler was called internally");
        record.text.count = strlen((char*)record.text.elements);

        cyphal_interface->send_msg<DiagnosticRecord>(
                &record,
                uavcan_diagnostic_Record_1_1_FIXED_PORT_ID_,
                &record_transfer_id
        );

        _delay_cyphal_until_millis = 0;
        _is_cyphal_on = true;
    }

public:
    explicit EmbeddedCyphal(
        FDCAN_HandleTypeDef* hfdcan,
        CanardNodeID node_id,
        std::string&& name,
        uavcan_node_Version_1_0&& protocol_version,
        uavcan_node_Version_1_0&& hardware_version,
        uavcan_node_Version_1_0&& software_version,
        uint64_t software_vcs_revision_id,
        std::array<RegisterDefinition, REGISTERS_COUNT>&& registers_list
    ):
        hfdcan(hfdcan),
        utilities(micros_64, std::bind(&EmbeddedCyphal::cyphal_error_handler, this)),
        cyphal_interface(CyphalInterface::create_bss<G4CAN, O1Allocator>(
            cyphal_bss_buffer,
            node_id,
            hfdcan,
            QUEUE_SIZE,
            utilities,
            cyphal_queue_buffer
        )),
        node_info_reader(
            cyphal_interface,
            std::forward<std::string>(name),
            std::forward<uavcan_node_Version_1_0>(protocol_version),
            std::forward<uavcan_node_Version_1_0>(hardware_version),
            std::forward<uavcan_node_Version_1_0>(software_version),
            std::forward<uint64_t>(software_vcs_revision_id)
        ),
        registers_handler(
            std::forward<std::array<RegisterDefinition, REGISTERS_COUNT>>(registers_list),
            cyphal_interface
        )
        {
        setup_subscriptions();

        HAL_IMPORTANT(HAL_FDCAN_ConfigTxDelayCompensation(
            hfdcan,
            hfdcan->Init.DataTimeSeg1 * hfdcan->Init.DataPrescaler,
            0
        ))
        HAL_IMPORTANT(HAL_FDCAN_EnableTxDelayCompensation(hfdcan))
        HAL_IMPORTANT(HAL_FDCAN_Start(hfdcan))

        _is_cyphal_on = true;
    }

    void set_mode(uint8_t mode) {
        _mode = mode;
    }

    void set_status(uint8_t status) {
        _health_status = status;
    }

    __attribute__((hot, flatten)) void cyphal_loop() {
        if (_is_cyphal_on) {
            cyphal_interface->loop();
        }
        if (_is_cyphal_on) {
            millis current_t = millis_32();
            in_loop_reporting(current_t);

            static millis heartbeat_time = 0;
            EACH_N(current_t, heartbeat_time, 1000, {
                heartbeat();
            })
        }

        if (_delay_cyphal_until_millis != 0 &&
            _delay_cyphal_until_millis <= millis_32()) {
            restart_cyphal();
        }
    }

    virtual void setup_subscriptions() {
        HAL_FDCAN_ConfigGlobalFilter(
            hfdcan,
            FDCAN_REJECT,
            FDCAN_REJECT,
            FDCAN_REJECT_REMOTE,
            FDCAN_REJECT_REMOTE
        );
    }

    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunused-parameter"
    // NOTE: <current_t> parameter required by the interface, but not used in this implementation
    virtual void in_loop_reporting(millis current_t) {
    #pragma GCC diagnostic pop
    }
};

#endif
