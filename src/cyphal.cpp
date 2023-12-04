#include "cyphal.h"

#ifdef __linux__

uint64_t micros_64() {
    struct timespec ts {};
    timespec_get(&ts, TIME_UTC);
    uint64_t us = SEC_TO_US((uint64_t)ts.tv_sec) + NS_TO_US((uint64_t)ts.tv_nsec);
    return us;
}

#endif

AbstractAllocator* allocator = nullptr;

#ifdef __linux__
#include <new>
#endif
#include <stdlib.h>

void* O1Allocator::allocate(CanardInstance* ins, size_t amount) {
    (void)ins;
    void* mem;

    CRITICAL_SECTION({ mem = o1heapAllocate(o1heap, amount); })

    return mem;
}

void O1Allocator::free(CanardInstance* ins, void* pointer) {
    (void)ins;
    CRITICAL_SECTION({ o1heapFree(o1heap, pointer); })
}

O1Allocator::O1Allocator(size_t size) {
#ifdef __linux__
    memory_arena = new(std::align_val_t{O1HEAP_ALIGNMENT}) uint8_t[size];
#else
    memory_arena = std::malloc(size);
#endif
    if (memory_arena == nullptr) {
        error_handler();
    }

#ifndef __linux__
    auto shift = (int)((uint8_t*)memory_arena) % O1HEAP_ALIGNMENT;
    if (shift != 0) {
        memory_arena = (void*)((uint8_t*)memory_arena + shift);
        size -= shift;
    }
#endif

    O1HeapInstance* out = o1heapInit(memory_arena, size);
    if (out == nullptr) {
        error_handler();
    }
    o1heap = out;
}

O1Allocator::~O1Allocator() {
#ifdef __linux__
    ::operator delete[](memory_arena, std::align_val_t{O1HEAP_ALIGNMENT});
#else
	std::free(memory_arena);
#endif
}
#include <cstdlib>

void* SystemAllocator::allocate(CanardInstance* const ins, const size_t amount) {
    (void)ins;
    void* mem;

    CRITICAL_SECTION({ mem = std::malloc(amount); })
    if (mem == nullptr) {
        error_handler();
    }
    return mem;
}

void SystemAllocator::free(CanardInstance* const ins, void* const pointer) {
    (void)ins;
    CRITICAL_SECTION({ std::free(pointer); })
}

#ifdef __linux__
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

const uint32_t CanardFDCANLengthToDLC[65] = {
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

size_t fdcan_dlc_to_len(uint32_t dlc) {
    auto dlc_index = (uint8_t)(dlc / 65536);
    if (dlc_index <= 8) {
        return dlc_index;
    }
    if (dlc_index <= 12) {
        return 8 + 4 * (dlc_index - 8);
    }
    return 32 + 16 * (dlc_index - 13);
}

CanardTxQueue queue{};
CanardInstance canard{};

#include <iostream>
void AbstractCANProvider::process_canard_rx(CanardFrame* frame) {
    CanardRxTransfer transfer = {.payload = nullptr};
    CanardRxSubscription* subscription = nullptr;
    void (*processor)(CanardRxTransfer*) = nullptr;
    IListener<CanardRxTransfer*>* listener = nullptr;

    const int8_t accept_result = canardRxAccept(
        (CanardInstance* const)&canard,
        micros_64(),
        frame,
        0,
        &transfer,
        &subscription
    );
    if (accept_result != 1) {
        goto exit;
    }
    if (subscription == nullptr) {
        goto exit;
    }
    listener = (IListener<CanardRxTransfer*>*)subscription->user_reference;
    if (listener == nullptr) {
        return;
    }
    listener->accept(&transfer);
exit:
    if (transfer.payload != nullptr) {
        canard.memory_free(&canard, transfer.payload);
    }
}

void AbstractCANProvider::process_canard_tx() {
    // Look at top of the TX queue of individual CAN frames
    while (queue.size != 0) {
        const CanardTxQueueItem* ti = canardTxPeek(&queue);

        if (0U == ti->tx_deadline_usec || ti->tx_deadline_usec > micros_64()) {
            int written = write_frame(ti);
            if (written < 0) {
                break;
            }
        }
        // After the frame is transmitted or if it has timed out while waiting,
        // pop it from the queue and deallocate:
        canard.memory_free(&canard, canardTxPop(&queue, ti));
    }
}
#if (defined(STM32G474xx) || defined(STM32_G)) && defined(HAL_FDCAN_MODULE_ENABLED)
#include <cstring>


uint32_t G4CAN::len_to_dlc(size_t len) {
    return CanardFDCANLengthToDLC[len];
}

size_t G4CAN::dlc_to_len(uint32_t dlc) {
    return fdcan_dlc_to_len(dlc);
}

void G4CAN::can_loop() {
    while (HAL_FDCAN_GetRxFifoFillLevel(handler, FDCAN_RX_FIFO0) != 0) {
        CanardFrame* frame = read_frame();
        if (frame == nullptr)
            break;
        process_canard_rx(frame);
        delete frame;
    }

    process_canard_tx();
}

uint8_t RxData[64] = {};
CanardFrame* G4CAN::read_frame() {
    // may want to check 2 FIFOs in the future
    uint32_t rx_fifo = -1;
    if (HAL_FDCAN_GetRxFifoFillLevel(handler, FDCAN_RX_FIFO0)) {
        rx_fifo = FDCAN_RX_FIFO0;
    } else if (HAL_FDCAN_GetRxFifoFillLevel(handler, FDCAN_RX_FIFO1)) {
        rx_fifo = FDCAN_RX_FIFO1;
    }

    if (rx_fifo == (uint32_t)-1) {
        return nullptr;
    }

    FDCAN_RxHeaderTypeDef RxHeader = {};
    if (HAL_FDCAN_GetRxMessage(handler, rx_fifo, &RxHeader, RxData) != HAL_OK) {
        error_handler();
    }

    auto rxf = new CanardFrame{};
    rxf->extended_can_id = RxHeader.Identifier;
    rxf->payload_size = dlc_to_len(RxHeader.DataLength);
    rxf->payload = (void*)RxData;
    return rxf;
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
    TxHeader.TxEventFifoControl = FDCAN_NO_TX_EVENTS;
    TxHeader.MessageMarker = 0x0;

    uint8_t TxData[64];

    std::memcpy(TxData, (uint8_t*)ti->frame.payload, ti->frame.payload_size);

    // all mailboxes should be free -
    // https://forum.opencyphal.org/t/uavcan-v0-found-data-transfer-reversal/1476/6
    // "Reduce the number of enqueued frames to 1" - fix to inner
    // priority inversion
    while (HAL_FDCAN_GetTxFifoFreeLevel(handler) != 3) {
    }  // wait for message to transmit

    if (HAL_FDCAN_AddMessageToTxFifoQ(handler, &TxHeader, TxData) != HAL_OK) {
        return -1;
    }
    return TxHeader.DataLength;
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
) {
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
        std::cerr << "[Error: OOM] Tried to send to port: " << metadata->port_id << ", node: "
<< +metadata->remote_node_id << std::endl;
#endif
        return;
    }
    if (push_state < 0) {
        error_handler();
    }
}

void CyphalInterface::subscribe(
    CanardPortID port_id,
    size_t extent,
    CanardTransferKind kind,
    CanardRxSubscription* subscription
) {
    if (canardRxSubscribe(
            (CanardInstance* const)&provider->canard,
            kind,
            port_id,
            extent,
            CANARD_DEFAULT_TRANSFER_ID_TIMEOUT_USEC,
            subscription
        ) != 1) {
        error_handler();
    }
}

void CyphalInterface::loop() {
    provider->can_loop();
}
