# Linux Examples

This folder contains small SocketCAN peers for the Arduino sketches:

- `simple_echo.cpp` talks to `examples/Arduino/simple_echo`.
- `service_echo.cpp` talks to `examples/Arduino/service_echo`.
- `full_example.cpp` talks to `examples/Arduino/full_example`.

The `.cpp` files use fixed
demo values: SocketCAN interface `vcan1.3`, local node-ID `42`, target node-ID
`2`, and a 5 second timeout.

## Project Shape

Use the examples as regular source files in a project like this:

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

Minimal `CMakeLists.txt` for one executable see in this directory.

Build and run:

```sh
cmake -S . -B build
cmake --build build
./build/simple_echo
```
