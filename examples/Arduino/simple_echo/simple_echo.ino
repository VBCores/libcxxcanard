#include <VBCoreG4_arduino_system.h>
#include <cyphal.h>
#include <cyphal_common_types.hpp>

constexpr CanardNodeID NODE_ID = 2;
constexpr CanardPortID ECHO_RX_PORT_ID = 5000;
constexpr CanardPortID ECHO_TX_PORT_ID = 5001;

CanFD canfd;
std::shared_ptr<ArduinoCyphal<>> cyphal;

void echo_handler(const UInt32& msg, CanardRxTransfer*) {
    Serial.print("received uint32: ");
    Serial.println(msg.value);

    UInt32 echo_msg = {.value = msg.value};

    static CanardTransferID echo_transfer_id = 0;
    cyphal->send_msg(
      &echo_msg,
      ECHO_TX_PORT_ID,
      &echo_transfer_id
    );
}

void setup() {
  Serial.begin(115200);

  SystemClock_Config();
  canfd.init();
  canfd.write_default_params();
  canfd.apply_config();

  //                           fdcan pointer, node id,             name
  cyphal = make_cyphal<ArduinoCyphal<>>(canfd.get_hfdcan(), NODE_ID, "org.voltbro.examples.simple_echo");
  cyphal->subscribe(ECHO_RX_PORT_ID, echo_handler);
  cyphal->begin();
  
  digitalWrite(LED1, HIGH);
}

void loop() {
  cyphal->cyphal_loop();
}
