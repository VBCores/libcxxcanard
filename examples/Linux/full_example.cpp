#include <cyphal/allocators/sys/sys_allocator.h>
#include <cyphal/cyphal.h>
#include <cyphal/providers/LinuxCAN.h>
#include <cyphal/subscriptions/subscription.h>
#include <cyphal_common_types.hpp>

#include <uavcan/_register/Access_1_0.hpp>
#include <voltbro/echo/echo_msg_1_0.hpp>
#include <voltbro/echo/echo_service_1_0.hpp>

#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <string>
#include <unistd.h>

using EchoMsg = voltbro_echo_echo_msg_1_0;
using EchoRequest = voltbro_echo_echo_service_Request_1_0;
using EchoResponse = voltbro_echo_echo_service_Response_1_0;
using RegisterAccessRequest = uavcan_register_Access_Request_1_0;
using RegisterAccessResponse = uavcan_register_Access_Response_1_0;

constexpr CanardPortID NATURAL32_RX_PORT_ID = 5000;
constexpr CanardPortID NATURAL32_TX_PORT_ID = 5001;
constexpr CanardPortID ECHO_MSG_PORT_ID = 5100;
constexpr CanardPortID ECHO_SERVICE_PORT_ID = 101;

constexpr uint8_t REGISTER_REAL32_TAG = 13U;
constexpr uint8_t REGISTER_NATURAL32_TAG = 9U;

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

void fill_register_name(uavcan_register_Name_1_0& out, const char* text) {
    const size_t size = std::min(std::strlen(text), sizeof(out.name.elements));
    std::memcpy(out.name.elements, text, size);
    out.name.count = size;
}

class Natural32Reader : public AbstractSubscription<UInt32> {
public:
    bool received = false;
    uint32_t value = 0;

    explicit Natural32Reader(InterfacePtr& interface)
        : AbstractSubscription<UInt32>(interface, NATURAL32_TX_PORT_ID) {}

private:
    void handler(const UInt32& msg, CanardRxTransfer*) override {
        received = true;
        value = msg.value;
    }
};

class EchoMsgReader : public AbstractSubscription<EchoMsg> {
public:
    bool received = false;
    std::string value;

    explicit EchoMsgReader(InterfacePtr& interface)
        : AbstractSubscription<EchoMsg>(interface, ECHO_MSG_PORT_ID) {}

private:
    void handler(const EchoMsg& msg, CanardRxTransfer*) override {
        received = true;
        value = to_string(msg.ping);
    }
};

class EchoResponseReader : public AbstractSubscription<EchoResponse> {
public:
    bool received = false;
    std::string value;

    explicit EchoResponseReader(InterfacePtr& interface)
        : AbstractSubscription<EchoResponse>(interface, ECHO_SERVICE_PORT_ID, CanardTransferKindResponse) {}

private:
    void handler(const EchoResponse& msg, CanardRxTransfer*) override {
        received = true;
        value = to_string(msg.pong);
    }
};

class RegisterResponseReader : public AbstractSubscription<RegisterAccessResponse> {
public:
    bool received = false;
    RegisterAccessResponse value{};

    explicit RegisterResponseReader(InterfacePtr& interface)
        : AbstractSubscription<RegisterAccessResponse>(
              interface,
              uavcan_register_Access_1_0_FIXED_PORT_ID_,
              CanardTransferKindResponse
          ) {}

private:
    void handler(const RegisterAccessResponse& msg, CanardRxTransfer*) override {
        received = true;
        value = msg;
    }
};

bool wait_for_register(CyphalInterface& interface, RegisterResponseReader& reader, uint64_t timeout_ms) {
    reader.received = false;
    return spin_until(interface, timeout_ms, [&]() {
        return reader.received && !interface.has_unsent_frames();
    });
}

int main(int argc, char** argv) {
    const Options options = parse_args(argc, argv);
    auto interface = make_interface(options);
    InterfacePtr interface_ref = interface;

    Natural32Reader natural_reader(interface_ref);
    EchoMsgReader echo_msg_reader(interface_ref);
    EchoResponseReader echo_response_reader(interface_ref);
    RegisterResponseReader register_reader(interface_ref);

    CanardTransferID natural_transfer_id = 0;
    UInt32 natural_sent{};
    natural_sent.value = 777U;
    interface->send_msg(&natural_sent, NATURAL32_RX_PORT_ID, &natural_transfer_id);

    const bool telemetry_ok = spin_until(*interface, options.timeout_ms, [&]() {
        return natural_reader.received &&
               echo_msg_reader.received &&
               !interface->has_unsent_frames();
    });
    if (!telemetry_ok) {
        std::cerr << "Timed out waiting for UInt32/EchoMsg telemetry" << std::endl;
        return 1;
    }
    if (echo_msg_reader.value != "hello from ArduinoCyphal") {
        std::cerr << "Unexpected echo message: `" << echo_msg_reader.value << "`" << std::endl;
        return 1;
    }

    CanardTransferID echo_request_transfer_id = 0;
    EchoRequest echo_request{};
    fill_string(echo_request.ping, "hil ping");
    interface->send_request(
        &echo_request,
        ECHO_SERVICE_PORT_ID,
        &echo_request_transfer_id,
        options.target_node_id
    );
    const bool echo_service_ok = spin_until(*interface, options.timeout_ms, [&]() {
        return echo_response_reader.received && !interface->has_unsent_frames();
    });
    if (!echo_service_ok || echo_response_reader.value != "hil ping") {
        std::cerr << "Echo service failed, response=`" << echo_response_reader.value << "`" << std::endl;
        return 1;
    }

    CanardTransferID register_transfer_id = 0;
    RegisterAccessRequest set_gain{};
    fill_register_name(set_gain.name, "control.gain");
    set_gain.value._tag_ = REGISTER_REAL32_TAG;
    set_gain.value.real32.value.elements[0] = 2.0F;
    set_gain.value.real32.value.count = 1;
    interface->send_request(
        &set_gain,
        uavcan_register_Access_1_0_FIXED_PORT_ID_,
        &register_transfer_id,
        options.target_node_id
    );
    if (!wait_for_register(*interface, register_reader, options.timeout_ms)) {
        std::cerr << "Timed out waiting for control.gain register response" << std::endl;
        return 1;
    }
    if (register_reader.value.value._tag_ != REGISTER_REAL32_TAG ||
        register_reader.value.value.real32.value.elements[0] != 2.0F) {
        std::cerr << "Unexpected control.gain register response" << std::endl;
        return 1;
    }

    RegisterAccessRequest read_last{};
    fill_register_name(read_last.name, "natural32.last");
    interface->send_request(
        &read_last,
        uavcan_register_Access_1_0_FIXED_PORT_ID_,
        &register_transfer_id,
        options.target_node_id
    );
    if (!wait_for_register(*interface, register_reader, options.timeout_ms)) {
        std::cerr << "Timed out waiting for natural32.last register response" << std::endl;
        return 1;
    }
    if (register_reader.value.value._tag_ != REGISTER_NATURAL32_TAG ||
        register_reader.value.value.natural32.value.elements[0] != natural_sent.value) {
        std::cerr << "Unexpected natural32.last register response" << std::endl;
        return 1;
    }

    std::cout << "full_example ok: telemetry UInt32=" << natural_reader.value
              << ", EchoMsg=`" << echo_msg_reader.value
              << "`, EchoService=`" << echo_response_reader.value
              << "`, natural32.last=" << register_reader.value.value.natural32.value.elements[0]
              << " via " << options.can_interface << std::endl;
    return 0;
}
