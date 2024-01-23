#include "provider.h"
#include "cyphal/interfaces.h"

CanardTxQueue queue{};
CanardInstance canard{};

std::unique_ptr<AbstractAllocator> _alloc_ptr;


void AbstractCANProvider::process_canard_rx(CanardFrame* frame) {
    CanardRxTransfer transfer = {.payload = nullptr};
    CanardRxSubscription* subscription = nullptr;
    void (*processor)(CanardRxTransfer*) = nullptr;
    IListener<CanardRxTransfer*>* listener = nullptr;

    const int8_t accept_result = canardRxAccept(
        (CanardInstance* const)&canard,
        utilities.micros_64(),
        frame,
        0,
        &transfer,
        &subscription
    );
    if (accept_result == 0 || accept_result > 1) {
        // The received frame is either invalid or it's a non-last frame of a multi-frame transfer.
        return;
    }
    if (accept_result < 0) goto exit;
    if (subscription == nullptr) goto exit;

    listener = reinterpret_cast<IListener<CanardRxTransfer*>*>(subscription->user_reference);
    if (listener == nullptr) goto exit;
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
}
