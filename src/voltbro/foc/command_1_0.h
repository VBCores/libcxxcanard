// This is an AUTO-GENERATED Cyphal DSDL data type implementation. Curious? See https://opencyphal.org.
// You shouldn't attempt to edit this file.
//
// Checking this file under version control is not recommended unless it is used as part of a high-SIL
// safety-critical codebase. The typical usage scenario is to generate it as part of the build process.
//
// To avoid conflicts with definitions given in the source DSDL file, all entities created by the code generator
// are named with an underscore at the end, like foo_bar_().
//
// Generator:     nunavut-2.3.1 (serialization was enabled)
// Source file:   /home/pi/ws/types/voltbro/foc/command.1.0.dsdl
// Generated at:  2025-12-19 12:32:08.195171 UTC
// Is deprecated: no
// Fixed port-ID: None
// Full name:     voltbro.foc.command
// Version:       1.0
//
// Platform
//     python_implementation:  CPython
//     python_version:  3.12.3
//     python_release_level:  final
//     python_build:  ('main', 'Nov  6 2025 13:44:16')
//     python_compiler:  GCC 13.3.0
//     python_revision:
//     python_xoptions:  {}
//     runtime_platform:  Linux-6.8.0-1031-raspi-aarch64-with-glibc2.39
//
// Language Options
//     target_endianness:  little
//     omit_float_serialization_support:  False
//     enable_serialization_asserts:  False
//     enable_override_variable_array_capacity:  False
//     cast_format:  (({type}) {value})

#ifndef VOLTBRO_FOC_COMMAND_1_0_INCLUDED_
#define VOLTBRO_FOC_COMMAND_1_0_INCLUDED_

#include <nunavut/support/serialization.h>
#include <stdlib.h>
#include <uavcan/primitive/scalar/Real32_1_0.h>
#include <uavcan/si/unit/angle/Scalar_1_0.h>
#include <uavcan/si/unit/angular_velocity/Scalar_1_0.h>
#include <uavcan/si/unit/torque/Scalar_1_0.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 434322821,
              "/home/pi/ws/types/voltbro/foc/command.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/home/pi/ws/types/voltbro/foc/command.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/home/pi/ws/types/voltbro/foc/command.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/home/pi/ws/types/voltbro/foc/command.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/home/pi/ws/types/voltbro/foc/command.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

/// This type does not have a fixed port-ID. See https://forum.opencyphal.org/t/choosing-message-and-service-ids/889
#define voltbro_foc_command_1_0_HAS_FIXED_PORT_ID_ false

// +-------------------------------------------------------------------------------------------------------------------+
// | voltbro.foc.command.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define voltbro_foc_command_1_0_FULL_NAME_             "voltbro.foc.command"
#define voltbro_foc_command_1_0_FULL_NAME_AND_VERSION_ "voltbro.foc.command.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define voltbro_foc_command_1_0_EXTENT_BYTES_                    28UL
#define voltbro_foc_command_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 28UL
static_assert(voltbro_foc_command_1_0_EXTENT_BYTES_ >= voltbro_foc_command_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

typedef struct
{
    /// uavcan.si.unit.torque.Scalar.1.0 torque
    uavcan_si_unit_torque_Scalar_1_0 _torque;

    /// uavcan.si.unit.angle.Scalar.1.0 angle
    uavcan_si_unit_angle_Scalar_1_0 angle;

    /// uavcan.si.unit.angular_velocity.Scalar.1.0 velocity
    uavcan_si_unit_angular_velocity_Scalar_1_0 velocity;

    /// uavcan.primitive.scalar.Real32.1.0 angle_kp
    uavcan_primitive_scalar_Real32_1_0 angle_kp;

    /// uavcan.primitive.scalar.Real32.1.0 velocity_kp
    uavcan_primitive_scalar_Real32_1_0 velocity_kp;

    /// uavcan.primitive.scalar.Real32.1.0 I_kp
    uavcan_primitive_scalar_Real32_1_0 I_kp;

    /// uavcan.primitive.scalar.Real32.1.0 I_ki
    uavcan_primitive_scalar_Real32_1_0 I_ki;
} voltbro_foc_command_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see voltbro_foc_command_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t voltbro_foc_command_1_0_serialize_(
    const voltbro_foc_command_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 224UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // uavcan.si.unit.torque.Scalar.1.0 torque
        size_t _size_bytes0_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err0_ = uavcan_si_unit_torque_Scalar_1_0_serialize_(
            &obj->_torque, &buffer[offset_bits / 8U], &_size_bytes0_);
        if (_err0_ < 0)
        {
            return _err0_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes0_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad0_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err1_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad0_);  // Optimize?
        if (_err1_ < 0)
        {
            return _err1_;
        }
        offset_bits += _pad0_;
    }
    {   // uavcan.si.unit.angle.Scalar.1.0 angle
        size_t _size_bytes1_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err2_ = uavcan_si_unit_angle_Scalar_1_0_serialize_(
            &obj->angle, &buffer[offset_bits / 8U], &_size_bytes1_);
        if (_err2_ < 0)
        {
            return _err2_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes1_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad1_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err3_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad1_);  // Optimize?
        if (_err3_ < 0)
        {
            return _err3_;
        }
        offset_bits += _pad1_;
    }
    {   // uavcan.si.unit.angular_velocity.Scalar.1.0 velocity
        size_t _size_bytes2_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err4_ = uavcan_si_unit_angular_velocity_Scalar_1_0_serialize_(
            &obj->velocity, &buffer[offset_bits / 8U], &_size_bytes2_);
        if (_err4_ < 0)
        {
            return _err4_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes2_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad2_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err5_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad2_);  // Optimize?
        if (_err5_ < 0)
        {
            return _err5_;
        }
        offset_bits += _pad2_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 angle_kp
        size_t _size_bytes3_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err6_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->angle_kp, &buffer[offset_bits / 8U], &_size_bytes3_);
        if (_err6_ < 0)
        {
            return _err6_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes3_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad3_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err7_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad3_);  // Optimize?
        if (_err7_ < 0)
        {
            return _err7_;
        }
        offset_bits += _pad3_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 velocity_kp
        size_t _size_bytes4_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err8_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->velocity_kp, &buffer[offset_bits / 8U], &_size_bytes4_);
        if (_err8_ < 0)
        {
            return _err8_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes4_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad4_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err9_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad4_);  // Optimize?
        if (_err9_ < 0)
        {
            return _err9_;
        }
        offset_bits += _pad4_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 I_kp
        size_t _size_bytes5_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err10_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->I_kp, &buffer[offset_bits / 8U], &_size_bytes5_);
        if (_err10_ < 0)
        {
            return _err10_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes5_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad5_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err11_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad5_);  // Optimize?
        if (_err11_ < 0)
        {
            return _err11_;
        }
        offset_bits += _pad5_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 I_ki
        size_t _size_bytes6_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err12_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->I_ki, &buffer[offset_bits / 8U], &_size_bytes6_);
        if (_err12_ < 0)
        {
            return _err12_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes6_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad6_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err13_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad6_);  // Optimize?
        if (_err13_ < 0)
        {
            return _err13_;
        }
        offset_bits += _pad6_;
    }
    // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
    *inout_buffer_size_bytes = (size_t) (offset_bits / 8U);
    return NUNAVUT_SUCCESS;
}

/// Deserialize an instance from the provided buffer.
/// The lifetime of the resulting object is independent of the original buffer.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original buffer where possible.
///
/// @param obj      The object to update from the provided serialized representation.
///
/// @param buffer   The source buffer containing the serialized representation. There are no alignment requirements.
///                 If the buffer is shorter or longer than expected, it will be implicitly zero-extended or truncated,
///                 respectively; see Specification for "implicit zero extension" and "implicit truncation" rules.
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the supplied serialized
///                                 representation, in bytes. Upon return this value will be updated with the
///                                 size of the consumed fragment of the serialized representation (in bytes),
///                                 which may be smaller due to the implicit truncation rule, but it is guaranteed
///                                 to never exceed the original buffer size even if the implicit zero extension rule
///                                 was activated. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t voltbro_foc_command_1_0_deserialize_(
    voltbro_foc_command_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
{
    if ((out_obj == NULL) || (inout_buffer_size_bytes == NULL) || ((buffer == NULL) && (0 != *inout_buffer_size_bytes)))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    if (buffer == NULL)
    {
        buffer = (const uint8_t*)"";
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    const size_t capacity_bits = capacity_bytes * (size_t) 8U;
    size_t offset_bits = 0U;
    // uavcan.si.unit.torque.Scalar.1.0 torque
    {
        size_t _size_bytes7_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err14_ = uavcan_si_unit_torque_Scalar_1_0_deserialize_(
            &out_obj->_torque, &buffer[offset_bits / 8U], &_size_bytes7_);
        if (_err14_ < 0)
        {
            return _err14_;
        }
        offset_bits += _size_bytes7_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.si.unit.angle.Scalar.1.0 angle
    {
        size_t _size_bytes8_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err15_ = uavcan_si_unit_angle_Scalar_1_0_deserialize_(
            &out_obj->angle, &buffer[offset_bits / 8U], &_size_bytes8_);
        if (_err15_ < 0)
        {
            return _err15_;
        }
        offset_bits += _size_bytes8_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.si.unit.angular_velocity.Scalar.1.0 velocity
    {
        size_t _size_bytes9_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err16_ = uavcan_si_unit_angular_velocity_Scalar_1_0_deserialize_(
            &out_obj->velocity, &buffer[offset_bits / 8U], &_size_bytes9_);
        if (_err16_ < 0)
        {
            return _err16_;
        }
        offset_bits += _size_bytes9_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 angle_kp
    {
        size_t _size_bytes10_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err17_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->angle_kp, &buffer[offset_bits / 8U], &_size_bytes10_);
        if (_err17_ < 0)
        {
            return _err17_;
        }
        offset_bits += _size_bytes10_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 velocity_kp
    {
        size_t _size_bytes11_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err18_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->velocity_kp, &buffer[offset_bits / 8U], &_size_bytes11_);
        if (_err18_ < 0)
        {
            return _err18_;
        }
        offset_bits += _size_bytes11_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 I_kp
    {
        size_t _size_bytes12_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err19_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->I_kp, &buffer[offset_bits / 8U], &_size_bytes12_);
        if (_err19_ < 0)
        {
            return _err19_;
        }
        offset_bits += _size_bytes12_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 I_ki
    {
        size_t _size_bytes13_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err20_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->I_ki, &buffer[offset_bits / 8U], &_size_bytes13_);
        if (_err20_ < 0)
        {
            return _err20_;
        }
        offset_bits += _size_bytes13_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void voltbro_foc_command_1_0_initialize_(voltbro_foc_command_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = voltbro_foc_command_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

#ifdef __cplusplus
}
#endif
#endif // VOLTBRO_FOC_COMMAND_1_0_INCLUDED_
