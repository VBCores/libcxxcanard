#include <VBCoreG4_arduino_system.h>
#include <cyphal.h>

#include <algorithm>
#include <cstring>

#include <voltbro/echo/echo_service_1_0.hpp>

using EchoRequest = voltbro_echo_echo_service_Request_1_0;
using EchoResponse = voltbro_echo_echo_service_Response_1_0;

constexpr CanardNodeID NODE_ID = 2;
constexpr CanardPortID ECHO_SERVICE_PORT_ID = 101;

CanFD canfd;
std::shared_ptr<ArduinoCyphal<>> cyphal;

void copy_string(uavcan_primitive_String_1_0& out, const uavcan_primitive_String_1_0& in) {
  const size_t size = std::min<size_t>(in.value.count, sizeof(out.value.elements));
  memcpy(out.value.elements, in.value.elements, size);
  out.value.count = size;
}

void echo_service_handler(const EchoRequest& request, CanardRxTransfer* transfer) {
  EchoResponse response{};
  copy_string(response.pong, request.ping);
  cyphal->send_response(&response, transfer);

  Serial.print("echo service bytes: ");
  Serial.println(response.pong.value.count);
}

void setup() {
  Serial.begin(115200);

  SystemClock_Config();
  canfd.init();
  canfd.write_default_params();
  canfd.apply_config();

  cyphal = make_cyphal<ArduinoCyphal<>>(canfd.get_hfdcan(), NODE_ID, "org.voltbro.examples.service_echo");
  cyphal->subscribe(ECHO_SERVICE_PORT_ID, CanardTransferKindRequest, echo_service_handler);
  cyphal->begin();

  digitalWrite(LED1, HIGH);
}

void loop() {
  cyphal->cyphal_loop();
}
