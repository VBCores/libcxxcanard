// This is an AUTO-GENERATED C++ traits header for libcxxcanard.
// Source file: /home/igor/Projects/libsws/cyphal_types/public_regulated_data_types/uavcan/diagnostic/8184.Record.1.1.dsdl
#pragma once

#include <cyphal.h>
#include <uavcan/diagnostic/Record_1_1.h>

template <>
struct CyphalTypeTraits<uavcan_diagnostic_Record_1_1> {
    using serializer_type = cyphal_serializer<uavcan_diagnostic_Record_1_1>;
    using deserializer_type = cyphal_deserializer<uavcan_diagnostic_Record_1_1>;

    static constexpr serializer_type serializer = uavcan_diagnostic_Record_1_1_serialize_;
    static constexpr deserializer_type deserializer = uavcan_diagnostic_Record_1_1_deserialize_;
    static constexpr size_t extent = uavcan_diagnostic_Record_1_1_EXTENT_BYTES_;
    static constexpr size_t buffer_size = uavcan_diagnostic_Record_1_1_SERIALIZATION_BUFFER_SIZE_BYTES_;
};

