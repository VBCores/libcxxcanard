# Linux Examples

This folder is intentionally flat: CMakeLists plus a few `.cpp` peers. The
examples are meant to be copied into, or used as a reference for, a normal
SocketCAN project.

Expected project shape:

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

`CMakeLists.txt` can also be used from this repository checkout. It looks for
`libcxxcanard` automatically when run from `examples/Linux`; otherwise set
`LIBCXXCANARD_DIR`. Set `CYPHAL_TYPES_DIR` when your type repositories are not
next to `libcxxcanard`.

## Build

```sh
CYPHAL_TYPES_DIR=/home/igor/Projects/libsws/cyphal_types \
cmake -S examples/Linux -B /tmp/libcxxcanard-linux-build

cmake --build /tmp/libcxxcanard-linux-build
```

## Run

`simple_echo` talks to `examples/Arduino/simple_echo`:

```sh
/tmp/libcxxcanard-linux-build/simple_echo --can vcan1.3 --target-node-id 2 --timeout-ms 5000
```

`service_echo` talks to `examples/Arduino/service_echo`:

```sh
/tmp/libcxxcanard-linux-build/service_echo --can vcan1.3 --target-node-id 2 --timeout-ms 5000
```

`full_example` talks to `examples/Arduino/full_example`:

```sh
/tmp/libcxxcanard-linux-build/full_example --can vcan1.3 --target-node-id 2 --timeout-ms 5000
```
