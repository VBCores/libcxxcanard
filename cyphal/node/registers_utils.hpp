#pragma once

#include <cyphal/node/registers_handler.hpp>

static constexpr uint8_t REGISTER_EMPTY_TAG = 0U;
static constexpr uint8_t REGISTER_BIT_TAG = 3U;
static constexpr uint8_t REGISTER_REAL32_TAG = 13U;
static constexpr uint8_t REGISTER_NATURAL32_TAG = 9U;

inline bool parse_register_bit(const uavcan_register_Value_1_0& value, bool& parsed) {
    if (value._tag_ != REGISTER_BIT_TAG || value.bit.value.count == 0) {
        return false;
    }
    parsed = value.bit.value.bitpacked[0] == 1;
    return true;
}

inline bool parse_register_real32(const uavcan_register_Value_1_0& value, float& parsed) {
    if (value._tag_ != REGISTER_REAL32_TAG || value.real32.value.count == 0) {
        return false;
    }
    parsed = value.real32.value.elements[0];
    return true;
}

inline void fill_register_bit(uavcan_register_Value_1_0& out, bool value) {
    out._tag_ = REGISTER_BIT_TAG;
    out.bit.value.bitpacked[0] = value;
    out.bit.value.count = 1;
}

inline void fill_register_real32(uavcan_register_Value_1_0& out, float value) {
    out._tag_ = REGISTER_REAL32_TAG;
    out.real32.value.elements[0] = value;
    out.real32.value.count = 1;
}

inline void fill_register_natural32(uavcan_register_Value_1_0& out, uint32_t value) {
    out._tag_ = REGISTER_NATURAL32_TAG;
    out.natural32.value.elements[0] = value;
    out.natural32.value.count = 1;
}
