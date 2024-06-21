#include "cyphal.h"

#ifdef __linux__
#include <iostream>
#endif

void CyphalInterface::push(
    const CanardMicrosecond tx_deadline_usec,
    const CanardTransferMetadata* const metadata,
    const size_t payload_size,
    const void* const payload
) const {
    provider->lock_canard();
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
        std::cerr << "[Error: OOM] Tried to send to port: " << metadata->port_id
                  << ", node: " << +metadata->remote_node_id << std::endl;
#else
        utilities.error_handler();
#endif
        return;
    }
    if (push_state < 0) {
        utilities.error_handler();
    }
    provider->unlock_canard();
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
        utilities.error_handler();
    }
}

void CyphalInterface::loop() {
    provider->can_loop();
}

void CyphalInterface::start_threads(uint64_t tx_delay_micros) {
    rx_terminate_flag.store(false);
    tx_terminate_flag.store(false);

    rx_thread = std::thread([=]() {
        std::cout << "Started RX thread" << std::endl;
        while(!rx_terminate_flag.load()) {
            this->loop();
        }
        std::cout << "Finished RX thread" << std::endl;
    });
    tx_thread = std::thread([=]() {
        std::cout << "Started TX thread" << std::endl;
        while(!tx_terminate_flag.load()) {
            this->provider->process_canard_tx();
            usleep(tx_delay_micros);
        }
        std::cout << "Finished TX thread" << std::endl;
    });

    rx_thread.detach();
    tx_thread.detach();
}

void CyphalInterface::stop_all_threads() {
    rx_terminate_flag.store(true);
    tx_terminate_flag.store(true);
}


CyphalInterface::~CyphalInterface() {
    stop_all_threads();
}
