# libcxxcanard

`libcxxcanard` is a small C++17 wrapper around
[libcanard](https://github.com/OpenCyphal/libcanard) and `o1heap`.
It keeps the Cyphal/CAN transport close to the underlying C API, but gives
application code a simpler interface:

- `CyphalInterface` owns the CAN provider, allocator, subscriptions, and queues.
- `AbstractSubscription<T>` deserializes incoming transfers and calls typed handlers.
- `send_msg`, `send_request`, and `send_response` handle serialization and sending.
- Linux builds use SocketCAN through `providers/LinuxCAN`.
- STM32 bare-metal projects use `providers/G4CAN`.
- Arduino builds should use the Arduino-formatted packed files from `src/`.

## DSDL Types

`libcxxcanard` expects every message/service type to have a generated
`CyphalTypeTraits<T>` specialization. The helper from
`cyphal_types/cyphal_types.cmake` generates:

- Nunavut C headers, for example `uavcan/primitive/scalar/Natural32_1_0.h`.
- C++ traits, for example `uavcan/primitive/scalar/Natural32_1_0.hpp`.

**Include `.hpp` files from C++ and Arduino code**. The `.hpp` file includes the
matching C header and registers the traits.

```cpp
#include <uavcan/primitive/scalar/Natural32_1_0.hpp>

using Natural32 = uavcan_primitive_scalar_Natural32_1_0;
```

## Arduino

- Clone `libcxxcanard` into your Arduino libraries directory,
  `.../Arduino/libraries/`.

Arduino builds use the specially packed library from `libcxxcanard/src`.
User code normally looks like this:

```cpp
#include <VBCoreG4_arduino_system.h>
#include <cyphal.h>

#include <uavcan/primitive/scalar/Natural32_1_0.hpp>

using Natural32 = uavcan_primitive_scalar_Natural32_1_0;
```

For STM32 and Arduino, the library provides `ArduinoCyphal<>` as the standard
embedded integration. User code normally overrides `setup_subscriptions()` and
`in_loop_reporting()`:

```cpp
class Natural32Sub : public AbstractSubscription<Natural32> {
public:
    Natural32Sub(InterfacePtr interface)
        : AbstractSubscription<Natural32>(interface, 5001) {}

private:
    void handler(const Natural32& msg, CanardRxTransfer*) override {
        Serial.println(msg.value);
    }
};

class AppCyphal : public ArduinoCyphal<> {
public:
    using ArduinoCyphal<>::ArduinoCyphal;

private:
    Natural32Sub* sub = nullptr;
    CanardTransferID transfer_id = 0;

    void setup_subscriptions() override {
        ArduinoCyphal<>::setup_subscriptions();
        sub = new Natural32Sub(cyphal_interface);
    }

    void in_loop_reporting(uint32_t now_ms) override {
        Natural32 msg{.value = now_ms};
        cyphal_interface->send_msg(&msg, 5000, &transfer_id);
    }
};
```

Arduino examples live in `examples/`:

- `examples/simple_echo.ino` is a small Natural32 echo sketch.
- `examples/full_example.ino` shows subscriptions, message publishing, service
  responses, and registers in one sketch.

## CMake

For ordinary CMake projects:

- [nnvg](https://nunavut.readthedocs.io/en/latest/index.html) and/or
  [uv](https://docs.astral.sh/uv/) must be available in the system.
- Clone `libcxxcanard` into the project.
- Create a directory for DSDL types, for example `cyphal_types`, clone all
  required type repositories into it, at least the
  [standard public regulated data types](https://github.com/OpenCyphal/public_regulated_data_types/),
  and put [cyphal_types.cmake](./examples/cyphal_types.cmake) there:
- The order is important: first `add_subdirectory(libcxxcanard)`, then `cyphal_add_dsdl_types`

```txt
cyphal_types/
    public_regulated_data_types/
    other_types/
    cyphal_types.cmake
```

- Add this to your `CMakeLists.txt`; replace `YOUR_TARGET_NAME` with your
  executable target name:

```cmake
add_subdirectory(libcxxcanard)
target_link_libraries(YOUR_TARGET_NAME PRIVATE libcxxcanard Threads::Threads)
target_include_directories(YOUR_TARGET_NAME PRIVATE
    ...  # your includes
    PATH/TO/libcxxcanard
    PATH/TO/libcxxcanard/libs
)
include(PATH/TO/cyphal_types/cyphal_types.cmake)
cyphal_add_dsdl_types(YOUR_TARGET_NAME
    TYPE_REPOS
        PATH/TO/cyphal_types/public_regulated_data_types
        PATH/TO/cyphal_types/voltbro_types  # optional
        PATH/TO/cyphal_types/other_types    # optional
)
```

### Quickstart

Minimal Linux/SocketCAN example: create an interface, send one
`uavcan.primitive.scalar.Natural32.1.0` message, and run the interface until the
TX queue is empty.

```cpp
#include <cstdlib>
#include <iostream>

#include <cyphal/allocators/sys/sys_allocator.h>
#include <cyphal/cyphal.h>
#include <cyphal/providers/LinuxCAN.h>

#include <uavcan/primitive/scalar/Natural32_1_0.hpp>

using Natural32 = uavcan_primitive_scalar_Natural32_1_0;

int main() {
    UtilityConfig utilities(
        _micros_64,
        []() {
            std::cerr << "Cyphal error" << std::endl;
            std::exit(1);
        }
    );

    auto interface = CyphalInterface::create_heap<LinuxCAN, SystemAllocator>(
        42,          // local node-ID
        "vcan1.3",   // SocketCAN interface
        64,          // TX queue length
        utilities
    );

    CanardTransferID transfer_id = 0;
    Natural32 msg{};
    msg.value = 123;

    interface->send_msg(&msg, 5000, &transfer_id);

    while (interface->has_unsent_frames()) {
        interface->loop();
    }
}
```

### Fuller Example

The usual application shape:

1. Create `UtilityConfig`.
2. Create `CyphalInterface` with the needed provider and allocator.
3. Define subscriptions by inheriting from `AbstractSubscription<T>`.
4. Call `interface->loop()` from the main loop or use threads.

The Linux provider can run RX/TX processing in background threads. In this
example, the VM sends `Natural32` to port `5000`, another node answers on port
`5001`, and the response handler immediately sends the next ping:

```cpp
#include <cstdlib>
#include <iostream>
#include <memory>

#include <cyphal/allocators/sys/sys_allocator.h>
#include <cyphal/cyphal.h>
#include <cyphal/providers/LinuxCAN.h>
#include <cyphal/subscriptions/subscription.h>

#include <uavcan/primitive/scalar/Natural32_1_0.hpp>

using Natural32 = uavcan_primitive_scalar_Natural32_1_0;

constexpr CanardPortID PING_PORT_ID = 5000;
constexpr CanardPortID PONG_PORT_ID = 5001;

class Natural32PingPong : public AbstractSubscription<Natural32> {
public:
    Natural32PingPong(InterfacePtr& interface)
        : AbstractSubscription<Natural32>(interface, PONG_PORT_ID),
          interface(interface) {}

private:
    InterfacePtr interface;
    CanardTransferID transfer_id = 0;

    void handler(const Natural32& msg, CanardRxTransfer*) override {
        std::cout << "pong=" << msg.value << std::endl;

        Natural32 ping{};
        ping.value = msg.value + 1;
        interface->send_msg(&ping, PING_PORT_ID, &transfer_id);
    }
};

int main() {
    UtilityConfig utilities(
        _micros_64,
        []() {
            std::cerr << "Cyphal error" << std::endl;
            std::exit(1);
        }
    );

    auto interface = CyphalInterface::create_heap<LinuxCAN, SystemAllocator>(
        42,
        "vcan1.3",
        64,
        utilities
    );
    InterfacePtr interface_ref = interface;

    Natural32PingPong ping_pong(interface_ref);

    CanardTransferID transfer_id = 0;
    Natural32 first_ping{};
    first_ping.value = 1;
    interface->send_msg(&first_ping, PING_PORT_ID, &transfer_id);

    interface->start_threads();
}
```

For services, subscribe with `CanardTransferKindRequest` or
`CanardTransferKindResponse`, then use `send_request()` or `send_response()`.
