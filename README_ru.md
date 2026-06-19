# libcxxcanard

`libcxxcanard` - небольшая C++17-обертка над
[libcanard](https://github.com/OpenCyphal/libcanard). Библиотека оставляет
транспортную модель близкой к libcanard, но убирает повторяющийся код
сериализации, подписок и настройки provider.

Текущий верхнеуровневый API:

- `CyphalInterface` владеет CAN provider, allocator, очередями и подписками.
- `EmbeddedCyphal` наследуется от `CyphalInterface`; `ArduinoCyphal` наследуется от `EmbeddedCyphal`.
- `make_cyphal<T>(...)` - предпочтительный способ создать embedded node, потому что после него работает `shared_from_this()`.
- `AbstractSubscription<T>` остается для class-style обработчиков.
- `subscribe(port, callback)` и `subscribe(port, kind, callback)` доступны для callback-style обработчиков.
- `cyphal_common_types.hpp` дает короткие алиасы: `UInt32`, `Float32`, `CyphalString`, `Bytes`, `Empty` и др.
  В non-Arduino сборках также есть `String` как алиас для `CyphalString`; в Arduino остается штатный `String`.

## Платформы

### Arduino

Arduino использует упакованную библиотеку из `src/`. После изменения headers или
генерируемых include обновите пакет:

```sh
make arduino-lib
```

Скетчи лежат в [examples/Arduino](examples/Arduino/README.md). Минимальная
форма:

```cpp
#include <VBCoreG4_arduino_system.h>
#include <cyphal.h>
#include <cyphal_common_types.hpp>

CanFD canfd;
std::shared_ptr<ArduinoCyphal<>> cyphal;

void setup() {
    SystemClock_Config();
    canfd.init();
    canfd.write_default_params();
    canfd.apply_config();

    cyphal = make_cyphal<ArduinoCyphal<>>(
        canfd.get_hfdcan(),
        42,
        "org.example.node"
    );
    cyphal->begin();
}

void loop() {
    cyphal->cyphal_loop();
}
```

### Linux / CMake

Linux использует SocketCAN через `cyphal/providers/LinuxCAN.h`. Примеры в
[examples/Linux](examples/Linux/README.md) - обычные CMake executables; там же
показано, как подключить `libcxxcanard` и DSDL-репозитории проекта.

Нужно:

- CMake и C++17 compiler.
- `nnvg` или `uv` для Nunavut codegen.
- SocketCAN interface, например `vcan1.3` или `can0`.

Типовой CMake:

```cmake
find_package(Threads REQUIRED)

add_subdirectory(libcxxcanard)
include(libcxxcanard/examples/cyphal_types.cmake)

add_executable(app main.cpp)
target_link_libraries(app PRIVATE libcxxcanard Threads::Threads)
target_include_directories(app PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/libcxxcanard
    ${CMAKE_CURRENT_SOURCE_DIR}/libcxxcanard/libs
)
cyphal_add_dsdl_types(app
    TYPE_REPOS
        ${CMAKE_CURRENT_SOURCE_DIR}/cyphal_types/public_regulated_data_types
        ${CMAKE_CURRENT_SOURCE_DIR}/cyphal_types/voltbro_types
)
```

### STM32 HAL

Bare-metal STM32 проекты используют `cyphal/providers/G4CAN.h` напрямую.
Папка под такие примеры зарезервирована в
[examples/STM32HAL](examples/STM32HAL/README.md).

## Callback-Style Subscribe

`subscribe(port, callback)` подписывает на message. Payload type выводится из
аргумента callback.

```cpp
cyphal->subscribe(5000, [](const UInt32& msg, CanardRxTransfer*) {
    Serial.println(msg.value);
});
```

Для services или других transfer kinds передайте kind явно:

```cpp
using EchoRequest = voltbro_echo_echo_service_Request_1_0;
using EchoResponse = voltbro_echo_echo_service_Response_1_0;

cyphal->subscribe(101, CanardTransferKindRequest,
    [&](const EchoRequest& request, CanardRxTransfer* transfer) {
        EchoResponse response{};
        response.pong = request.ping;
        cyphal->send_response(&response, transfer);
    }
);
```

Если тип не выводится, укажите payload явно:

```cpp
cyphal->subscribe<UInt32>(5000, my_callable);
```

## Class-Style Subscribe

Class-style подписки удобны, когда handler хранит состояние или является частью
класса node.

```cpp
class UInt32Sub : public AbstractSubscription<UInt32> {
public:
    explicit UInt32Sub(InterfacePtr interface)
        : AbstractSubscription<UInt32>(interface, 5000) {}

private:
    void handler(const UInt32& msg, CanardRxTransfer*) override {
        Serial.println(msg.value);
    }
};

class AppCyphal : public ArduinoCyphal<> {
public:
    using ArduinoCyphal<>::ArduinoCyphal;

private:
    UInt32Sub* sub = nullptr;

    void setup_subscriptions() override {
        ArduinoCyphal<>::setup_subscriptions();
        sub = new UInt32Sub(shared_from_this());
    }
};
```

## Отправка Transfers

Message отправляется broadcast, transfer-ID ведется отдельно на subject:

```cpp
static CanardTransferID transfer_id = 0;

UInt32 msg{};
msg.value = 123;
cyphal->send_msg(&msg, 5000, &transfer_id);
```

Request требует remote node-ID:

```cpp
using EchoRequest = voltbro_echo_echo_service_Request_1_0;

static CanardTransferID transfer_id = 0;

EchoRequest request{};
fill_string(request.ping, "ping");
cyphal->send_request(&request, 101, &transfer_id, target_node_id);
```

Response берет metadata из входящего request:

```cpp
using EchoRequest = voltbro_echo_echo_service_Request_1_0;
using EchoResponse = voltbro_echo_echo_service_Response_1_0;

void on_echo_request(const EchoRequest& request, CanardRxTransfer* transfer) {
    EchoResponse response{};
    response.pong = request.ping;
    cyphal->send_response(&response, transfer);
}
```

## Примеры

- [Arduino examples](examples/Arduino/README.md): минимальный message echo, минимальный service echo и полный embedded node.
- [Linux examples](examples/Linux/README.md): SocketCAN peers, которые говорят с Arduino sketches.
- [STM32 HAL examples](examples/STM32HAL/README.md): заготовка для direct HAL проектов.
