// This is an AUTO-GENERATED C++ traits header for libcxxcanard.
// Source file: /home/igor/Projects/libsws/cyphal_types/public_regulated_data_types/uavcan/file/409.Write.1.1.dsdl
#pragma once

#include <cyphal.h>
#include <uavcan/file/Write_1_1.h>

template <>
struct CyphalTypeTraits<uavcan_file_Write_Request_1_1> {
    using serializer_type = cyphal_serializer<uavcan_file_Write_Request_1_1>;
    using deserializer_type = cyphal_deserializer<uavcan_file_Write_Request_1_1>;

    static constexpr serializer_type serializer = uavcan_file_Write_Request_1_1_serialize_;
    static constexpr deserializer_type deserializer = uavcan_file_Write_Request_1_1_deserialize_;
    static constexpr size_t extent = uavcan_file_Write_Request_1_1_EXTENT_BYTES_;
    static constexpr size_t buffer_size = uavcan_file_Write_Request_1_1_SERIALIZATION_BUFFER_SIZE_BYTES_;
};

template <>
struct CyphalTypeTraits<uavcan_file_Write_Response_1_1> {
    using serializer_type = cyphal_serializer<uavcan_file_Write_Response_1_1>;
    using deserializer_type = cyphal_deserializer<uavcan_file_Write_Response_1_1>;

    static constexpr serializer_type serializer = uavcan_file_Write_Response_1_1_serialize_;
    static constexpr deserializer_type deserializer = uavcan_file_Write_Response_1_1_deserialize_;
    static constexpr size_t extent = uavcan_file_Write_Response_1_1_EXTENT_BYTES_;
    static constexpr size_t buffer_size = uavcan_file_Write_Response_1_1_SERIALIZATION_BUFFER_SIZE_BYTES_;
};
