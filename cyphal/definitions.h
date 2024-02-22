#pragma once

#include <functional>

#if defined(STM32G474xx) || defined(STM32_G)
#include "stm32g4xx_hal.h"
// TODO: rework this dependency
#if __has_include("utils.h")
#include "utils.h"
#else
#define CRITICAL_SECTION(code) code
#endif
#else
#define CRITICAL_SECTION(code) code
#include <cstdint>
#include <unistd.h>
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
struct UtilityConfig {
    using micros_64_type = std::function<uint64_t()>;
    using error_handler_type = std::function<void()>;

    const micros_64_type micros_64;
    const error_handler_type error_handler;

    explicit UtilityConfig(
        micros_64_type&& micros,
        error_handler_type&& handler
    ) noexcept
        : micros_64(std::forward<micros_64_type>(micros)),
          error_handler(std::forward<error_handler_type>(handler)){};
};
// NOLINTEND(cppcoreguidelines-avoid-const-or-ref-data-members)

#ifdef __linux__
extern UtilityConfig DEFAULT_CONFIG;
#endif
