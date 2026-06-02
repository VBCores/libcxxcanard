#include <VBCoreG4_arduino_system.h>
#include <cyphal.h>

#include <uavcan/primitive/scalar/Natural32_1_0.hpp>

using Natural32 = uavcan_primitive_scalar_Natural32_1_0;

constexpr CanardNodeID NODE_ID = 2;
constexpr CanardPortID ECHO_RX_PORT_ID = 5000;
constexpr CanardPortID ECHO_TX_PORT_ID = 5001;

class Natural32EchoSub : public AbstractSubscription<Natural32> {
public:
  Natural32EchoSub(InterfacePtr interface):
    AbstractSubscription<Natural32>(interface, ECHO_RX_PORT_ID),
    interface(interface)
  {}

private:
  InterfacePtr interface;
  CanardTransferID echo_transfer_id = 0;

  void handler(const Natural32& msg, CanardRxTransfer*) override {
    Serial.print("echo natural32: ");
    Serial.println(msg.value);

    Natural32 echo_msg = {.value = msg.value};
    interface->send_msg(
      &echo_msg,
      ECHO_TX_PORT_ID,
      &echo_transfer_id
    );
  }
};

class EchoCyphal : public ArduinoCyphal<> {
public:
  using ArduinoCyphal<>::ArduinoCyphal;

private:
  Natural32EchoSub* echo_sub = nullptr;

  void setup_subscriptions() override {
    ArduinoCyphal<>::setup_subscriptions();
    echo_sub = new Natural32EchoSub(cyphal_interface);
  }
};

CanFD canfd;
EchoCyphal* cyphal = nullptr;

void setup() {
  Serial.begin(115200);

  SystemClock_Config();
  canfd.init();
  canfd.write_default_params();
  canfd.apply_config();

  cyphal = new EchoCyphal(canfd.get_hfdcan(), NODE_ID, "org.voltbro.examples.simple_echo");
  cyphal->begin();
  digitalWrite(LED1, HIGH);
}

void loop() {
  cyphal->cyphal_loop();
}
