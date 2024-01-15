#pragma once

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

extern void error_handler();

#ifdef __linux__
uint64_t micros_64();
#else
extern uint64_t micros_64();
#endif
