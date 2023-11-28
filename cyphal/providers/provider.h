#pragma once

#include "cyphal/allocators/allocator.h"
#include "cyphal/definitions.h"
#include "libcanard/canard.h"

class AbstractCANProvider {
    friend class CyphalInterface;

protected:
    const size_t CANARD_MTU;
    const size_t WIRE_MTU;
    CanardTxQueue queue;
    CanardInstance canard;

public:
    typedef void Handler;

    AbstractCANProvider() = delete;
    AbstractCANProvider(size_t canard_mtu, size_t wire_mtu)
        : WIRE_MTU(wire_mtu), CANARD_MTU(canard_mtu), canard{}, queue{} {};

    template <class T, class... Args>
    void setup(CanardNodeID node_id, Args&&... args) {
        auto memory_pair = get_memory_pair<T>(args...);
        canard = canardInit(std::get<0>(memory_pair), std::get<1>(memory_pair));
        canard.node_id = node_id;
        queue = canardTxInit(200, CANARD_MTU);
    }

    virtual uint32_t len_to_dlc(size_t len) = 0;
    virtual size_t dlc_to_len(uint32_t dlc) = 0;
    virtual void can_loop() = 0;
    virtual bool read_frame(CanardFrame*)  = 0;
    virtual int write_frame(const CanardTxQueueItem* ti) = 0;
    void process_canard_rx(CanardFrame*);
    void process_canard_tx();

    virtual ~AbstractCANProvider() {
        auto allocator_obj = get_allocator();
        if (allocator_obj != nullptr) {
            delete allocator_obj;
        }
    };
};
