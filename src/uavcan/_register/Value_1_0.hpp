// This is an AUTO-GENERATED C++ traits header for libcxxcanard.
// Source file: /home/igor/Projects/libsws/cyphal_types/public_regulated_data_types/uavcan/register/Value.1.0.dsdl
#pragma once

#include <cyphal.h>
#include <uavcan/_register/Value_1_0.h>

template <>
struct CyphalTypeTraits<uavcan_register_Value_1_0> {
    using serializer_type = cyphal_serializer<uavcan_register_Value_1_0>;
    using deserializer_type = cyphal_deserializer<uavcan_register_Value_1_0>;

    static constexpr serializer_type serializer = uavcan_register_Value_1_0_serialize_;
    static constexpr deserializer_type deserializer = uavcan_register_Value_1_0_deserialize_;
    static constexpr size_t extent = uavcan_register_Value_1_0_EXTENT_BYTES_;
    static constexpr size_t buffer_size = uavcan_register_Value_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_;
};

