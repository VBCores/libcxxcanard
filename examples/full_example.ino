#include <VBCoreG4_arduino_system.h>
#include <cyphal.h>

#include <uavcan/primitive/scalar/Natural32_1_0.hpp>
#include <voltbro/echo/echo_msg_1_0.hpp>
#include <voltbro/echo/echo_service_1_0.hpp>

using Natural32 = uavcan_primitive_scalar_Natural32_1_0;
using EchoMsg = voltbro_echo_echo_msg_1_0;
using EchoRequest = voltbro_echo_echo_service_Request_1_0;
using EchoResponse = voltbro_echo_echo_service_Response_1_0;

constexpr CanardNodeID NODE_ID = 2;
constexpr CanardPortID NATURAL32_RX_PORT_ID = 5000;
constexpr CanardPortID NATURAL32_TX_PORT_ID = 5001;
constexpr CanardPortID ECHO_MSG_PORT_ID = 5100;
constexpr CanardPortID ECHO_SERVICE_PORT_ID = 101;

bool telemetry_enabled = true;
float gain = 1.0F;
uint32_t last_natural32 = 0;

void fill_string(uavcan_primitive_String_1_0& out, const char* text) {
  const size_t size = std::min(strlen(text), sizeof(out.value.elements));
  memcpy(out.value.elements, text, size);
  out.value.count = size;
}

void copy_string(uavcan_primitive_String_1_0& out, const uavcan_primitive_String_1_0& in) {
  const size_t size = std::min<size_t>(in.value.count, sizeof(out.value.elements));
  memcpy(out.value.elements, in.value.elements, size);
  out.value.count = size;
}

std::array<RegisterDefinition, 3> make_registers() {
  return {{
    {"telemetry.enabled", [](const uavcan_register_Value_1_0& in, uavcan_register_Value_1_0& out, RegisterAccessResponse&) {
      parse_register_bit(in, telemetry_enabled);
      fill_register_bit(out, telemetry_enabled);
    }},
    {"control.gain", [](const uavcan_register_Value_1_0& in, uavcan_register_Value_1_0& out, RegisterAccessResponse&) {
      parse_register_real32(in, gain);
      fill_register_real32(out, gain);
    }},
    {"natural32.last", [](const uavcan_register_Value_1_0&, uavcan_register_Value_1_0& out, RegisterAccessResponse&) {
      fill_register_natural32(out, last_natural32);
    }},
  }};
}

class Natural32Sub : public AbstractSubscription<Natural32> {
public:
  Natural32Sub(InterfacePtr interface):
    AbstractSubscription<Natural32>(interface, NATURAL32_RX_PORT_ID)
  {}

private:
  void handler(const Natural32& msg, CanardRxTransfer*) override {
    last_natural32 = msg.value;
    Serial.print("rx natural32: ");
    Serial.println(last_natural32);
  }
};

class EchoMsgSub : public AbstractSubscription<EchoMsg> {
public:
  EchoMsgSub(InterfacePtr interface):
    AbstractSubscription<EchoMsg>(interface, ECHO_MSG_PORT_ID)
  {}

private:
  void handler(const EchoMsg& msg, CanardRxTransfer*) override {
    Serial.print("rx echo msg bytes: ");
    Serial.println(msg.ping.value.count);
  }
};

class EchoService : public AbstractSubscription<EchoRequest> {
public:
  EchoService(InterfacePtr interface):
    AbstractSubscription<EchoRequest>(interface, ECHO_SERVICE_PORT_ID, CanardTransferKindRequest),
    interface(interface)
  {}

private:
  InterfacePtr interface;

  void handler(const EchoRequest& request, CanardRxTransfer* transfer) override {
    EchoResponse response{};
    copy_string(response.pong, request.ping);
    interface->send_response(&response, transfer);
  }
};

class FullExampleCyphal : public ArduinoCyphal<3> {
public:
  FullExampleCyphal(FDCAN_HandleTypeDef* hfdcan, CanardNodeID node_id):
    ArduinoCyphal<3>(
      hfdcan,
      node_id,
      "org.voltbro.examples.full",
      make_registers()
    )
  {}

private:
  Natural32Sub* natural32_sub = nullptr;
  EchoMsgSub* echo_msg_sub = nullptr;
  EchoService* echo_service = nullptr;
  CanardTransferID natural32_transfer_id = 0;
  CanardTransferID echo_msg_transfer_id = 0;

  void setup_subscriptions() override {
    ArduinoCyphal<3>::setup_subscriptions();
    natural32_sub = new Natural32Sub(cyphal_interface);
    echo_msg_sub = new EchoMsgSub(cyphal_interface);
    echo_service = new EchoService(cyphal_interface);
  }

  void in_loop_reporting(uint32_t current_t) override {
    static uint32_t report_t = 0;
    EACH_N(current_t, report_t, 1000, {
      if (!telemetry_enabled) {
        return;
      }

      Natural32 natural_msg = {.value = static_cast<uint32_t>(current_t * gain)};
      cyphal_interface->send_msg(
        &natural_msg,
        NATURAL32_TX_PORT_ID,
        &natural32_transfer_id
      );

      EchoMsg echo_msg{};
      fill_string(echo_msg.ping, "hello from ArduinoCyphal");
      cyphal_interface->send_msg(
        &echo_msg,
        ECHO_MSG_PORT_ID,
        &echo_msg_transfer_id
      );

      digitalToggle(LED2);
    })
  }
};

CanFD canfd;
FullExampleCyphal* cyphal = nullptr;

void setup() {
  Serial.begin(115200);

  SystemClock_Config();
  canfd.init();
  canfd.write_default_params();
  canfd.apply_config();

  cyphal = new FullExampleCyphal(canfd.get_hfdcan(), NODE_ID);
  cyphal->begin();
  digitalWrite(LED1, HIGH);
}

void loop() {
  cyphal->cyphal_loop();
}
