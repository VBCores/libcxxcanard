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
// Source file:   /Users/igor/Work/misc/cyphal_ws/types/voltbro/battery/state.1.0.dsdl
// Generated at:  2025-12-16 13:34:01.631748 UTC
// Is deprecated: no
// Fixed port-ID: None
// Full name:     voltbro.battery.state
// Version:       1.0
//
// Platform
//     python_implementation:  CPython
//     python_version:  3.13.7
//     python_release_level:  final
//     python_build:  ('main', 'Aug 14 2025 11:12:11')
//     python_compiler:  Clang 17.0.0 (clang-1700.0.13.3)
//     python_revision:
//     python_xoptions:  {}
//     runtime_platform:  macOS-15.5-arm64-arm-64bit-Mach-O
//
// Language Options
//     target_endianness:  little
//     omit_float_serialization_support:  False
//     enable_serialization_asserts:  False
//     enable_override_variable_array_capacity:  False
//     cast_format:  (({type}) {value})

#ifndef VOLTBRO_BATTERY_STATE_1_0_INCLUDED_
#define VOLTBRO_BATTERY_STATE_1_0_INCLUDED_

#include <nunavut/support/serialization.h>
#include <stdlib.h>
#include <uavcan/primitive/String_1_0.h>
#include <uavcan/primitive/scalar/Integer8_1_0.h>
#include <uavcan/si/unit/electric_charge/Scalar_1_0.h>
#include <uavcan/si/unit/electric_current/Scalar_1_0.h>
#include <uavcan/si/unit/voltage/Scalar_1_0.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 434322821,
              "/Users/igor/Work/misc/cyphal_ws/types/voltbro/battery/state.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/Users/igor/Work/misc/cyphal_ws/types/voltbro/battery/state.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/Users/igor/Work/misc/cyphal_ws/types/voltbro/battery/state.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/Users/igor/Work/misc/cyphal_ws/types/voltbro/battery/state.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/Users/igor/Work/misc/cyphal_ws/types/voltbro/battery/state.1.0.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

/// This type does not have a fixed port-ID. See https://forum.opencyphal.org/t/choosing-message-and-service-ids/889
#define voltbro_battery_state_1_0_HAS_FIXED_PORT_ID_ false

// +-------------------------------------------------------------------------------------------------------------------+
// | voltbro.battery.state.1.0
// +-------------------------------------------------------------------------------------------------------------------+
#define voltbro_battery_state_1_0_FULL_NAME_             "voltbro.battery.state"
#define voltbro_battery_state_1_0_FULL_NAME_AND_VERSION_ "voltbro.battery.state.1.0"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define voltbro_battery_state_1_0_EXTENT_BYTES_                    540UL
#define voltbro_battery_state_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_ 540UL
static_assert(voltbro_battery_state_1_0_EXTENT_BYTES_ >= voltbro_battery_state_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

typedef struct
{
    /// uavcan.si.unit.voltage.Scalar.1.0 voltage
    uavcan_si_unit_voltage_Scalar_1_0 voltage;

    /// uavcan.si.unit.electric_current.Scalar.1.0 current
    uavcan_si_unit_electric_current_Scalar_1_0 current;

    /// uavcan.si.unit.electric_charge.Scalar.1.0 charge
    uavcan_si_unit_electric_charge_Scalar_1_0 charge;

    /// uavcan.si.unit.electric_charge.Scalar.1.0 capacity
    uavcan_si_unit_electric_charge_Scalar_1_0 capacity;

    /// uavcan.si.unit.electric_charge.Scalar.1.0 design_capacity
    uavcan_si_unit_electric_charge_Scalar_1_0 design_capacity;

    /// uavcan.primitive.scalar.Integer8.1.0 power_supply_status
    uavcan_primitive_scalar_Integer8_1_0 power_supply_status;

    /// uavcan.primitive.scalar.Integer8.1.0 power_supply_health
    uavcan_primitive_scalar_Integer8_1_0 power_supply_health;

    /// uavcan.primitive.scalar.Integer8.1.0 power_supply_technology
    uavcan_primitive_scalar_Integer8_1_0 power_supply_technology;

    /// uavcan.primitive.scalar.Integer8.1.0 is_present
    uavcan_primitive_scalar_Integer8_1_0 is_present;

    /// uavcan.primitive.String.1.0 location
    uavcan_primitive_String_1_0 location;

    /// uavcan.primitive.String.1.0 serial_number
    uavcan_primitive_String_1_0 serial_number;
} voltbro_battery_state_1_0;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see voltbro_battery_state_1_0_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t voltbro_battery_state_1_0_serialize_(
    const voltbro_battery_state_1_0* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 4320UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // uavcan.si.unit.voltage.Scalar.1.0 voltage
        size_t _size_bytes0_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err0_ = uavcan_si_unit_voltage_Scalar_1_0_serialize_(
            &obj->voltage, &buffer[offset_bits / 8U], &_size_bytes0_);
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
    {   // uavcan.si.unit.electric_current.Scalar.1.0 current
        size_t _size_bytes1_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err2_ = uavcan_si_unit_electric_current_Scalar_1_0_serialize_(
            &obj->current, &buffer[offset_bits / 8U], &_size_bytes1_);
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
    {   // uavcan.si.unit.electric_charge.Scalar.1.0 charge
        size_t _size_bytes2_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err4_ = uavcan_si_unit_electric_charge_Scalar_1_0_serialize_(
            &obj->charge, &buffer[offset_bits / 8U], &_size_bytes2_);
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
    {   // uavcan.si.unit.electric_charge.Scalar.1.0 capacity
        size_t _size_bytes3_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err6_ = uavcan_si_unit_electric_charge_Scalar_1_0_serialize_(
            &obj->capacity, &buffer[offset_bits / 8U], &_size_bytes3_);
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
    {   // uavcan.si.unit.electric_charge.Scalar.1.0 design_capacity
        size_t _size_bytes4_ = 4UL;  // Nested object (max) size, in bytes.
        int8_t _err8_ = uavcan_si_unit_electric_charge_Scalar_1_0_serialize_(
            &obj->design_capacity, &buffer[offset_bits / 8U], &_size_bytes4_);
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
    {   // uavcan.primitive.scalar.Integer8.1.0 power_supply_status
        size_t _size_bytes5_ = 1UL;  // Nested object (max) size, in bytes.
        int8_t _err10_ = uavcan_primitive_scalar_Integer8_1_0_serialize_(
            &obj->power_supply_status, &buffer[offset_bits / 8U], &_size_bytes5_);
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
    {   // uavcan.primitive.scalar.Integer8.1.0 power_supply_health
        size_t _size_bytes6_ = 1UL;  // Nested object (max) size, in bytes.
        int8_t _err12_ = uavcan_primitive_scalar_Integer8_1_0_serialize_(
            &obj->power_supply_health, &buffer[offset_bits / 8U], &_size_bytes6_);
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
    {   // uavcan.primitive.scalar.Integer8.1.0 power_supply_technology
        size_t _size_bytes7_ = 1UL;  // Nested object (max) size, in bytes.
        int8_t _err14_ = uavcan_primitive_scalar_Integer8_1_0_serialize_(
            &obj->power_supply_technology, &buffer[offset_bits / 8U], &_size_bytes7_);
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
    {   // uavcan.primitive.scalar.Integer8.1.0 is_present
        size_t _size_bytes8_ = 1UL;  // Nested object (max) size, in bytes.
        int8_t _err16_ = uavcan_primitive_scalar_Integer8_1_0_serialize_(
            &obj->is_present, &buffer[offset_bits / 8U], &_size_bytes8_);
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
    {   // uavcan.primitive.String.1.0 location
        size_t _size_bytes9_ = 258UL;  // Nested object (max) size, in bytes.
        int8_t _err18_ = uavcan_primitive_String_1_0_serialize_(
            &obj->location, &buffer[offset_bits / 8U], &_size_bytes9_);
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
    {   // uavcan.primitive.String.1.0 serial_number
        size_t _size_bytes10_ = 258UL;  // Nested object (max) size, in bytes.
        int8_t _err20_ = uavcan_primitive_String_1_0_serialize_(
            &obj->serial_number, &buffer[offset_bits / 8U], &_size_bytes10_);
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
static inline int8_t voltbro_battery_state_1_0_deserialize_(
    voltbro_battery_state_1_0* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // uavcan.si.unit.voltage.Scalar.1.0 voltage
    {
        size_t _size_bytes11_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err22_ = uavcan_si_unit_voltage_Scalar_1_0_deserialize_(
            &out_obj->voltage, &buffer[offset_bits / 8U], &_size_bytes11_);
        if (_err22_ < 0)
        {
            return _err22_;
        }
        offset_bits += _size_bytes11_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.si.unit.electric_current.Scalar.1.0 current
    {
        size_t _size_bytes12_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err23_ = uavcan_si_unit_electric_current_Scalar_1_0_deserialize_(
            &out_obj->current, &buffer[offset_bits / 8U], &_size_bytes12_);
        if (_err23_ < 0)
        {
            return _err23_;
        }
        offset_bits += _size_bytes12_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.si.unit.electric_charge.Scalar.1.0 charge
    {
        size_t _size_bytes13_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err24_ = uavcan_si_unit_electric_charge_Scalar_1_0_deserialize_(
            &out_obj->charge, &buffer[offset_bits / 8U], &_size_bytes13_);
        if (_err24_ < 0)
        {
            return _err24_;
        }
        offset_bits += _size_bytes13_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.si.unit.electric_charge.Scalar.1.0 capacity
    {
        size_t _size_bytes14_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err25_ = uavcan_si_unit_electric_charge_Scalar_1_0_deserialize_(
            &out_obj->capacity, &buffer[offset_bits / 8U], &_size_bytes14_);
        if (_err25_ < 0)
        {
            return _err25_;
        }
        offset_bits += _size_bytes14_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.si.unit.electric_charge.Scalar.1.0 design_capacity
    {
        size_t _size_bytes15_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err26_ = uavcan_si_unit_electric_charge_Scalar_1_0_deserialize_(
            &out_obj->design_capacity, &buffer[offset_bits / 8U], &_size_bytes15_);
        if (_err26_ < 0)
        {
            return _err26_;
        }
        offset_bits += _size_bytes15_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Integer8.1.0 power_supply_status
    {
        size_t _size_bytes16_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err27_ = uavcan_primitive_scalar_Integer8_1_0_deserialize_(
            &out_obj->power_supply_status, &buffer[offset_bits / 8U], &_size_bytes16_);
        if (_err27_ < 0)
        {
            return _err27_;
        }
        offset_bits += _size_bytes16_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Integer8.1.0 power_supply_health
    {
        size_t _size_bytes17_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err28_ = uavcan_primitive_scalar_Integer8_1_0_deserialize_(
            &out_obj->power_supply_health, &buffer[offset_bits / 8U], &_size_bytes17_);
        if (_err28_ < 0)
        {
            return _err28_;
        }
        offset_bits += _size_bytes17_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Integer8.1.0 power_supply_technology
    {
        size_t _size_bytes18_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err29_ = uavcan_primitive_scalar_Integer8_1_0_deserialize_(
            &out_obj->power_supply_technology, &buffer[offset_bits / 8U], &_size_bytes18_);
        if (_err29_ < 0)
        {
            return _err29_;
        }
        offset_bits += _size_bytes18_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.scalar.Integer8.1.0 is_present
    {
        size_t _size_bytes19_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err30_ = uavcan_primitive_scalar_Integer8_1_0_deserialize_(
            &out_obj->is_present, &buffer[offset_bits / 8U], &_size_bytes19_);
        if (_err30_ < 0)
        {
            return _err30_;
        }
        offset_bits += _size_bytes19_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.String.1.0 location
    {
        size_t _size_bytes20_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err31_ = uavcan_primitive_String_1_0_deserialize_(
            &out_obj->location, &buffer[offset_bits / 8U], &_size_bytes20_);
        if (_err31_ < 0)
        {
            return _err31_;
        }
        offset_bits += _size_bytes20_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    // uavcan.primitive.String.1.0 serial_number
    {
        size_t _size_bytes21_ = (size_t)(capacity_bytes - nunavutChooseMin((offset_bits / 8U), capacity_bytes));
        const int8_t _err32_ = uavcan_primitive_String_1_0_deserialize_(
            &out_obj->serial_number, &buffer[offset_bits / 8U], &_size_bytes21_);
        if (_err32_ < 0)
        {
            return _err32_;
        }
        offset_bits += _size_bytes21_ * 8U;  // Advance by the size of the nested serialized representation.
    }
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void voltbro_battery_state_1_0_initialize_(voltbro_battery_state_1_0* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = voltbro_battery_state_1_0_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

#ifdef __cplusplus
}
#endif
#endif // VOLTBRO_BATTERY_STATE_1_0_INCLUDED_

