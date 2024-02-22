#pragma once

#include <array>
#include <cstdint>

#include "cyphal/definitions.h"

extern const std::array<uint32_t, 65> CanardFDCANLengthToDLC;
extern size_t fdcan_dlc_to_len(uint32_t);
