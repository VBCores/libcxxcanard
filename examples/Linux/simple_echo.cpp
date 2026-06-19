#include <cyphal/allocators/sys/sys_allocator.h>
#include <cyphal/cyphal.h>
#include <cyphal/providers/LinuxCAN.h>
#include <cyphal_common_types.hpp>

#include <cstdlib>
#include <iostream>
#include <unistd.h>

constexpr CanardNodeID LOCAL_NODE_ID = 42;
constexpr CanardPortID ECHO_RX_PORT_ID = 5000;
constexpr CanardPortID ECHO_TX_PORT_ID = 5001;
constexpr uint64_t TIMEOUT_MS = 5000;

template <typename Predicate>
bool spin_until(CyphalInterface& interface, uint64_t timeout_ms, Predicate&& predicate) {
    const uint64_t deadline = _micros_64() + (timeout_ms * 1000U);
    while (_micros_64() < deadline) {
        interface.loop();
        if (predicate()) {
            return true;
        }
        usleep(1000);
    }
    return false;
}

int main() {
    UtilityConfig config(
        _micros_64,
        []() {
            std::cerr << "Cyphal error handler was called" << std::endl;
            std::exit(1);
        }
    );
    auto interface = CyphalInterface::create_heap<LinuxCAN, SystemAllocator>(
        LOCAL_NODE_ID,
        "vcan1.3",
        64,
        config
    );

    bool received = false;
    uint32_t echoed_value = 0;
    interface->subscribe(ECHO_TX_PORT_ID, [&](const UInt32& msg, CanardRxTransfer*) {
        received = true;
        echoed_value = msg.value;
    });

    CanardTransferID transfer_id = 0;
    UInt32 sent{};
    sent.value = static_cast<uint32_t>(_micros_64());
    interface->send_msg(&sent, ECHO_RX_PORT_ID, &transfer_id);

    const bool ok = spin_until(*interface, TIMEOUT_MS, [&]() {
        return received && !interface->has_unsent_frames();
    });
    if (!ok || echoed_value != sent.value) {
        std::cerr << "UInt32 echo failed" << std::endl;
        return 1;
    }

    std::cout << "simple_echo ok: UInt32=" << echoed_value << std::endl;
    return 0;
}
