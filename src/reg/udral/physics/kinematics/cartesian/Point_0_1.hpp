// This is an AUTO-GENERATED C++ traits header for libcxxcanard.
// Source file: /home/igor/Projects/libsws/cyphal_types/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/Point.0.1.dsdl
#pragma once

#include <cyphal.h>
#include <reg/udral/physics/kinematics/cartesian/Point_0_1.h>

template <>
struct CyphalTypeTraits<reg_udral_physics_kinematics_cartesian_Point_0_1> {
    using serializer_type = cyphal_serializer<reg_udral_physics_kinematics_cartesian_Point_0_1>;
    using deserializer_type = cyphal_deserializer<reg_udral_physics_kinematics_cartesian_Point_0_1>;

    static constexpr serializer_type serializer = reg_udral_physics_kinematics_cartesian_Point_0_1_serialize_;
    static constexpr deserializer_type deserializer = reg_udral_physics_kinematics_cartesian_Point_0_1_deserialize_;
    static constexpr size_t extent = reg_udral_physics_kinematics_cartesian_Point_0_1_EXTENT_BYTES_;
    static constexpr size_t buffer_size = reg_udral_physics_kinematics_cartesian_Point_0_1_SERIALIZATION_BUFFER_SIZE_BYTES_;
};
