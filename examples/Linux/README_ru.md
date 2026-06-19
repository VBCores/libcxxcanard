# Linux Examples

В этой папке лежат маленькие SocketCAN примеры, "парные" для Arduino sketches:

- `simple_echo.cpp` говорит с `examples/Arduino/simple_echo`.
- `service_echo.cpp` говорит с `examples/Arduino/service_echo`.
- `full_example.cpp` говорит с `examples/Arduino/full_example`.

В `.cpp` файлах используются фиксированные demo values: SocketCAN interface `vcan1.3`, local
node-ID `42`, target node-ID `2` и timeout 5 секунд.

## Структура проекта

Используйте примеры как обычные source files в проекте такой формы:

```txt
project/
    CMakeLists.txt
    simple_echo.cpp
    libcxxcanard/
    cyphal_types/
        cyphal_types.cmake
        public_regulated_data_types/
        voltbro_types/
```

Минимальный `CMakeLists.txt` см. в этой папке

Сборка и запуск:

```sh
cmake -S . -B build
cmake --build build
./build/simple_echo
```
