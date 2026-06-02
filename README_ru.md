# libcxxcanard

`libcxxcanard` - небольшая C++17-обертка над
[libcanard](https://github.com/OpenCyphal/libcanard) и `o1heap`.
Библиотека оставляет Cyphal/CAN транспорт близким к исходному C API, но дает
более удобный интерфейс для прикладного кода:

- `CyphalInterface` владеет CAN provider, allocator, subscriptions и очередями.
- `AbstractSubscription<T>` десериализует входящие transfers и вызывает обработчики.
- `send_msg`, `send_request` и `send_response` для простой отправки сообщений, сериализации и пр.
- Linux-сборки используют SocketCAN через `providers/LinuxCAN`.
- STM32 bare-metal проекты: `providers/G4CAN`
- Arduino-сборки должны пользоваться упакованными по Arduino-формату файлами из `src/`

## DSDL Types

`libcxxcanard` ожидает, что у каждого message/service type есть сгенерированная
специализация `CyphalTypeTraits<T>`. Helper из
`cyphal_types/cyphal_types.cmake` генерирует:

- Nunavut C headers, например `uavcan/primitive/scalar/Natural32_1_0.h`.
- C++ traits, например `uavcan/primitive/scalar/Natural32_1_0.hpp`.

**В C++ и Arduino коде включайте именно `.hpp`**. Он подключает соответствующий C header и регистрирует traits.

```cpp
#include <uavcan/primitive/scalar/Natural32_1_0.hpp>

using Natural32 = uavcan_primitive_scalar_Natural32_1_0;
```

## Arduino

- Клонируйте `libcxxcanard` в папку с ардуино библиотеками, `.../Arduino/libraries/`

Arduino-сборки используют специальным образом упакованную библиотеку из `libcxxcanard/src`.
Для пользователя это выглядит так:

```cpp
#include <VBCoreG4_arduino_system.h>
#include <cyphal.h>

#include <uavcan/primitive/scalar/Natural32_1_0.hpp>

using Natural32 = uavcan_primitive_scalar_Natural32_1_0;
```

Для STM32 и Arduino в библиотеке есть `ArduinoCyphal<>` предоставляющий "эталонную" интеграцию.
В пользовательском коде обычно достаточно переопределить `setup_subscriptions()` и `in_loop_reporting()`:

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

Arduino-примеры лежат в `examples/`:

- `examples/simple_echo.ino` - маленький Natural32 echo sketch.
- `examples/full_example.ino` показывает subscriptions, message publishing,
  service responses и registers в одном sketch.

## CMake

Для обычных CMake проектов:

- В системе должен быть доступен [nnvg](https://nunavut.readthedocs.io/en/latest/index.html) И/ИЛИ [uv](https://docs.astral.sh/uv/)
- Клонируйте `libcxxcanard` в проект
- Создайте папку для типов, например `cyphal_types`, клонируйте в нее все нужные типы
(как минимум [стандартные](https://github.com/OpenCyphal/public_regulated_data_types/))
и положите в нее же [cyphal_types.cmake](./examples/cyphal_types.cmake):
- Порядок важен: сначала `add_subdirectory(libcxxcanard)`, затем `cyphal_add_dsdl_types`

```txt
cyphal_types/
    public_regulated_data_types/
    еще_какие-то_типы/
    cyphal_types.cmake
```

- Добавьте в свой CMakeLists.txt (замените YOUR_TARGET_NAME на название executable):

```cmake
add_subdirectory(libcxxcanard)
target_link_libraries(YOUR_TARGET_NAME PRIVATE libcxxcanard Threads::Threads)
target_include_directories(YOUR_TARGET_NAME PRIVATE
    ...  # ваши инклюды
    ПУТЬ/К/libcxxcanard
    ПУТЬ/К/libcxxcanard/libs
)
include(ПУТЬ/К/cyphal_types/cyphal_types.cmake)
cyphal_add_dsdl_types(YOUR_TARGET_NAME
    TYPE_REPOS
        ПУТЬ/К/cyphal_types/public_regulated_data_types
        ПУТЬ/К/cyphal_types/voltbro_types  # если есть
        ПУТЬ/К/cyphal_types/прочие_типы  # если есть
)
```

### Quickstart

Минимальный Linux/SocketCAN пример: создать interface, отправить одно сообщение
`uavcan.primitive.scalar.Natural32.1.0` и крутить interface, пока TX queue не
опустеет.

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

### Более полный пример

Обычная форма приложения:

1. Создать `UtilityConfig`.
2. Создать `CyphalInterface` с нужным provider и allocator.
3. Описать подписки через наследование от `AbstractSubscription<T>`.
4. Вызывать `interface->loop()` из main loop или использовать треды.

Linux provider умеет крутить RX/TX обработку в фоновых тредах. В этом примере
VM отправляет `Natural32` на порт `5000`, другая нода отвечает на порт `5001`,
а обработчик ответа сразу отправляет следующий ping:

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

Для services подпишитесь с `CanardTransferKindRequest` или
`CanardTransferKindResponse`, затем используйте `send_request()` или
`send_response()`.
