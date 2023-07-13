#include "cyphal.h"

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
    if (push_state < 0) {
        Error_Handler();
    }
}

void CyphalInterface::subscribe(
    CanardPortID port_id,
    size_t extent,
    CanardRxSubscription* const subscription,
) {
    if (canardRxSubscribe(
            (CanardInstance* const)&provider->canard,
            CanardTransferKindRequest,
            port_id,
            extent,
            CANARD_DEFAULT_TRANSFER_ID_TIMEOUT_USEC,
            subscription
        ) != 1) {
        Error_Handler();
    }
}
