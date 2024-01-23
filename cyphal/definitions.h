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
#include <unistd.h>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <stdint.h>
#endif

// timestamp conversion macros
#define SEC_TO_US(sec) ((sec) * 1000000)
#define NS_TO_US(ns) ((ns) / 1000)

#ifdef __linux__
uint64_t _micros_64();
#endif

struct UtilityConfig {
    const std::function<uint64_t()> micros_64;
    const std::function<void()> error_handler;

    explicit UtilityConfig(std::function<uint64_t()>&& micros, std::function<void()>&& handler):
        micros_64(micros),
        error_handler(handler)
    {};
};

#ifdef __linux__
extern UtilityConfig DEFAULT_CONFIG;
#endif
