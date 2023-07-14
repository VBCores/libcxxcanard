#pragma once

#if defined(STM32G474xx) || defined(STM32_G)
#include "stm32g4xx_hal.h"
#include "utils.h"
#elif defined(STM32F446xx) || defined(STM32_F)
#include "stm32f4xx_hal.h"
#include "utils.h"
#else
#define LINUX_CAN
#define CRITICAL_SECTION(code) code
#include <unistd.h>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#endif

// timestamp conversion macros
#define SEC_TO_US(sec) ((sec)*1000000)
#define NS_TO_US(ns) ((ns) / 1000)

extern void Error_Handler();