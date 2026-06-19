# Linux Examples

Эта папка специально плоская: `CMakeLists.txt` и несколько `.cpp` peers. Примеры
можно скопировать в обычный SocketCAN проект или использовать как reference.

Ожидаемая структура проекта:

```txt
project/
    CMakeLists.txt
    simple_echo.cpp
    service_echo.cpp
    full_example.cpp
    libcxxcanard/
    cyphal_types/
        public_regulated_data_types/
        voltbro_types/
```

`CMakeLists.txt` можно запускать и прямо из этого checkout. Он сам находит
`libcxxcanard`, если запущен из `examples/Linux`; иначе задайте
`LIBCXXCANARD_DIR`. Если DSDL type repositories лежат не рядом с
`libcxxcanard`, задайте `CYPHAL_TYPES_DIR`.

## Сборка

```sh
CYPHAL_TYPES_DIR=/home/igor/Projects/libsws/cyphal_types \
cmake -S examples/Linux -B /tmp/libcxxcanard-linux-build

cmake --build /tmp/libcxxcanard-linux-build
```

## Запуск

`simple_echo` говорит с `examples/Arduino/simple_echo`:

```sh
/tmp/libcxxcanard-linux-build/simple_echo --can vcan1.3 --target-node-id 2 --timeout-ms 5000
```

`service_echo` говорит с `examples/Arduino/service_echo`:

```sh
/tmp/libcxxcanard-linux-build/service_echo --can vcan1.3 --target-node-id 2 --timeout-ms 5000
```

`full_example` говорит с `examples/Arduino/full_example`:

```sh
/tmp/libcxxcanard-linux-build/full_example --can vcan1.3 --target-node-id 2 --timeout-ms 5000
```
