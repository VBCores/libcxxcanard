// This is an AUTO-GENERATED C++ traits header for libcxxcanard.
// Source file: /home/igor/Projects/libsws/cyphal_types/voltbro_types/voltbro/hmi/led_service.1.0.dsdl
#pragma once

#include <cyphal.h>
#include <voltbro/hmi/led_service_1_0.h>

template <>
struct CyphalTypeTraits<voltbro_hmi_led_service_Request_1_0> {
    using serializer_type = cyphal_serializer<voltbro_hmi_led_service_Request_1_0>;
    using deserializer_type = cyphal_deserializer<voltbro_hmi_led_service_Request_1_0>;

    static constexpr serializer_type serializer = voltbro_hmi_led_service_Request_1_0_serialize_;
    static constexpr deserializer_type deserializer = voltbro_hmi_led_service_Request_1_0_deserialize_;
    static constexpr size_t extent = voltbro_hmi_led_service_Request_1_0_EXTENT_BYTES_;
    static constexpr size_t buffer_size = voltbro_hmi_led_service_Request_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_;
};

template <>
struct CyphalTypeTraits<voltbro_hmi_led_service_Response_1_0> {
    using serializer_type = cyphal_serializer<voltbro_hmi_led_service_Response_1_0>;
    using deserializer_type = cyphal_deserializer<voltbro_hmi_led_service_Response_1_0>;

    static constexpr serializer_type serializer = voltbro_hmi_led_service_Response_1_0_serialize_;
    static constexpr deserializer_type deserializer = voltbro_hmi_led_service_Response_1_0_deserialize_;
    static constexpr size_t extent = voltbro_hmi_led_service_Response_1_0_EXTENT_BYTES_;
    static constexpr size_t buffer_size = voltbro_hmi_led_service_Response_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_;
};
