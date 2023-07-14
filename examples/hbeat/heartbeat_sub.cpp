#include "cyphal.h"
#include "subscriptions/subscription.h"
#include "providers/LinuxCAN.h"
#include "allocators/o1/o1_allocator.h"

#include <iostream>

#include "uavcan/node/Heartbeat_1_0.h"

void Error_Handler() {
    std::cout << "err" << std::endl;
}

class HBeatReader : public AbstractSubscription<uavcan_node_Heartbeat_1_0> {
    SUBSCRIPTION_BODY_FIXED_MESSAGE(
        HBeatReader,
        uavcan_node_Heartbeat_1_0
    )
    void handler(const uavcan_node_Heartbeat_1_0& hbeat, CanardRxTransfer* transfer) {
        std::cout << hbeat.uptime << " " << +transfer->metadata.remote_node_id << std::endl;
    }
};

int main() {
    auto interface = CyphalInterface(99);
    interface.setup<LinuxCAN, O1Allocator>("vcan0");
    auto reader = HBeatReader(&interface);
    while (1) {
        interface.loop();
    }
}