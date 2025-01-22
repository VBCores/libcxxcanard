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

void CyphalInterface::unsubscribe(CanardPortID port_id, CanardTransferKind kind) {
    if (canardRxUnsubscribe((CanardInstance* const)&provider->canard, kind, port_id) != 1) {
        utilities.error_handler();
    }
}

void CyphalInterface::loop() {
    provider->can_loop();
}

#ifdef __linux__
void CyphalInterface::start_threads(uint64_t tx_delay_micros) {
    threads_terminate_flag.store(false);

    rx_thread = std::thread([=]() {
        std::cout << "Started RX thread" << std::endl;
        while(!threads_terminate_flag.load()) {
            this->provider->can_loop(true);  // no_tx=true
        }
        std::cout << "Finished RX thread" << std::endl;
        is_rx_terminated.store(true);
    });
    tx_thread = std::thread([=]() {
        std::cout << "Started TX thread" << std::endl;
        while(!threads_terminate_flag.load()) {
            this->provider->process_canard_tx();
            usleep(tx_delay_micros);
        }
        std::cout << "Finished TX thread" << std::endl;
        is_tx_terminated.store(true);
    });

    rx_thread.detach();
    tx_thread.detach();
}

void CyphalInterface::stop_all_threads() {
    threads_terminate_flag.store(true);
}
#endif

CyphalInterface::~CyphalInterface() {
#ifdef __linux__
    stop_all_threads();
    while (!is_rx_terminated.load()) {}
    std::cout << "Waited for RX thread" << std::endl;
    while (!is_tx_terminated.load()) {}
    std::cout << "Waited for TX thread" << std::endl;
#endif
}
