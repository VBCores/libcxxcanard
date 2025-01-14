#include "provider.h"
#include "cyphal/interfaces.h"

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
