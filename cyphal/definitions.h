#pragma once

#include <functional>

#if defined(STM32G474xx) || defined(STM32_G)
#include "stm32g4xx_hal.h"
#include "stm32g4xx_hal_fdcan.h"
// TODO: rework this dependency
#if __has_include("voltbro/utils.h")
    #include "voltbro/utils.h"
#else
    #define CRITICAL_SECTION(code) code
#endif
#else
#define CRITICAL_SECTION(code) code
#include <unistd.h>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <utility>
#endif

// timestamp conversion macros
#define SEC_TO_US(sec) ((sec) * 1000000)
#define NS_TO_US(ns) ((ns) / 1000)

#ifdef __linux__
uint64_t _micros_64();
#endif

// NOLINTBEGIN(cppcoreguidelines-avoid-const-or-ref-data-members)
/**
 * Коллекция разных функций, требуемых для работы cyphal: микросекунды и обработчик ошибок.
 * Не очень типично для linux, но привычно на stm32 - поэтому используется везде ради кроссплатформенности.
*/
struct UtilityConfig {
    using micros_64_type = std::function<uint64_t()>;
    using error_handler_type = std::function<void()>;

    const micros_64_type micros_64;
    const error_handler_type error_handler;

    /**
     * @param micros Функция (функтор), возвращающая `uint64_t` микросекунды
     * @param handler Функция - "*что делать при ошибке*". На stm32 обычно просто `Error_Handler`, на linux - что угодно, можно просто `exit()`.
    */
    explicit UtilityConfig(micros_64_type&& micros, error_handler_type&& handler) noexcept
        : micros_64(std::forward<micros_64_type>(micros)),
          error_handler(std::forward<error_handler_type>(handler)){};
};
// NOLINTEND(cppcoreguidelines-avoid-const-or-ref-data-members)

#ifdef __linux__
extern const UtilityConfig DEFAULT_CONFIG;
#endif
