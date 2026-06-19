#include <cyphal/allocators/sys/sys_allocator.h>
#include <cyphal/cyphal.h>
#include <cyphal/providers/LinuxCAN.h>

#include <voltbro/echo/echo_service_1_0.hpp>

#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <unistd.h>

using EchoRequest = voltbro_echo_echo_service_Request_1_0;
using EchoResponse = voltbro_echo_echo_service_Response_1_0;

constexpr CanardNodeID LOCAL_NODE_ID = 42;
constexpr CanardNodeID TARGET_NODE_ID = 2;
constexpr CanardPortID ECHO_SERVICE_PORT_ID = 101;
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

void fill_string(uavcan_primitive_String_1_0& out, const char* text) {
    const size_t size = std::min(std::strlen(text), sizeof(out.value.elements));
    std::memcpy(out.value.elements, text, size);
    out.value.count = size;
}

std::string to_string(const uavcan_primitive_String_1_0& value) {
    return std::string(
        reinterpret_cast<const char*>(value.value.elements),
        reinterpret_cast<const char*>(value.value.elements) + value.value.count
    );
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
    std::string response_text;
    interface->subscribe(ECHO_SERVICE_PORT_ID, CanardTransferKindResponse, [&](const EchoResponse& response, CanardRxTransfer*) {
        received = true;
        response_text = to_string(response.pong);
    });

    CanardTransferID transfer_id = 0;
    EchoRequest request{};
    fill_string(request.ping, "service hil");
    interface->send_request(&request, ECHO_SERVICE_PORT_ID, &transfer_id, TARGET_NODE_ID);

    const bool ok = spin_until(*interface, TIMEOUT_MS, [&]() {
        return received && !interface->has_unsent_frames();
    });
    if (!ok || response_text != "service hil") {
        std::cerr << "Echo service failed" << std::endl;
        return 1;
    }

    std::cout << "service_echo ok: " << response_text << std::endl;
    return 0;
}
