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
// Source file:   /home/pi/ws/types/voltbro/config/six_step/values.1.0.dsdl
// Generated at:  2025-12-19 12:32:08.167536 UTC
// Is deprecated: no
// Fixed port-ID: None
// Full name:     voltbro.config.six_step.values
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

#ifndef VOLTBRO_CONFIG_SIX_STEP_VALUES_1_0_INCLUDED_
#define VOLTBRO_CONFIG_SIX_STEP_VALUES_1_0_INCLUDED_

#include <nunavut/support/serialization.h>
#include <stdlib.h>
#include <uavcan/primitive/scalar/Integer32_1_0.h>
#include <uavcan/primitive/scalar/Integer8_1_0.h>
#include <uavcan/primitive/scalar/Real32_1_0.h>
#include <voltbro/config/six_step/pid_config_1_0.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 434322821,
              "/home/pi/ws/types/voltbro/config/six_step/values.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/home/pi/ws/types/voltbro/config/six_step/values.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/home/pi/ws/types/voltbro/config/six_step/values.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/home/pi/ws/types/voltbro/config/six_step/values.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/home/pi/ws/types/voltbro/config/six_step/values.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

/// This type does not have a fixed port-ID. See https://forum.opencyphal.org/t/choosing-message-and-service-ids/889
#define voltbro_config_six_step_values_1_0_HAS_FIXED_PORT_ID_ false

// +-------------------------------------------------------------------------------------------------------------------+
// | voltbro.config.six_step.values.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define voltbro_config_six_step_values_1_0_FULL_NAME_             "voltbro.config.six_step.values"
#define voltbro_config_six_step_values_1_0_FULL_NAME_AND_VERSION_ "voltbro.config.six_step.values.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define voltbro_config_six_step_values_1_0_EXTENT_BYTES_                    146UL
#define voltbro_config_six_step_values_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 146UL
static_assert(voltbro_config_six_step_values_1_0_EXTENT_BYTES_ >= voltbro_config_six_step_values_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

typedef struct
{
    /// uavcan.primitive.scalar.Integer8.1.0 predict_change
    uavcan_primitive_scalar_Integer8_1_0 predict_change;

    /// uavcan.primitive.scalar.Integer8.1.0 detect_stall
    uavcan_primitive_scalar_Integer8_1_0 detect_stall;

    /// uavcan.primitive.scalar.Real32.1.0 encoder_filtering
    uavcan_primitive_scalar_Real32_1_0 encoder_filtering;

    /// uavcan.primitive.scalar.Real32.1.0 speed_filtering
    uavcan_primitive_scalar_Real32_1_0 speed_filtering;

    /// uavcan.primitive.scalar.Real32.1.0 sampling_interval
    uavcan_primitive_scalar_Real32_1_0 sampling_interval;

    /// uavcan.primitive.scalar.Real32.1.0 stall_timeout
    uavcan_primitive_scalar_Real32_1_0 stall_timeout;

    /// uavcan.primitive.scalar.Real32.1.0 stall_tolerance
    uavcan_primitive_scalar_Real32_1_0 stall_tolerance;

    /// uavcan.primitive.scalar.Real32.1.0 current_limit
    uavcan_primitive_scalar_Real32_1_0 current_limit;

    /// uavcan.primitive.scalar.Real32.1.0 speed_mult
    uavcan_primitive_scalar_Real32_1_0 speed_mult;

    /// uavcan.primitive.scalar.Real32.1.0 I_mult
    uavcan_primitive_scalar_Real32_1_0 I_mult;

    /// uavcan.primitive.scalar.Real32.1.0 PWM_mult
    uavcan_primitive_scalar_Real32_1_0 PWM_mult;

    /// uavcan.primitive.scalar.Integer32.1.0 max_PWM_per_s
    uavcan_primitive_scalar_Integer32_1_0 max_PWM_per_s;

    /// uavcan.primitive.scalar.Real32.1.0 speed_const
    uavcan_primitive_scalar_Real32_1_0 speed_const;

    /// uavcan.primitive.scalar.Real32.1.0 torque_const
    uavcan_primitive_scalar_Real32_1_0 _torque_const;

    /// uavcan.primitive.scalar.Real32.1.0 max_current
    uavcan_primitive_scalar_Real32_1_0 max_current;

    /// uavcan.primitive.scalar.Real32.1.0 stall_current
    uavcan_primitive_scalar_Real32_1_0 stall_current;

    /// voltbro.config.six_step.pid_config.1.0 velocity_pid
    voltbro_config_six_step_pid_config_1_0 velocity_pid;

    /// voltbro.config.six_step.pid_config.1.0 current_pid
    voltbro_config_six_step_pid_config_1_0 current_pid;
} voltbro_config_six_step_values_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see voltbro_config_six_step_values_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t voltbro_config_six_step_values_1_0_serialize_(
    const voltbro_config_six_step_values_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 1168UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // uavcan.primitive.scalar.Integer8.1.0 predict_change
        size_t _size_bytes0_ = 1UL;  // Nested object (max) size, in bytes.
        int8_t _err0_ = uavcan_primitive_scalar_Integer8_1_0_serialize_(
            &obj->predict_change, &buffer[offset_bits / 8U], &_size_bytes0_);
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
    {   // uavcan.primitive.scalar.Integer8.1.0 detect_stall
        size_t _size_bytes1_ = 1UL;  // Nested object (max) size, in bytes.
        int8_t _err2_ = uavcan_primitive_scalar_Integer8_1_0_serialize_(
            &obj->detect_stall, &buffer[offset_bits / 8U], &_size_bytes1_);
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
    {   // uavcan.primitive.scalar.Real32.1.0 encoder_filtering
        size_t _size_bytes2_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err4_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->encoder_filtering, &buffer[offset_bits / 8U], &_size_bytes2_);
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
    {   // uavcan.primitive.scalar.Real32.1.0 speed_filtering
        size_t _size_bytes3_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err6_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->speed_filtering, &buffer[offset_bits / 8U], &_size_bytes3_);
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
    {   // uavcan.primitive.scalar.Real32.1.0 sampling_interval
        size_t _size_bytes4_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err8_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->sampling_interval, &buffer[offset_bits / 8U], &_size_bytes4_);
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
    {   // uavcan.primitive.scalar.Real32.1.0 stall_timeout
        size_t _size_bytes5_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err10_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->stall_timeout, &buffer[offset_bits / 8U], &_size_bytes5_);
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
    {   // uavcan.primitive.scalar.Real32.1.0 stall_tolerance
        size_t _size_bytes6_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err12_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->stall_tolerance, &buffer[offset_bits / 8U], &_size_bytes6_);
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
    {   // uavcan.primitive.scalar.Real32.1.0 current_limit
        size_t _size_bytes7_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err14_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->current_limit, &buffer[offset_bits / 8U], &_size_bytes7_);
        if (_err14_ < 0)
        {
            return _err14_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes7_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad7_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err15_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad7_);  // Optimize?
        if (_err15_ < 0)
        {
            return _err15_;
        }
        offset_bits += _pad7_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 speed_mult
        size_t _size_bytes8_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err16_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->speed_mult, &buffer[offset_bits / 8U], &_size_bytes8_);
        if (_err16_ < 0)
        {
            return _err16_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes8_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad8_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err17_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad8_);  // Optimize?
        if (_err17_ < 0)
        {
            return _err17_;
        }
        offset_bits += _pad8_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 I_mult
        size_t _size_bytes9_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err18_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->I_mult, &buffer[offset_bits / 8U], &_size_bytes9_);
        if (_err18_ < 0)
        {
            return _err18_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes9_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad9_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err19_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad9_);  // Optimize?
        if (_err19_ < 0)
        {
            return _err19_;
        }
        offset_bits += _pad9_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 PWM_mult
        size_t _size_bytes10_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err20_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->PWM_mult, &buffer[offset_bits / 8U], &_size_bytes10_);
        if (_err20_ < 0)
        {
            return _err20_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes10_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad10_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err21_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad10_);  // Optimize?
        if (_err21_ < 0)
        {
            return _err21_;
        }
        offset_bits += _pad10_;
    }
    {   // uavcan.primitive.scalar.Integer32.1.0 max_PWM_per_s
        size_t _size_bytes11_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err22_ = uavcan_primitive_scalar_Integer32_1_0_serialize_(
            &obj->max_PWM_per_s, &buffer[offset_bits / 8U], &_size_bytes11_);
        if (_err22_ < 0)
        {
            return _err22_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes11_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad11_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err23_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad11_);  // Optimize?
        if (_err23_ < 0)
        {
            return _err23_;
        }
        offset_bits += _pad11_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 speed_const
        size_t _size_bytes12_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err24_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->speed_const, &buffer[offset_bits / 8U], &_size_bytes12_);
        if (_err24_ < 0)
        {
            return _err24_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes12_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad12_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err25_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad12_);  // Optimize?
        if (_err25_ < 0)
        {
            return _err25_;
        }
        offset_bits += _pad12_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 torque_const
        size_t _size_bytes13_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err26_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->_torque_const, &buffer[offset_bits / 8U], &_size_bytes13_);
        if (_err26_ < 0)
        {
            return _err26_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes13_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad13_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err27_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad13_);  // Optimize?
        if (_err27_ < 0)
        {
            return _err27_;
        }
        offset_bits += _pad13_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 max_current
        size_t _size_bytes14_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err28_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->max_current, &buffer[offset_bits / 8U], &_size_bytes14_);
        if (_err28_ < 0)
        {
            return _err28_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes14_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad14_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err29_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad14_);  // Optimize?
        if (_err29_ < 0)
        {
            return _err29_;
        }
        offset_bits += _pad14_;
    }
    {   // uavcan.primitive.scalar.Real32.1.0 stall_current
        size_t _size_bytes15_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err30_ = uavcan_primitive_scalar_Real32_1_0_serialize_(
            &obj->stall_current, &buffer[offset_bits / 8U], &_size_bytes15_);
        if (_err30_ < 0)
        {
            return _err30_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes15_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad15_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err31_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad15_);  // Optimize?
        if (_err31_ < 0)
        {
            return _err31_;
        }
        offset_bits += _pad15_;
    }
    {   // voltbro.config.six_step.pid_config.1.0 velocity_pid
        size_t _size_bytes16_ = 40UL;  // Nested object (max) size, in bytes.
        // Constant delimiter header can be written ahead of the nested object.
        (void) memmove(&buffer[offset_bits / 8U], &_size_bytes16_, 4U);
        offset_bits += 32U;
        int8_t _err32_ = voltbro_config_six_step_pid_config_1_0_serialize_(
            &obj->velocity_pid, &buffer[offset_bits / 8U], &_size_bytes16_);
        if (_err32_ < 0)
        {
            return _err32_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes16_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad16_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err33_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad16_);  // Optimize?
        if (_err33_ < 0)
        {
            return _err33_;
        }
        offset_bits += _pad16_;
    }
    {   // voltbro.config.six_step.pid_config.1.0 current_pid
        size_t _size_bytes17_ = 40UL;  // Nested object (max) size, in bytes.
        // Constant delimiter header can be written ahead of the nested object.
        (void) memmove(&buffer[offset_bits / 8U], &_size_bytes17_, 4U);
        offset_bits += 32U;
        int8_t _err34_ = voltbro_config_six_step_pid_config_1_0_serialize_(
            &obj->current_pid, &buffer[offset_bits / 8U], &_size_bytes17_);
        if (_err34_ < 0)
        {
            return _err34_;
        }
        // It is assumed that we know the exact type of the serialized entity, hence we expect the size to match.
        offset_bits += _size_bytes17_ * 8U;  // Advance by the size of the nested object.
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad17_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err35_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad17_);  // Optimize?
        if (_err35_ < 0)
        {
            return _err35_;
        }
        offset_bits += _pad17_;
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
static inline int8_t voltbro_config_six_step_values_1_0_deserialize_(
    voltbro_config_six_step_values_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // uavcan.primitive.scalar.Integer8.1.0 predict_change
    {
        size_t _size_bytes18_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err36_ = uavcan_primitive_scalar_Integer8_1_0_deserialize_(
            &out_obj->predict_change, &buffer[offset_bits / 8U], &_size_bytes18_);
        if (_err36_ < 0)
        {
            return _err36_;
        }
        offset_bits += _size_bytes18_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Integer8.1.0 detect_stall
    {
        size_t _size_bytes19_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err37_ = uavcan_primitive_scalar_Integer8_1_0_deserialize_(
            &out_obj->detect_stall, &buffer[offset_bits / 8U], &_size_bytes19_);
        if (_err37_ < 0)
        {
            return _err37_;
        }
        offset_bits += _size_bytes19_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 encoder_filtering
    {
        size_t _size_bytes20_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err38_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->encoder_filtering, &buffer[offset_bits / 8U], &_size_bytes20_);
        if (_err38_ < 0)
        {
            return _err38_;
        }
        offset_bits += _size_bytes20_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 speed_filtering
    {
        size_t _size_bytes21_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err39_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->speed_filtering, &buffer[offset_bits / 8U], &_size_bytes21_);
        if (_err39_ < 0)
        {
            return _err39_;
        }
        offset_bits += _size_bytes21_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 sampling_interval
    {
        size_t _size_bytes22_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err40_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->sampling_interval, &buffer[offset_bits / 8U], &_size_bytes22_);
        if (_err40_ < 0)
        {
            return _err40_;
        }
        offset_bits += _size_bytes22_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 stall_timeout
    {
        size_t _size_bytes23_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err41_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->stall_timeout, &buffer[offset_bits / 8U], &_size_bytes23_);
        if (_err41_ < 0)
        {
            return _err41_;
        }
        offset_bits += _size_bytes23_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 stall_tolerance
    {
        size_t _size_bytes24_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err42_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->stall_tolerance, &buffer[offset_bits / 8U], &_size_bytes24_);
        if (_err42_ < 0)
        {
            return _err42_;
        }
        offset_bits += _size_bytes24_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 current_limit
    {
        size_t _size_bytes25_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err43_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->current_limit, &buffer[offset_bits / 8U], &_size_bytes25_);
        if (_err43_ < 0)
        {
            return _err43_;
        }
        offset_bits += _size_bytes25_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 speed_mult
    {
        size_t _size_bytes26_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err44_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->speed_mult, &buffer[offset_bits / 8U], &_size_bytes26_);
        if (_err44_ < 0)
        {
            return _err44_;
        }
        offset_bits += _size_bytes26_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 I_mult
    {
        size_t _size_bytes27_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err45_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->I_mult, &buffer[offset_bits / 8U], &_size_bytes27_);
        if (_err45_ < 0)
        {
            return _err45_;
        }
        offset_bits += _size_bytes27_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 PWM_mult
    {
        size_t _size_bytes28_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err46_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->PWM_mult, &buffer[offset_bits / 8U], &_size_bytes28_);
        if (_err46_ < 0)
        {
            return _err46_;
        }
        offset_bits += _size_bytes28_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Integer32.1.0 max_PWM_per_s
    {
        size_t _size_bytes29_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err47_ = uavcan_primitive_scalar_Integer32_1_0_deserialize_(
            &out_obj->max_PWM_per_s, &buffer[offset_bits / 8U], &_size_bytes29_);
        if (_err47_ < 0)
        {
            return _err47_;
        }
        offset_bits += _size_bytes29_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 speed_const
    {
        size_t _size_bytes30_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err48_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->speed_const, &buffer[offset_bits / 8U], &_size_bytes30_);
        if (_err48_ < 0)
        {
            return _err48_;
        }
        offset_bits += _size_bytes30_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 torque_const
    {
        size_t _size_bytes31_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err49_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->_torque_const, &buffer[offset_bits / 8U], &_size_bytes31_);
        if (_err49_ < 0)
        {
            return _err49_;
        }
        offset_bits += _size_bytes31_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 max_current
    {
        size_t _size_bytes32_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err50_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->max_current, &buffer[offset_bits / 8U], &_size_bytes32_);
        if (_err50_ < 0)
        {
            return _err50_;
        }
        offset_bits += _size_bytes32_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Real32.1.0 stall_current
    {
        size_t _size_bytes33_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err51_ = uavcan_primitive_scalar_Real32_1_0_deserialize_(
            &out_obj->stall_current, &buffer[offset_bits / 8U], &_size_bytes33_);
        if (_err51_ < 0)
        {
            return _err51_;
        }
        offset_bits += _size_bytes33_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // voltbro.config.six_step.pid_config.1.0 velocity_pid
    {
        // Delimiter header: truncated uint32
        size_t _size_bytes34_ = 0U;
        _size_bytes34_ = nunavutGetU32(&buffer[0], capacity_bytes, offset_bits, 32);
        offset_bits += 32U;
        if (_size_bytes34_ > (capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes)))
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_DELIMITER_HEADER;
        }
        const size_t _dh16_ = _size_bytes34_;  // Store the original delimiter header value.
        const int8_t _err52_ = voltbro_config_six_step_pid_config_1_0_deserialize_(
            &out_obj->velocity_pid, &buffer[offset_bits / 8U], &_size_bytes34_);
        if (_err52_ < 0)
        {
            return _err52_;
        }
        // Advance the offset by the size of the delimiter header, even if the nested deserialization routine
        // consumed fewer bytes of data. This behavior implements the implicit truncation rule for nested objects.
        offset_bits += _dh16_ * 8U;
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // voltbro.config.six_step.pid_config.1.0 current_pid
    {
        // Delimiter header: truncated uint32
        size_t _size_bytes35_ = 0U;
        _size_bytes35_ = nunavutGetU32(&buffer[0], capacity_bytes, offset_bits, 32);
        offset_bits += 32U;
        if (_size_bytes35_ > (capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes)))
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_DELIMITER_HEADER;
        }
        const size_t _dh17_ = _size_bytes35_;  // Store the original delimiter header value.
        const int8_t _err53_ = voltbro_config_six_step_pid_config_1_0_deserialize_(
            &out_obj->current_pid, &buffer[offset_bits / 8U], &_size_bytes35_);
        if (_err53_ < 0)
        {
            return _err53_;
        }
        // Advance the offset by the size of the delimiter header, even if the nested deserialization routine
        // consumed fewer bytes of data. This behavior implements the implicit truncation rule for nested objects.
        offset_bits += _dh17_ * 8U;
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void voltbro_config_six_step_values_1_0_initialize_(voltbro_config_six_step_values_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = voltbro_config_six_step_values_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

#ifdef __cplusplus
}
#endif
#endif // VOLTBRO_CONFIG_SIX_STEP_VALUES_1_0_INCLUDED_

