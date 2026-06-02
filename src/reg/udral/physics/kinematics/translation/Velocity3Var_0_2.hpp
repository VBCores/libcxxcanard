// This is an AUTO-GENERATED C++ traits header for libcxxcanard.
// Source file: /home/igor/Projects/libsws/cyphal_types/public_regulated_data_types/reg/udral/physics/kinematics/translation/Velocity3Var.0.2.dsdl
#pragma once

#include <cyphal.h>
#include <reg/udral/physics/kinematics/translation/Velocity3Var_0_2.h>

template <>
struct CyphalTypeTraits<reg_udral_physics_kinematics_translation_Velocity3Var_0_2> {
    using serializer_type = cyphal_serializer<reg_udral_physics_kinematics_translation_Velocity3Var_0_2>;
    using deserializer_type = cyphal_deserializer<reg_udral_physics_kinematics_translation_Velocity3Var_0_2>;

    static constexpr serializer_type serializer = reg_udral_physics_kinematics_translation_Velocity3Var_0_2_serialize_;
    static constexpr deserializer_type deserializer = reg_udral_physics_kinematics_translation_Velocity3Var_0_2_deserialize_;
    static constexpr size_t extent = reg_udral_physics_kinematics_translation_Velocity3Var_0_2_EXTENT_BYTES_;
    static constexpr size_t buffer_size = reg_udral_physics_kinematics_translation_Velocity3Var_0_2_SERIALIZATION_BUFFER_SIZE_BYTES_;
};
