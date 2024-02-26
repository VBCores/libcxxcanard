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
// Source file:   /home/pi/ws/libs/types/public_regulated_data_types/uavcan/si/unit/magnetic_field_strength/Vector3.1.1.dsdl
// Generated at:  2024-02-26 15:58:42.362008 UTC
// Is deprecated: no
// Fixed port-ID: None
// Full name:     uavcan.si.unit.magnetic_field_strength.Vector3
// Version:       1.1
//
// Platform
//     python_implementation:  CPython
//     python_version:  3.10.12
//     python_release_level:  final
//     python_build:  ('main', 'Nov 20 2023 15:14:05')
//     python_compiler:  GCC 11.4.0
//     python_revision:
//     python_xoptions:  {}
//     runtime_platform:  Linux-5.15.0-1046-raspi-aarch64-with-glibc2.35
//
// Language Options
//     target_endianness:  little
//     omit_float_serialization_support:  False
//     enable_serialization_asserts:  False
//     enable_override_variable_array_capacity:  False
//     cast_format:  (({type}) {value})

#ifndef UAVCAN_SI_UNIT_MAGNETIC_FIELD_STRENGTH_VECTOR3_1_1_INCLUDED_
#define UAVCAN_SI_UNIT_MAGNETIC_FIELD_STRENGTH_VECTOR3_1_1_INCLUDED_

#include <nunavut/support/serialization.h>
#include <stdlib.h>
#include <string.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 434322821,
              "/home/pi/ws/libs/types/public_regulated_data_types/uavcan/si/unit/magnetic_field_strength/Vector3.1.1.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/home/pi/ws/libs/types/public_regulated_data_types/uavcan/si/unit/magnetic_field_strength/Vector3.1.1.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/home/pi/ws/libs/types/public_regulated_data_types/uavcan/si/unit/magnetic_field_strength/Vector3.1.1.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/home/pi/ws/libs/types/public_regulated_data_types/uavcan/si/unit/magnetic_field_strength/Vector3.1.1.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/home/pi/ws/libs/types/public_regulated_data_types/uavcan/si/unit/magnetic_field_strength/Vector3.1.1.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

/// This type does not have a fixed port-ID. See https://forum.opencyphal.org/t/choosing-message-and-service-ids/889
#define uavcan_si_unit_magnetic_field_strength_Vector3_1_1_HAS_FIXED_PORT_ID_ false

// +-------------------------------------------------------------------------------------------------------------------+
// | uavcan.si.unit.magnetic_field_strength.Vector3.1.1
// +-------------------------------------------------------------------------------------------------------------------+
#define uavcan_si_unit_magnetic_field_strength_Vector3_1_1_FULL_NAME_             "uavcan.si.unit.magnetic_field_strength.Vector3"
#define uavcan_si_unit_magnetic_field_strength_Vector3_1_1_FULL_NAME_AND_VERSION_ "uavcan.si.unit.magnetic_field_strength.Vector3.1.1"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define uavcan_si_unit_magnetic_field_strength_Vector3_1_1_EXTENT_BYTES_                    12UL
#define uavcan_si_unit_magnetic_field_strength_Vector3_1_1_SERIALIZATION_BUFFER_SIZE_BYTES_ 12UL
static_assert(uavcan_si_unit_magnetic_field_strength_Vector3_1_1_EXTENT_BYTES_ >= uavcan_si_unit_magnetic_field_strength_Vector3_1_1_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// Array metadata for: saturated float32[3] ampere_per_meter
#define uavcan_si_unit_magnetic_field_strength_Vector3_1_1_ampere_per_meter_ARRAY_CAPACITY_           3U
#define uavcan_si_unit_magnetic_field_strength_Vector3_1_1_ampere_per_meter_ARRAY_IS_VARIABLE_LENGTH_ false

typedef struct
{
    /// saturated float32[3] ampere_per_meter
    float ampere_per_meter[3];
} uavcan_si_unit_magnetic_field_strength_Vector3_1_1;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see uavcan_si_unit_magnetic_field_strength_Vector3_1_1_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t uavcan_si_unit_magnetic_field_strength_Vector3_1_1_serialize_(
    const uavcan_si_unit_magnetic_field_strength_Vector3_1_1* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 96UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // saturated float32[3] ampere_per_meter
        // Saturation code not emitted -- assume the native representation is conformant.
        static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
        // Optimization prospect: this item is aligned at the byte boundary, so it is possible to use memmove().
        nunavutCopyBits(&buffer[0], offset_bits, 3UL * 32UL, &obj->ampere_per_meter[0], 0U);
        offset_bits += 3UL * 32UL;
    }
    if (offset_bits % 8U != 0U)  // Pad to 8 bits. TODO: Eliminate redundant padding checks.
    {
        const uint8_t _pad0_ = (uint8_t)(8U - offset_bits % 8U);
        const int8_t _err0_ = nunavutSetUxx(&buffer[0], capacity_bytes, offset_bits, 0U, _pad0_);  // Optimize?
        if (_err0_ < 0)
        {
            return _err0_;
        }
        offset_bits += _pad0_;
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
static inline int8_t uavcan_si_unit_magnetic_field_strength_Vector3_1_1_deserialize_(
    uavcan_si_unit_magnetic_field_strength_Vector3_1_1* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // saturated float32[3] ampere_per_meter
    static_assert(NUNAVUT_PLATFORM_IEEE754_FLOAT, "Native IEEE754 binary32 required. TODO: relax constraint");
    nunavutGetBits(&out_obj->ampere_per_meter[0], &buffer[0], capacity_bytes, offset_bits, 3UL * 32U);
    offset_bits += 3UL * 32U;
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void uavcan_si_unit_magnetic_field_strength_Vector3_1_1_initialize_(uavcan_si_unit_magnetic_field_strength_Vector3_1_1* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = uavcan_si_unit_magnetic_field_strength_Vector3_1_1_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

#ifdef __cplusplus
}
#endif
#endif // UAVCAN_SI_UNIT_MAGNETIC_FIELD_STRENGTH_VECTOR3_1_1_INCLUDED_
