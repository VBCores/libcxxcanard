#include "cyphal.h"

#include <chrono>

#ifdef __linux__

uint64_t _micros_64() {
    using namespace std::chrono;
    int64_t microseconds_since_epoch =
        duration_cast<microseconds>(system_clock::now().time_since_epoch()).count();
    return static_cast<uint64_t>(microseconds_since_epoch);
}

// NOLINTBEGIN(cppcoreguidelines-avoid-non-const-global-variables)
const UtilityConfig DEFAULT_CONFIG(_micros_64, []() { exit(1); });
// NOLINTEND(cppcoreguidelines-avoid-non-const-global-variables)

#endif

#ifdef __linux__
#include <new>
#endif
#include <cstdlib>

void* O1Allocator::allocate(CanardInstance* ins, size_t amount) {
    (void)ins;
    void* mem = nullptr;

    CRITICAL_SECTION({ mem = o1heapAllocate(o1heap, amount); })

    return mem;
}

void O1Allocator::free(CanardInstance* ins, void* pointer) {
    (void)ins;
    CRITICAL_SECTION({ o1heapFree(o1heap, pointer); })
}

void O1Allocator::align_self(size_t size) {
    if (!is_self_allocated) {
        auto loc = reinterpret_cast<uintptr_t>(memory_arena);
        auto shift = loc % O1HEAP_ALIGNMENT;
        if (shift != 0) {
            // NOLINTBEGIN(performance-no-int-to-ptr)
            memory_arena = reinterpret_cast<void*>(loc + shift);
            // NOLINTEND(performance-no-int-to-ptr)
            size -= shift;
        }
    }

    O1HeapInstance* out = o1heapInit(memory_arena, size);
    if (out == nullptr) {
        utilities.error_handler();
    }
    o1heap = out;
}

O1Allocator::O1Allocator(size_t size, void* memory, const UtilityConfig& utilities)
    : AbstractAllocator(size, utilities), memory_arena(memory) {
    align_self(size);
}

O1Allocator::O1Allocator(size_t size, const UtilityConfig& utilities)
    : AbstractAllocator(size, utilities),
      memory_arena(operator new(size, std::align_val_t{O1HEAP_ALIGNMENT})) {
    if (memory_arena == nullptr) {
        utilities.error_handler();
    }
    is_self_allocated = true;

    align_self(size);
}

O1Allocator::~O1Allocator() {
    if (!is_self_allocated) {
        return;
    }
    operator delete(memory_arena, std::align_val_t{O1HEAP_ALIGNMENT});
}
#include <cstdlib>

void* SystemAllocator::allocate(CanardInstance* const ins, const size_t amount) {
    (void)ins;
    void* mem = nullptr;

    // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-no-malloc,hicpp-no-malloc)
    CRITICAL_SECTION({ mem = std::malloc(amount); })
    // NOLINTEND(cppcoreguidelines-owning-memory,cppcoreguidelines-no-malloc,hicpp-no-malloc)

    if (mem == nullptr) {
        utilities.error_handler();
    }
    return mem;
}

void SystemAllocator::free(CanardInstance* const ins, void* const pointer) {
    (void)ins;

    // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-no-malloc,hicpp-no-malloc)
    CRITICAL_SECTION({ std::free(pointer); })
    // NOLINTEND(cppcoreguidelines-owning-memory,cppcoreguidelines-no-malloc,hicpp-no-malloc)
}

#if defined(__linux__) || defined(ARDUINO)
#define FDCAN_DLC_BYTES_0 ((uint32_t)0x00000000U)  /*!< 0 bytes data field  */
#define FDCAN_DLC_BYTES_1 ((uint32_t)0x00010000U)  /*!< 1 bytes data field  */
#define FDCAN_DLC_BYTES_2 ((uint32_t)0x00020000U)  /*!< 2 bytes data field  */
#define FDCAN_DLC_BYTES_3 ((uint32_t)0x00030000U)  /*!< 3 bytes data field  */
#define FDCAN_DLC_BYTES_4 ((uint32_t)0x00040000U)  /*!< 4 bytes data field  */
#define FDCAN_DLC_BYTES_5 ((uint32_t)0x00050000U)  /*!< 5 bytes data field  */
#define FDCAN_DLC_BYTES_6 ((uint32_t)0x00060000U)  /*!< 6 bytes data field  */
#define FDCAN_DLC_BYTES_7 ((uint32_t)0x00070000U)  /*!< 7 bytes data field  */
#define FDCAN_DLC_BYTES_8 ((uint32_t)0x00080000U)  /*!< 8 bytes data field  */
#define FDCAN_DLC_BYTES_12 ((uint32_t)0x00090000U) /*!< 12 bytes data field */
#define FDCAN_DLC_BYTES_16 ((uint32_t)0x000A0000U) /*!< 16 bytes data field */
#define FDCAN_DLC_BYTES_20 ((uint32_t)0x000B0000U) /*!< 20 bytes data field */
#define FDCAN_DLC_BYTES_24 ((uint32_t)0x000C0000U) /*!< 24 bytes data field */
#define FDCAN_DLC_BYTES_32 ((uint32_t)0x000D0000U) /*!< 32 bytes data field */
#define FDCAN_DLC_BYTES_48 ((uint32_t)0x000E0000U) /*!< 48 bytes data field */
#define FDCAN_DLC_BYTES_64 ((uint32_t)0x000F0000U) /*!< 64 bytes data field */
#endif

const std::array<uint32_t, 65> CanardFDCANLengthToDLC = {
    // 0-8
    FDCAN_DLC_BYTES_0,
    FDCAN_DLC_BYTES_1,
    FDCAN_DLC_BYTES_2,
    FDCAN_DLC_BYTES_3,
    FDCAN_DLC_BYTES_4,
    FDCAN_DLC_BYTES_5,
    FDCAN_DLC_BYTES_6,
    FDCAN_DLC_BYTES_7,
    FDCAN_DLC_BYTES_8,
    // 9-12
    FDCAN_DLC_BYTES_12,
    FDCAN_DLC_BYTES_12,
    FDCAN_DLC_BYTES_12,
    FDCAN_DLC_BYTES_12,
    // 13-16
    FDCAN_DLC_BYTES_16,
    FDCAN_DLC_BYTES_16,
    FDCAN_DLC_BYTES_16,
    FDCAN_DLC_BYTES_16,
    // 17-20
    FDCAN_DLC_BYTES_20,
    FDCAN_DLC_BYTES_20,
    FDCAN_DLC_BYTES_20,
    FDCAN_DLC_BYTES_20,
    // 20-24
    FDCAN_DLC_BYTES_24,
    FDCAN_DLC_BYTES_24,
    FDCAN_DLC_BYTES_24,
    FDCAN_DLC_BYTES_24,
    // 24-32
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    // 33-48
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    // 49-64
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
};

constexpr int MAX_16BIT = 65536;
constexpr int GAP_1_INDICIES = 8;
constexpr int GAP_4 = 4;
constexpr int GAP_4_INDICIES = 12;
constexpr int GAP_16 = 4;
constexpr int GAP_16_INDICIES_OFFSET = 32;

size_t fdcan_dlc_to_len(uint32_t dlc) {
    auto dlc_index = dlc;
    if (dlc_index <= GAP_1_INDICIES) {
        return dlc_index;
    }
    if (dlc_index <= GAP_4_INDICIES) {
        return GAP_1_INDICIES + GAP_4 * (dlc_index - GAP_1_INDICIES);
    }
    return GAP_16_INDICIES_OFFSET + GAP_16 * (dlc_index - (GAP_4_INDICIES + 1));
}

std::unique_ptr<AbstractAllocator> _alloc_ptr;

void AbstractCANProvider::process_canard_rx(CanardFrame* frame) {
    lock_canard();

    CanardRxTransfer transfer = {.payload = nullptr};
    CanardRxSubscription* subscription = nullptr;

    const int8_t accept_result = canardRxAccept(
        (CanardInstance* const)&canard,
        utilities.micros_64(),
        frame,
        0,
        &transfer,
        &subscription
    );

    if (accept_result == -CANARD_ERROR_OUT_OF_MEMORY) {
        utilities.error_handler();
    } else if (accept_result < 0) {
        // Invalid arguments
        return;
    } else if (accept_result == 1) {
        if (subscription != nullptr) {
            auto listener =
                static_cast<IListener<CanardRxTransfer*>*>(subscription->user_reference);
            if (listener != nullptr) {
                listener->accept(&transfer);
            }
        }
        canard.memory_free(&canard, transfer.payload);
    } else {  // accept_result == 0 || accept_result > 1
        // The received frame is either invalid or it's a non-last frame of a multi-frame transfer.
    }

    unlock_canard();
}

void AbstractCANProvider::process_canard_tx() {
    lock_canard();

    // Look at top of the TX queue of individual CAN frames
    while (queue.size != 0) {
        const CanardTxQueueItem* ti = canardTxPeek(&queue);

        if (0U == ti->tx_deadline_usec || ti->tx_deadline_usec > utilities.micros_64()) {
            int written = write_frame(ti);
            if (written < 0) {
                break;
            }
        }
        // After the frame is transmitted or if it has timed out while waiting,
        // pop it from the queue and deallocate:
        canard.memory_free(&canard, canardTxPop(&queue, ti));
    }

    unlock_canard();
}

void AbstractCANProvider::clear_queue() {
    lock_canard();
    while (queue.size != 0) {
        const CanardTxQueueItem* ti = canardTxPeek(&queue);
        canard.memory_free(&canard, canardTxPop(&queue, ti));
    }
    unlock_canard();
};

AbstractCANProvider::~AbstractCANProvider() = default;
#if (defined(STM32G474xx) || defined(STM32_G)) && defined(HAL_FDCAN_MODULE_ENABLED)
#include <cstring>


uint32_t G4CAN::len_to_dlc(size_t len) {
    return CanardFDCANLengthToDLC[len];
}

size_t G4CAN::dlc_to_len(uint32_t dlc) {
    return fdcan_dlc_to_len(dlc);
}

void G4CAN::can_loop(bool no_tx) {
    while (HAL_FDCAN_GetRxFifoFillLevel(handler, FDCAN_RX_FIFO0) != 0) {
        CanardFrame frame;
        uint8_t RxData[64] = {};
        bool has_read = read_frame(&frame, static_cast<void*>(RxData));
        if (!has_read)
            break;
        process_canard_rx(&frame);
    }

    if (!no_tx) {
        process_canard_tx();
    }

    static FDCAN_ProtocolStatusTypeDef fdcan_status;
    HAL_FDCAN_GetProtocolStatus(handler, &fdcan_status);
    if (fdcan_status.BusOff) {
        CLEAR_BIT(handler->Instance->CCCR, FDCAN_CCCR_INIT);
    }
}

bool G4CAN::read_frame(CanardFrame* rxf, void* data) {
    uint8_t* RxData = static_cast<uint8_t*>(data);
    // may want to check 2 FIFOs in the future
    uint32_t rx_fifo = -1;
    if (HAL_FDCAN_GetRxFifoFillLevel(handler, FDCAN_RX_FIFO0)) {
        rx_fifo = FDCAN_RX_FIFO0;
    } else if (HAL_FDCAN_GetRxFifoFillLevel(handler, FDCAN_RX_FIFO1)) {
        rx_fifo = FDCAN_RX_FIFO1;
    }

    if (rx_fifo == (uint32_t)-1) {
        return false;
    }

    FDCAN_RxHeaderTypeDef RxHeader = {};
    if (HAL_FDCAN_GetRxMessage(handler, rx_fifo, &RxHeader, RxData) != HAL_OK) {
        utilities.error_handler();
    }

    rxf->extended_can_id = RxHeader.Identifier;
    rxf->payload_size = dlc_to_len(RxHeader.DataLength);
    rxf->payload = data;
    return true;
}

int G4CAN::write_frame(const CanardTxQueueItem* ti) {
    FDCAN_TxHeaderTypeDef TxHeader;

    TxHeader.Identifier = ti->frame.extended_can_id;
    TxHeader.IdType = FDCAN_EXTENDED_ID;
    TxHeader.TxFrameType = FDCAN_DATA_FRAME;
    TxHeader.DataLength = CanardFDCANLengthToDLC[ti->frame.payload_size];
    TxHeader.ErrorStateIndicator = FDCAN_ESI_ACTIVE;
    TxHeader.BitRateSwitch = FDCAN_BRS_ON;
    TxHeader.FDFormat = FDCAN_FD_CAN;
    TxHeader.TxEventFifoControl = FDCAN_STORE_TX_EVENTS;
    TxHeader.MessageMarker = 0x0;

    // all mailboxes should be free -
    // https://forum.opencyphal.org/t/uavcan-v0-found-data-transfer-reversal/1476/6
    // "Reduce the number of enqueued frames to 1" - fix to inner priority inversion
    for (int i = 0; HAL_FDCAN_GetTxFifoFreeLevel(handler) != 3 && i < 3; i++) {
        delay_cycles(ONE_FULL_FRAME_CYCLES);
    }  // wait for message to transmit
    if (HAL_FDCAN_GetTxFifoFreeLevel(handler) != 3) {
        return -1;
    }

    if (HAL_FDCAN_AddMessageToTxFifoQ(handler, &TxHeader, (uint8_t*)ti->frame.payload) != HAL_OK) {
        return -1;
    }
    return TxHeader.DataLength;
}

HAL_StatusTypeDef apply_filter(G4CAN::Handler hfdcan, FDCAN_FilterTypeDef* hw_filter, const CanardFilter& filter) {
    static uint32_t filter_index = 0;

    hw_filter->IdType = FDCAN_EXTENDED_ID;
    hw_filter->FilterIndex = filter_index;
    hw_filter->FilterType = FDCAN_FILTER_MASK;
    hw_filter->FilterConfig = FDCAN_FILTER_TO_RXFIFO0;
    hw_filter->FilterID1 = filter.extended_can_id;
    hw_filter->FilterID2 = filter.extended_mask;
    HAL_StatusTypeDef result = HAL_FDCAN_ConfigFilter(hfdcan, hw_filter);

    if (result == HAL_OK) {
        filter_index += 1;
    }
    return result;
}
#endif

#ifdef __linux__
#include <iostream>
#endif

void CyphalInterface::push(
    const CanardMicrosecond tx_deadline_usec,
    const CanardTransferMetadata* const metadata,
    const size_t payload_size,
    const void* const payload
) const {
    provider->lock_canard();
    int32_t push_state = canardTxPush(
        &provider->queue,
        &provider->canard,
        tx_deadline_usec,
        metadata,
        payload_size,
        payload
    );
    if (push_state == -CANARD_ERROR_OUT_OF_MEMORY) {
#ifdef __linux__
        std::cerr << "[Error: OOM] Tried to send to port: " << metadata->port_id
                  << ", node: " << +metadata->remote_node_id << std::endl;
#else
        utilities.error_handler();
#endif
        return;
    }
    if (push_state < 0) {
        utilities.error_handler();
    }
    provider->unlock_canard();
}

void CyphalInterface::subscribe(
    CanardPortID port_id,
    size_t extent,
    CanardTransferKind kind,
    CanardRxSubscription* subscription
) const {
    if (canardRxSubscribe(
            (CanardInstance* const)&provider->canard,
            kind,
            port_id,
            extent,
            CANARD_DEFAULT_TRANSFER_ID_TIMEOUT_USEC,
            subscription
        ) != 1) {
        utilities.error_handler();
    }
}

void CyphalInterface::loop() {
    provider->can_loop();
}

#ifdef __linux__
void CyphalInterface::start_threads(uint64_t tx_delay_micros) {
    threads_terminate_flag.store(false);

    rx_thread = std::thread([=]() {
        std::cout << "Started RX thread" << std::endl;
        while(!threads_terminate_flag.load()) {
            this->provider->can_loop(true);  // no_tx=true
        }
        std::cout << "Finished RX thread" << std::endl;
        is_rx_terminated.store(true);
    });
    tx_thread = std::thread([=]() {
        std::cout << "Started TX thread" << std::endl;
        while(!threads_terminate_flag.load()) {
            this->provider->process_canard_tx();
            usleep(tx_delay_micros);
        }
        std::cout << "Finished TX thread" << std::endl;
        is_tx_terminated.store(true);
    });

    rx_thread.detach();
    tx_thread.detach();
}

void CyphalInterface::stop_all_threads() {
    threads_terminate_flag.store(true);
}
#endif

CyphalInterface::~CyphalInterface() {
#ifdef __linux__
    stop_all_threads();
    while (!is_rx_terminated.load()) {}
    std::cout << "Waited for RX thread" << std::endl;
    while (!is_tx_terminated.load()) {}
    std::cout << "Waited for TX thread" << std::endl;
#endif
}
#if (defined(STM32G474xx) || defined(STM32_G))

#include "stm32g4xx_ll_utils.h"

NodeInfoReader::NodeInfoReader(
    InterfacePtr interface,
    std::string&& name,
    uavcan_node_Version_1_0&& protocol_version,
    uavcan_node_Version_1_0&& hardware_version,
    uavcan_node_Version_1_0&& software_version,
    uint64_t software_vcs_revision_id
): AbstractSubscription<NodeInfoRequest>(
    interface,
    uavcan_node_GetInfo_1_0_FIXED_PORT_ID_,
    CanardTransferKindRequest
) {
    node_info.protocol_version = std::move(protocol_version);
    node_info.hardware_version = std::move(hardware_version);
    node_info.software_version = std::move(software_version);
    node_info.software_vcs_revision_id = software_vcs_revision_id;

    node_info.certificate_of_authenticity.count = 0;
    node_info.software_image_crc.count = 0;

    strcpy((char*)node_info.name.elements, name.c_str());
    node_info.name.count = name.size();

    uint32_t word0 = LL_GetUID_Word0();
    uint32_t word1 = LL_GetUID_Word1();
    uint32_t word2 = LL_GetUID_Word2();
    memcpy(node_info.unique_id, &word0, 4);
    memcpy(node_info.unique_id + 4, &word1, 4);
    memcpy(node_info.unique_id + 8, &word2, 4);
};

void NodeInfoReader::handler(
    const uavcan_node_GetInfo_Request_1_0& object,
    CanardRxTransfer* transfer
) {
    interface->send_response<NodeInfoResponse>(&node_info, transfer);
}
#endif
