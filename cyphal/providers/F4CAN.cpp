#include "F4CAN.h"
#if (defined(STM32F446xx) || defined(STM32_F)) && defined(HAL_CAN_MODULE_ENABLED)
#include <cstring>

uint32_t F4CAN::len_to_dlc(size_t len) {
    return CanardCANLengthToDLC[len];
}

size_t F4CAN::dlc_to_len(uint32_t dlc) {
    return CanardCANDLCToLength[dlc];
}

void F4CAN::can_loop() {
    while (HAL_CAN_GetRxFifoFillLevel(handler, FDCAN_RX_FIFO0) != 0) {
        CanardFrame frame;
        bool has_read = read_frame(&frame);
        if (!has_read)
            break;
        process_canard_rx(&frame);
    }

    process_canard_tx();
}

bool F4CAN::read_frame(CanardFrame* rxf) () {
    uint32_t rx_fifo = -1;
    if (HAL_CAN_GetRxFifoFillLevel(handler, CAN_RX_FIFO0)) {
        rx_fifo = CAN_RX_FIFO0;
    } else if (HAL_CAN_GetRxFifoFillLevel(handler, CAN_RX_FIFO1)) {
        rx_fifo = CAN_RX_FIFO1;
    }

    if (rx_fifo == (uint32_t)-1) {
        return false;
    }

    CAN_RxHeaderTypeDef RxHeader = {};
    uint8_t RxData[64] = {};
    if (HAL_CAN_GetRxMessage(handler, rx_fifo, &RxHeader, RxData) != HAL_OK) {
        error_handler();
    }

    rxf->extended_can_id = RxHeader->ExtId;
    rxf->payload_size = CanardCANDLCToLength[RxHeader->DLC];
    rxf->payload = (void*)RxData;
    return true;
}

int F4CAN::write(const CanardTxQueueItem* ti) {
    CAN_TxHeaderTypeDef TxHeader;
    TxHeader.IDE = CAN_ID_EXT;
    TxHeader.RTR = CAN_RTR_DATA;
    TxHeader.DLC = CanardCANLengthToDLC[ti->frame.payload_size];
    TxHeader.ExtId = ti->frame.extended_can_id;
    TxHeader.TransmitGlobalTime = DISABLE;

    uint8_t TxData[8];

    std::memcpy(TxData, (uint8_t*)ti->frame.payload, ti->frame.payload_size);

    // all mailboxes should be free -
    // https://forum.opencyphal.org/t/uavcan-v0-found-data-transfer-reversal/1476/6
    // "Reduce the number of enqueued frames to 1" - fix to inner
    // priority inversion
    while (HAL_CAN_GetTxMailboxesFreeLevel(handler) != 3) {
    }  // wait for message to transmit

    if (HAL_CAN_AddTxMessage(handler, &TxHeader, TxData) != HAL_OK) {
        return -1;
    }
    return TxHeader.DLC;
}
#endif