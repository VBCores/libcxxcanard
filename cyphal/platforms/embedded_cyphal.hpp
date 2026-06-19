#pragma once

#if defined(STM32G0)
#include "stm32g0xx_hal.h"
#elif defined(STM32G4)
#include "stm32g4xx_hal.h"
#endif
#if defined(HAL_FDCAN_MODULE_ENABLED)

#include <functional>
#include <memory>

#include <cyphal/node/node_info_handler.h>
#include <cyphal/node/registers_handler.hpp>
#include <cyphal/providers/G4CAN.h>
#include <cyphal/allocators/o1/o1_allocator.h>

#include <uavcan/diagnostic/Record_1_1.hpp>
#include <uavcan/node/Heartbeat_1_0.hpp>
#include <uavcan/node/Health_1_0.h>
#include <uavcan/node/Mode_1_0.h>

// NOTE: MUST be implemented by user
#ifndef ARDUINO
#define millis_t millis
#define micros_t micros
millis_t millis_32();
micros_t micros_64();
#else
#include <Arduino.h>
#include "utils.h"
#define millis_t uint32_t
#define micros_t uint64_t
#define millis_32 millis
#define micros_64 micros
#endif

template<size_t QUEUE_SIZE, millis_t DELAY_ON_ERROR, size_t REGISTERS_COUNT>
class EmbeddedCyphal: public CyphalInterface {
protected:
    FDCAN_HandleTypeDef* hfdcan;
    std::byte cyphal_bss_buffer[sizeof(G4CAN) + sizeof(O1Allocator)] __attribute__((aligned(4)));
    bool _is_cyphal_on = false;
    uint8_t _health_status = uavcan_node_Health_1_0_NOMINAL;
    uint8_t _mode = uavcan_node_Mode_1_0_INITIALIZATION;
    millis_t _delay_cyphal_until_millis = 0;

    std::string node_name;
    uavcan_node_Version_1_0 protocol_version;
    uavcan_node_Version_1_0 hardware_version;
    uavcan_node_Version_1_0 software_version;
    uint64_t software_vcs_revision_id;
    std::array<RegisterDefinition, REGISTERS_COUNT> registers_list;
    std::unique_ptr<NodeInfoReader> node_info_reader;
    std::unique_ptr<RegistersHandler<REGISTERS_COUNT>> registers_handler;
    // Must match the arena size requested by G4CAN::create_bss().
    static const size_t CYPHAL_BUFFER_SIZE = static_cast<size_t>(
        QUEUE_SIZE * sizeof(CanardTxQueueItem) * QUEUE_SIZE_MULT
    );
    static inline std::byte cyphal_queue_buffer[CYPHAL_BUFFER_SIZE] __attribute__((aligned(O1HEAP_ALIGNMENT)));

    void heartbeat() {
        static CanardTransferID hbeat_transfer_id = 0;
        uavcan_node_Heartbeat_1_0 heartbeat_msg = {
            .uptime = (uint32_t)std::floor(millis_32() / 1000.0f),
            .health = {_health_status},
            .mode = {_mode},
            .vendor_specific_status_code = static_cast<uint8_t>(queue_size())
        };

        if (_is_cyphal_on) {
            send_msg(
                &heartbeat_msg,
                uavcan_node_Heartbeat_1_0_FIXED_PORT_ID_,
                &hbeat_transfer_id,
                MICROS_S * 2
            );
        }
    }

    void cyphal_error_handler() {
        _is_cyphal_on = false;
        clear_queue();
        // delay for half a second
        _delay_cyphal_until_millis = millis_32() + DELAY_ON_ERROR;
    }

    void restart_cyphal() {
        clear_queue();

        static CanardTransferID record_transfer_id = 0;
        uavcan_diagnostic_Record_1_1 record;
        record.severity.value = uavcan_diagnostic_Severity_1_0_ERROR;
        sprintf(reinterpret_cast<char*>(record.text.elements), "cyphal_error_handler was called internally");
        record.text.count = strlen((char*)record.text.elements);

        send_msg(
                &record,
                uavcan_diagnostic_Record_1_1_FIXED_PORT_ID_,
                &record_transfer_id
        );

        _delay_cyphal_until_millis = 0;
        _is_cyphal_on = true;
    }

    void start_cyphal() {
        HAL_IMPORTANT(HAL_FDCAN_ConfigTxDelayCompensation(
            this->hfdcan,
            this->hfdcan->Init.DataTimeSeg1 * this->hfdcan->Init.DataPrescaler,
            0
        ))
        HAL_IMPORTANT(HAL_FDCAN_EnableTxDelayCompensation(this->hfdcan))
        HAL_IMPORTANT(HAL_FDCAN_Start(this->hfdcan))

        _is_cyphal_on = true;
    }

    void setup_builtin_subscriptions() {
        InterfacePtr interface = shared_from_this();
        node_info_reader = std::unique_ptr<NodeInfoReader>(new NodeInfoReader(
            interface,
            std::move(node_name),
            std::move(protocol_version),
            std::move(hardware_version),
            std::move(software_version),
            software_vcs_revision_id
        ));
        registers_handler = std::unique_ptr<RegistersHandler<REGISTERS_COUNT>>(
            new RegistersHandler<REGISTERS_COUNT>(std::move(registers_list), interface)
        );
    }

    void finish_cyphal_setup() {
        setup_builtin_subscriptions();
        setup_subscriptions();
        start_cyphal();
    }

public:
    explicit EmbeddedCyphal(
        FDCAN_HandleTypeDef* hfdcan,
        CanardNodeID node_id,
        std::string&& name,
        std::array<RegisterDefinition, REGISTERS_COUNT>&& registers_list
    ):
        EmbeddedCyphal(
            hfdcan,
            node_id,
            std::move(name),
            uavcan_node_Version_1_0{1, 0},
            uavcan_node_Version_1_0{1, 0},
            uavcan_node_Version_1_0{1, 0},
            0,
            std::move(registers_list)
        )
    {}

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
        CyphalInterface(
            node_id,
            UtilityConfig(micros_64, std::bind(&EmbeddedCyphal::cyphal_error_handler, this)),
            nullptr
        ),
        hfdcan(hfdcan),
        node_name(std::move(name)),
        protocol_version(std::move(protocol_version)),
        hardware_version(std::move(hardware_version)),
        software_version(std::move(software_version)),
        software_vcs_revision_id(software_vcs_revision_id),
        registers_list(std::move(registers_list)) {
        std::byte* buffer = cyphal_bss_buffer;
        auto provider = G4CAN::create_bss<O1Allocator>(
            &buffer,
            hfdcan,
            node_id,
            QUEUE_SIZE,
            get_utilities(),
            cyphal_queue_buffer
        );
        attach_provider(provider, destroy_provider<G4CAN>);
    }

    ~EmbeddedCyphal() override {
        node_info_reader.reset();
        registers_handler.reset();
        clear_callback_subscriptions();
        detach_provider();
    }

    void set_mode(uint8_t mode) {
        _mode = mode;
    }

    void set_status(uint8_t status) {
        _health_status = status;
    }

    __attribute__((hot, flatten)) void cyphal_loop() {
        if (_is_cyphal_on) {
            loop();
        }
        if (_is_cyphal_on) {
            millis_t current_t = millis_32();
            in_loop_reporting(current_t);

            static millis_t heartbeat_time = 0;
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
            this->hfdcan,
            FDCAN_REJECT,
            FDCAN_REJECT,
            FDCAN_REJECT_REMOTE,
            FDCAN_REJECT_REMOTE
        );
    }

    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunused-parameter"
    // NOTE: <current_t> parameter required by the interface, but not used in this implementation
    virtual void in_loop_reporting(millis_t current_t) {
    #pragma GCC diagnostic pop
    }

    void begin() {
        finish_cyphal_setup();
        set_mode(uavcan_node_Mode_1_0_OPERATIONAL);
    }
};


#ifdef ARDUINO
template<size_t REGISTERS_COUNT = 0>
class ArduinoCyphal : public EmbeddedCyphal<128, 500, REGISTERS_COUNT> {
private:
    using Base = EmbeddedCyphal<128, 500, REGISTERS_COUNT>;

public:
    explicit ArduinoCyphal(
        FDCAN_HandleTypeDef* hfdcan,
        CanardNodeID node_id,
        std::string name = "org.voltbro.arduino.node",
        std::array<RegisterDefinition, REGISTERS_COUNT> registers_list = {}
    ):
        Base(
            hfdcan,
            node_id,
            std::move(name),
            std::move(registers_list)
        )
    {}

    void setup_subscriptions() override {
        HAL_IMPORTANT(HAL_FDCAN_ConfigGlobalFilter(
            this->hfdcan,
            FDCAN_ACCEPT_IN_RX_FIFO0,
            FDCAN_ACCEPT_IN_RX_FIFO0,
            FDCAN_REJECT_REMOTE,
            FDCAN_REJECT_REMOTE
        ));
    }
};
#undef millis_t
#undef micros_t
#undef millis_32
#undef micros_64
#endif

#endif
