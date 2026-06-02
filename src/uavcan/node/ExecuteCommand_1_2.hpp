// This is an AUTO-GENERATED C++ traits header for libcxxcanard.
// Source file: /home/igor/Projects/libsws/cyphal_types/public_regulated_data_types/uavcan/node/435.ExecuteCommand.1.2.dsdl
#pragma once

#include <cyphal.h>
#include <uavcan/node/ExecuteCommand_1_2.h>

template <>
struct CyphalTypeTraits<uavcan_node_ExecuteCommand_Request_1_2> {
    using serializer_type = cyphal_serializer<uavcan_node_ExecuteCommand_Request_1_2>;
    using deserializer_type = cyphal_deserializer<uavcan_node_ExecuteCommand_Request_1_2>;

    static constexpr serializer_type serializer = uavcan_node_ExecuteCommand_Request_1_2_serialize_;
    static constexpr deserializer_type deserializer = uavcan_node_ExecuteCommand_Request_1_2_deserialize_;
    static constexpr size_t extent = uavcan_node_ExecuteCommand_Request_1_2_EXTENT_BYTES_;
    static constexpr size_t buffer_size = uavcan_node_ExecuteCommand_Request_1_2_SERIALIZATION_BUFFER_SIZE_BYTES_;
};

template <>
struct CyphalTypeTraits<uavcan_node_ExecuteCommand_Response_1_2> {
    using serializer_type = cyphal_serializer<uavcan_node_ExecuteCommand_Response_1_2>;
    using deserializer_type = cyphal_deserializer<uavcan_node_ExecuteCommand_Response_1_2>;

    static constexpr serializer_type serializer = uavcan_node_ExecuteCommand_Response_1_2_serialize_;
    static constexpr deserializer_type deserializer = uavcan_node_ExecuteCommand_Response_1_2_deserialize_;
    static constexpr size_t extent = uavcan_node_ExecuteCommand_Response_1_2_EXTENT_BYTES_;
    static constexpr size_t buffer_size = uavcan_node_ExecuteCommand_Response_1_2_SERIALIZATION_BUFFER_SIZE_BYTES_;
};
