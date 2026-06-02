// This is an AUTO-GENERATED C++ traits header for libcxxcanard.
// Source file: /home/igor/Projects/libsws/cyphal_types/public_regulated_data_types/uavcan/si/sample/magnetic_field_strength/Scalar.1.1.dsdl
#pragma once

#include <cyphal.h>
#include <uavcan/si/sample/magnetic_field_strength/Scalar_1_1.h>

template <>
struct CyphalTypeTraits<uavcan_si_sample_magnetic_field_strength_Scalar_1_1> {
    using serializer_type = cyphal_serializer<uavcan_si_sample_magnetic_field_strength_Scalar_1_1>;
    using deserializer_type = cyphal_deserializer<uavcan_si_sample_magnetic_field_strength_Scalar_1_1>;

    static constexpr serializer_type serializer = uavcan_si_sample_magnetic_field_strength_Scalar_1_1_serialize_;
    static constexpr deserializer_type deserializer = uavcan_si_sample_magnetic_field_strength_Scalar_1_1_deserialize_;
    static constexpr size_t extent = uavcan_si_sample_magnetic_field_strength_Scalar_1_1_EXTENT_BYTES_;
    static constexpr size_t buffer_size = uavcan_si_sample_magnetic_field_strength_Scalar_1_1_SERIALIZATION_BUFFER_SIZE_BYTES_;
};
