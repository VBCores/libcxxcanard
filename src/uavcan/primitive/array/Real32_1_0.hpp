// This is an AUTO-GENERATED C++ traits header for libcxxcanard.
// Source file: /home/igor/Projects/libsws/cyphal_types/public_regulated_data_types/uavcan/primitive/array/Real32.1.0.dsdl
#pragma once

#include <cyphal.h>
#include <uavcan/primitive/array/Real32_1_0.h>

template <>
struct CyphalTypeTraits<uavcan_primitive_array_Real32_1_0> {
    using serializer_type = cyphal_serializer<uavcan_primitive_array_Real32_1_0>;
    using deserializer_type = cyphal_deserializer<uavcan_primitive_array_Real32_1_0>;

    static constexpr serializer_type serializer = uavcan_primitive_array_Real32_1_0_serialize_;
    static constexpr deserializer_type deserializer = uavcan_primitive_array_Real32_1_0_deserialize_;
    static constexpr size_t extent = uavcan_primitive_array_Real32_1_0_EXTENT_BYTES_;
    static constexpr size_t buffer_size = uavcan_primitive_array_Real32_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_;
};
