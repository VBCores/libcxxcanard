# Arduino Examples

These sketches target the VBCore STM32G4 Arduino setup and use the packed
library from `src/`.

## Sketches

- `simple_echo/simple_echo.ino`: minimal callback-style message echo. It
  subscribes to `UInt32` on port `5000` and publishes the same value on `5001`.
- `service_echo/service_echo.ino`: minimal callback-style service. It
  subscribes to service `101` as `CanardTransferKindRequest` and echoes the
  request string in the response.
- `full_example/full_example.ino`: class-style subscriptions, periodic
  telemetry, echo service, node info, and registers.

## Build

Compile a sketch with Arduino CLI or the helper used for STM32 Arduino builds:

```sh
arduino-cli compile -b STMicroelectronics:stm32:GenG4:pnum=GENERIC_G474RETX examples/Arduino/simple_echo
```

The Linux peers in `../Linux` are written to talk to these sketches over CAN.
