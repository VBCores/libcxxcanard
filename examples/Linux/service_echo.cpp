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

constexpr CanardPortID ECHO_SERVICE_PORT_ID = 101;

struct Options {
    std::string can_interface = "vcan1.3";
    CanardNodeID node_id = 42;
    CanardNodeID target_node_id = 2;
    uint64_t timeout_ms = 5000;
};

uint64_t parse_u64(const char* value, const char* option_name) {
    char* end = nullptr;
    const unsigned long parsed = std::strtoul(value, &end, 10);
    if ((end == value) || (*end != '\0')) {
        std::cerr << "Invalid value for " << option_name << ": " << value << std::endl;
        std::exit(2);
    }
    return static_cast<uint64_t>(parsed);
}

Options parse_args(int argc, char** argv) {
    Options options;
    for (int index = 1; index < argc; index += 2) {
        if ((index + 1) >= argc) {
            std::cerr << "Missing value for " << argv[index] << std::endl;
            std::exit(2);
        }
        const std::string option = argv[index];
        const char* value = argv[index + 1];
        if (option == "--can") {
            options.can_interface = value;
        } else if (option == "--node-id") {
            options.node_id = static_cast<CanardNodeID>(parse_u64(value, option.c_str()));
        } else if (option == "--target-node-id") {
            options.target_node_id = static_cast<CanardNodeID>(parse_u64(value, option.c_str()));
        } else if (option == "--timeout-ms") {
            options.timeout_ms = parse_u64(value, option.c_str());
        } else {
            std::cerr << "Unknown option: " << option << std::endl;
            std::exit(2);
        }
    }
    return options;
}

std::shared_ptr<CyphalInterface> make_interface(const Options& options) {
    static UtilityConfig config(
        _micros_64,
        []() {
            std::cerr << "Cyphal error handler was called" << std::endl;
            std::exit(1);
        }
    );
    return CyphalInterface::create_heap<LinuxCAN, SystemAllocator>(
        options.node_id,
        options.can_interface,
        64,
        config
    );
}

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

int main(int argc, char** argv) {
    const Options options = parse_args(argc, argv);
    auto interface = make_interface(options);

    bool received = false;
    std::string response_text;
    interface->subscribe(ECHO_SERVICE_PORT_ID, CanardTransferKindResponse, [&](const EchoResponse& response, CanardRxTransfer*) {
        received = true;
        response_text = to_string(response.pong);
    });

    CanardTransferID transfer_id = 0;
    EchoRequest request{};
    fill_string(request.ping, "service hil");
    interface->send_request(&request, ECHO_SERVICE_PORT_ID, &transfer_id, options.target_node_id);

    const bool ok = spin_until(*interface, options.timeout_ms, [&]() {
        return received && !interface->has_unsent_frames();
    });
    if (!ok || response_text != "service hil") {
        std::cerr << "Echo service failed, response=`" << response_text << "`" << std::endl;
        return 1;
    }

    std::cout << "service_echo ok: `" << response_text
              << "` via " << options.can_interface << std::endl;
    return 0;
}
