#include "provider.h"
#include "interfaces.h"

CanardTxQueue queue{};
CanardInstance canard{};

#ifdef LINUX_CAN
uint64_t micros() {
    struct timespec ts {};
    timespec_get(&ts, TIME_UTC);
    uint64_t us = SEC_TO_US((uint64_t)ts.tv_sec) + NS_TO_US((uint64_t)ts.tv_nsec);
    return us;
}
#else
uint64_t micros() {
    return 0;
}
#endif

#include <iostream>
void AbstractCANProvider::process_canard_rx(CanardFrame* frame) {
    CanardRxTransfer transfer = {.payload = nullptr};
    CanardRxSubscription* subscription = nullptr;
    void (*processor)(CanardRxTransfer*) = nullptr;
    IListener<CanardRxTransfer*>* listener = nullptr;

    const int8_t accept_result = canardRxAccept(
        (CanardInstance* const)&canard,
        micros(),
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

        if (0U == ti->tx_deadline_usec || ti->tx_deadline_usec > micros()) {
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
