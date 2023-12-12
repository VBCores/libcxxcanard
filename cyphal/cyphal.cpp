#include "cyphal.h"

#ifdef LINUX_CAN
#include <iostream>
#endif

void CyphalInterface::push(
    const CanardMicrosecond tx_deadline_usec,
    const CanardTransferMetadata* const metadata,
    const size_t payload_size,
    const void* const payload
) const {
    int32_t push_state = canardTxPush(
        &provider->queue,
        &provider->canard,
        tx_deadline_usec,
        metadata,
        payload_size,
        payload
    );
    if (push_state == -CANARD_ERROR_OUT_OF_MEMORY) {
#ifdef LINUX_CAN
        std::cerr << "[Error: OOM] Tried to send to port: " << metadata->port_id << ", node: " 
<< +metadata->remote_node_id << std::endl;
#else
        error_handler();
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
) const {
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
