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
        CanardFrame frame;
        bool has_read = read_frame(&frame);
        if (!has_read)
            break;
        process_canard_rx(&frame);
    }

    process_canard_tx();
}

static uint8_t RxData[64] = {};
bool G4CAN::read_frame(CanardFrame* rxf) {
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
        error_handler();
    }

    rxf->extended_can_id = RxHeader.Identifier;
    rxf->payload_size = dlc_to_len(RxHeader.DataLength);
    rxf->payload = (void*)RxData;
    return true;
}

uint32_t code_length( uint8_t length )
{
    if( length < 12 ) return (uint32_t)length << 16;
    if( length < 32 ) return (uint32_t)(length + 24 ) << 14;
    switch( length ) {
        case 32: return FDCAN_DLC_BYTES_32;
        case 48: return FDCAN_DLC_BYTES_48;
        case 64: return FDCAN_DLC_BYTES_64;
        default:
            error_handler();
    }
}

uint8_t TxData[64];
int G4CAN::write_frame(const CanardTxQueueItem* ti) {
    FDCAN_TxHeaderTypeDef TxHeader;
    if (HAL_FDCAN_GetTxFifoFreeLevel(handler) != 0)
    {
        // Add message to Tx FIFO
        TxHeader.Identifier = ti->frame.extended_can_id;
        TxHeader.IdType = FDCAN_EXTENDED_ID;
        TxHeader.TxFrameType = FDCAN_DATA_FRAME;
        //TxHeader.DataLength = code_length(ti->frame.payload_size);
        TxHeader.DataLength = CanardFDCANLengthToDLC[ti->frame.payload_size];
        TxHeader.ErrorStateIndicator = FDCAN_ESI_ACTIVE;
        TxHeader.BitRateSwitch = FDCAN_BRS_ON;
        TxHeader.FDFormat = FDCAN_FD_CAN;
        TxHeader.TxEventFifoControl = FDCAN_STORE_TX_EVENTS;
        TxHeader.MessageMarker = 0x00;
        if (HAL_FDCAN_AddMessageToTxFifoQ(handler, &TxHeader, (uint8_t *)ti->frame.payload) != HAL_OK)
        {
            error_handler();
        }

        return 0;
    }

    return 1;

    /*
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

    std::memcpy(TxData, (uint8_t*)ti->frame.payload, ti->frame.payload_size);

    // all mailboxes should be free -
    // https://forum.opencyphal.org/t/uavcan-v0-found-data-transfer-reversal/1476/6
    // "Reduce the number of enqueued frames to 1" - fix to inner priority inversion

    /*
    for (int i = 0; HAL_FDCAN_GetTxFifoFreeLevel(handler) != 3 && i < 3; i++) {
        delay_cycles(ONE_FULL_FRAME_CYCLES);
    } // wait for message to transmit
    if (HAL_FDCAN_GetTxFifoFreeLevel(handler) != 3) {
        return -1;
    }

    while (HAL_FDCAN_GetTxFifoFreeLevel(handler) != 3) {
    }

    if (HAL_FDCAN_AddMessageToTxFifoQ(handler, &TxHeader, TxData) != HAL_OK) {
        return -1;
    }
    return TxHeader.DataLength;*/
}
#endif
