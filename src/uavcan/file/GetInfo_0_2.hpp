// This is an AUTO-GENERATED C++ traits header for libcxxcanard.
// Source file: /home/igor/Projects/libsws/cyphal_types/public_regulated_data_types/uavcan/file/405.GetInfo.0.2.dsdl
#pragma once

#include <cyphal.h>
#include <uavcan/file/GetInfo_0_2.h>

template <>
struct CyphalTypeTraits<uavcan_file_GetInfo_Request_0_2> {
    using serializer_type = cyphal_serializer<uavcan_file_GetInfo_Request_0_2>;
    using deserializer_type = cyphal_deserializer<uavcan_file_GetInfo_Request_0_2>;

    static constexpr serializer_type serializer = uavcan_file_GetInfo_Request_0_2_serialize_;
    static constexpr deserializer_type deserializer = uavcan_file_GetInfo_Request_0_2_deserialize_;
    static constexpr size_t extent = uavcan_file_GetInfo_Request_0_2_EXTENT_BYTES_;
    static constexpr size_t buffer_size = uavcan_file_GetInfo_Request_0_2_SERIALIZATION_BUFFER_SIZE_BYTES_;
};

template <>
struct CyphalTypeTraits<uavcan_file_GetInfo_Response_0_2> {
    using serializer_type = cyphal_serializer<uavcan_file_GetInfo_Response_0_2>;
    using deserializer_type = cyphal_deserializer<uavcan_file_GetInfo_Response_0_2>;

    static constexpr serializer_type serializer = uavcan_file_GetInfo_Response_0_2_serialize_;
    static constexpr deserializer_type deserializer = uavcan_file_GetInfo_Response_0_2_deserialize_;
    static constexpr size_t extent = uavcan_file_GetInfo_Response_0_2_EXTENT_BYTES_;
    static constexpr size_t buffer_size = uavcan_file_GetInfo_Response_0_2_SERIALIZATION_BUFFER_SIZE_BYTES_;
};
