#pragma once

#include "allocators/allocator.h"
#include "definitions.h"
#include "libcanard/canard.h"

class AbstractCANProvider {
    friend class CyphalInterface;

   protected:
    const size_t CANARD_MTU;
    const size_t WIRE_MTU;
    CanardTxQueue queue;
    CanardInstance canard;

   public:
    AbstractCANProvider() = delete;
    AbstractCANProvider(size_t canard_mtu, size_t wire_mtu)
        : WIRE_MTU(wire_mtu), CANARD_MTU(canard_mtu), canard{}, queue{} {};
    template <class T>
    CanardTxQueue* setup(CanardNodeID node_id) {
        auto memory_pair = get_memory_pair<T>();
        canard = canardInit(memory_pair[0], memory_pair[1]);
        canard.node_id = node_id;
        queue = canardTxInit(200, CANARD_MTU);
    }

    virtual uint32_t len_to_dlc(size_t len) = 0;
    virtual size_t dlc_to_len(uint32_t dlc) = 0;
    virtual void can_loop() = 0;
    virtual CanardFrame* read_frame() = 0;
    virtual int write_frame(const CanardTxQueueItem* ti) = 0;
    void process_canard_rx(CanardFrame*);
    void process_canard_tx();
};
