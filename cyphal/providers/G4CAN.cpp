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
