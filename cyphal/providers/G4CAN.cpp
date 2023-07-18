#include "G4CAN.h"
#if (defined(STM32G474xx) || defined(STM32_G)) && defined(HAL_FDCAN_MODULE_ENABLED)
#include <cstring>

#include "FDCAN_generic.h"

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
        Error_Handler();
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
