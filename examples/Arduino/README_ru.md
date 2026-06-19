# Arduino Examples

Эти скетчи рассчитаны на VBCore STM32G4 Arduino setup и используют
упакованную библиотеку из `src/`.

## Скетчи

- `simple_echo/simple_echo.ino`: минимальный callback-style message echo.
  Подписывается на `UInt32` на порту `5000` и публикует то же значение на `5001`.
- `service_echo/service_echo.ino`: минимальный callback-style service.
  Подписывается на service `101` как `CanardTransferKindRequest` и возвращает
  строку из request в response.
- `full_example/full_example.ino`: class-style subscriptions, периодическая
  telemetry, echo service, node info и registers.

## Сборка

После изменений в библиотеке обновите Arduino package:

```sh
make arduino-lib
```

Скомпилировать sketch можно через Arduino CLI или helper для STM32 Arduino:

```sh
arduino-cli compile -b STMicroelectronics:stm32:GenG4:pnum=GENERIC_G474RETX examples/Arduino/simple_echo
```

Linux peers в `../Linux` написаны так, чтобы говорить с этими скетчами по CAN.
