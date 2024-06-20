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
// Source file:   /home/pi/control/external/public_regulated_data_types/uavcan/internet/udp/500.HandleIncomingPacket.0.1.dsdl
// Generated at:  2024-06-20 11:16:20.720088 UTC
// Is deprecated: yes
// Fixed port-ID: 500
// Full name:     uavcan.internet.udp.HandleIncomingPacket
// Version:       0.1
//
// Platform
//     python_implementation:  CPython
//     python_version:  3.12.3
//     python_release_level:  final
//     python_build:  ('main', 'Apr 10 2024 05:33:47')
//     python_compiler:  GCC 13.2.0
//     python_revision:
//     python_xoptions:  {}
//     runtime_platform:  Linux-6.8.0-1004-raspi-aarch64-with-glibc2.39
//
// Language Options
//     target_endianness:  little
//     omit_float_serialization_support:  False
//     enable_serialization_asserts:  False
//     enable_override_variable_array_capacity:  False
//     cast_format:  (({type}) {value})

//           _____  ______ _____  _____  ______ _____       _______ ______ _____
//          |  __ `|  ____|  __ `|  __ `|  ____/ ____|   /`|__   __|  ____|  __ `
//          | |  | | |__  | |__) | |__) | |__ | |       /  `  | |  | |__  | |  | |
//          | |  | |  __| |  ___/|  _  /|  __|| |      / /` ` | |  |  __| | |  | |
//          | |__| | |____| |    | | ` `| |___| |____ / ____ `| |  | |____| |__| |
//          |_____/|______|_|    |_|  `_`______`_____/_/    `_`_|  |______|_____/
//
// WARNING: this data type is deprecated and is nearing the end of its life cycle. Seek replacement.

#ifndef UAVCAN_INTERNET_UDP_HANDLE_INCOMING_PACKET_0_1_INCLUDED_
#define UAVCAN_INTERNET_UDP_HANDLE_INCOMING_PACKET_0_1_INCLUDED_

#include <nunavut/support/serialization.h>
#include <stdint.h>
#include <stdlib.h>

static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_TARGET_ENDIANNESS == 434322821,
              "/home/pi/control/external/public_regulated_data_types/uavcan/internet/udp/500.HandleIncomingPacket.0.1.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_OMIT_FLOAT_SERIALIZATION_SUPPORT == 0,
              "/home/pi/control/external/public_regulated_data_types/uavcan/internet/udp/500.HandleIncomingPacket.0.1.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_SERIALIZATION_ASSERTS == 0,
              "/home/pi/control/external/public_regulated_data_types/uavcan/internet/udp/500.HandleIncomingPacket.0.1.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_ENABLE_OVERRIDE_VARIABLE_ARRAY_CAPACITY == 0,
              "/home/pi/control/external/public_regulated_data_types/uavcan/internet/udp/500.HandleIncomingPacket.0.1.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );
static_assert( NUNAVUT_SUPPORT_LANGUAGE_OPTION_CAST_FORMAT == 2368206204,
              "/home/pi/control/external/public_regulated_data_types/uavcan/internet/udp/500.HandleIncomingPacket.0.1.dsdl is trying to use a serialization library that was compiled with "
              "different language options. This is dangerous and therefore not allowed." );

#ifdef __cplusplus
extern "C" {
#endif

#define uavcan_internet_udp_HandleIncomingPacket_0_1_HAS_FIXED_PORT_ID_ true
#define uavcan_internet_udp_HandleIncomingPacket_0_1_FIXED_PORT_ID_     500U

// +-------------------------------------------------------------------------------------------------------------------+
// | uavcan.internet.udp.HandleIncomingPacket.0.1
// +-------------------------------------------------------------------------------------------------------------------+
#define uavcan_internet_udp_HandleIncomingPacket_0_1_FULL_NAME_             "uavcan.internet.udp.HandleIncomingPacket"
#define uavcan_internet_udp_HandleIncomingPacket_0_1_FULL_NAME_AND_VERSION_ "uavcan.internet.udp.HandleIncomingPacket.0.1"

// +-------------------------------------------------------------------------------------------------------------------+
// | uavcan.internet.udp.HandleIncomingPacket.Request.0.1
// +-------------------------------------------------------------------------------------------------------------------+
#define uavcan_internet_udp_HandleIncomingPacket_Request_0_1_FULL_NAME_             "uavcan.internet.udp.HandleIncomingPacket.Request"
#define uavcan_internet_udp_HandleIncomingPacket_Request_0_1_FULL_NAME_AND_VERSION_ "uavcan.internet.udp.HandleIncomingPacket.Request.0.1"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define uavcan_internet_udp_HandleIncomingPacket_Request_0_1_EXTENT_BYTES_                    600UL
#define uavcan_internet_udp_HandleIncomingPacket_Request_0_1_SERIALIZATION_BUFFER_SIZE_BYTES_ 313UL
static_assert(uavcan_internet_udp_HandleIncomingPacket_Request_0_1_EXTENT_BYTES_ >= uavcan_internet_udp_HandleIncomingPacket_Request_0_1_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

/// Array metadata for: saturated uint8[<=309] payload
#define uavcan_internet_udp_HandleIncomingPacket_Request_0_1_payload_ARRAY_CAPACITY_           309U
#define uavcan_internet_udp_HandleIncomingPacket_Request_0_1_payload_ARRAY_IS_VARIABLE_LENGTH_ true

typedef struct
{
    /// saturated uint16 session_id
    uint16_t session_id;

    /// saturated uint8[<=309] payload
    struct  /// Array address equivalence guarantee: &elements[0] == &payload
    {
        uint8_t elements[uavcan_internet_udp_HandleIncomingPacket_Request_0_1_payload_ARRAY_CAPACITY_];
        size_t count;
    } payload;
} uavcan_internet_udp_HandleIncomingPacket_Request_0_1;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see uavcan_internet_udp_HandleIncomingPacket_Request_0_1_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t uavcan_internet_udp_HandleIncomingPacket_Request_0_1_serialize_(
    const uavcan_internet_udp_HandleIncomingPacket_Request_0_1* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    const size_t capacity_bytes = *inout_buffer_size_bytes;
    if ((8U * (size_t) capacity_bytes) < 2504UL)
    {
        return -NUNAVUT_ERROR_SERIALIZATION_BUFFER_TOO_SMALL;
    }
    // Notice that fields that are not an integer number of bytes long may overrun the space allocated for them
    // in the serialization buffer up to the next byte boundary. This is by design and is guaranteed to be safe.
    size_t offset_bits = 0U;
    {   // saturated uint16 session_id
        // Saturation code not emitted -- native representation matches the serialized representation.
        (void) memmove(&buffer[offset_bits / 8U], &obj->session_id, 2U);
        offset_bits += 16U;
    }
    {   // saturated uint8[<=309] payload
        if (obj->payload.count > 309)
        {
            return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
        }
        // Array length prefix: truncated uint16
        (void) memmove(&buffer[offset_bits / 8U], &obj->payload.count, 2U);
        offset_bits += 16U;
        // Optimization prospect: this item is aligned at the byte boundary, so it is possible to use memmove().
        nunavutCopyBits(&buffer[0], offset_bits, obj->payload.count * 8U, &obj->payload.elements[0], 0U);
        offset_bits += obj->payload.count * 8U;
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
static inline int8_t uavcan_internet_udp_HandleIncomingPacket_Request_0_1_deserialize_(
    uavcan_internet_udp_HandleIncomingPacket_Request_0_1* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
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
    // saturated uint16 session_id
    out_obj->session_id = nunavutGetU16(&buffer[0], capacity_bytes, offset_bits, 16);
    offset_bits += 16U;
    // saturated uint8[<=309] payload
    // Array length prefix: truncated uint16
    out_obj->payload.count = nunavutGetU16(&buffer[0], capacity_bytes, offset_bits, 16);
    offset_bits += 16U;
    if (out_obj->payload.count > 309U)
    {
        return -NUNAVUT_ERROR_REPRESENTATION_BAD_ARRAY_LENGTH;
    }
    nunavutGetBits(&out_obj->payload.elements[0], &buffer[0], capacity_bytes, offset_bits, out_obj->payload.count * 8U);
    offset_bits += out_obj->payload.count * 8U;
    offset_bits = (offset_bits + 7U) & ~(size_t) 7U;  // Align on 8 bits.
    *inout_buffer_size_bytes = (size_t) (nunavutChooseMin(offset_bits, capacity_bits) / 8U);
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void uavcan_internet_udp_HandleIncomingPacket_Request_0_1_initialize_(uavcan_internet_udp_HandleIncomingPacket_Request_0_1* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = uavcan_internet_udp_HandleIncomingPacket_Request_0_1_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

// +-------------------------------------------------------------------------------------------------------------------+
// | uavcan.internet.udp.HandleIncomingPacket.Response.0.1
// +-------------------------------------------------------------------------------------------------------------------+
#define uavcan_internet_udp_HandleIncomingPacket_Response_0_1_FULL_NAME_             "uavcan.internet.udp.HandleIncomingPacket.Response"
#define uavcan_internet_udp_HandleIncomingPacket_Response_0_1_FULL_NAME_AND_VERSION_ "uavcan.internet.udp.HandleIncomingPacket.Response.0.1"

/// Extent is the minimum amount of memory required to hold any serialized representation of any compatible
/// version of the data type; or, on other words, it is the the maximum possible size of received objects of this type.
/// The size is specified in bytes (rather than bits) because by definition, extent is an integer number of bytes long.
/// When allocating a deserialization (RX) buffer for this data type, it should be at least extent bytes large.
/// When allocating a serialization (TX) buffer, it is safe to use the size of the largest serialized representation
/// instead of the extent because it provides a tighter bound of the object size; it is safe because the concrete type
/// is always known during serialization (unlike deserialization). If not sure, use extent everywhere.
#define uavcan_internet_udp_HandleIncomingPacket_Response_0_1_EXTENT_BYTES_                    63UL
#define uavcan_internet_udp_HandleIncomingPacket_Response_0_1_SERIALIZATION_BUFFER_SIZE_BYTES_ 0UL
static_assert(uavcan_internet_udp_HandleIncomingPacket_Response_0_1_EXTENT_BYTES_ >= uavcan_internet_udp_HandleIncomingPacket_Response_0_1_SERIALIZATION_BUFFER_SIZE_BYTES_,
              "Internal constraint violation");

typedef struct
{
    uint8_t _dummy_;
} uavcan_internet_udp_HandleIncomingPacket_Response_0_1;

/// Serialize an instance into the provided buffer.
/// The lifetime of the resulting serialized representation is independent of the original instance.
/// This method may be slow for large objects (e.g., images, point clouds, radar samples), so in a later revision
/// we may define a zero-copy alternative that keeps references to the original object where possible.
///
/// @param obj      The object to serialize.
///
/// @param buffer   The destination buffer. There are no alignment requirements.
///                 @see uavcan_internet_udp_HandleIncomingPacket_Response_0_1_SERIALIZATION_BUFFER_SIZE_BYTES_
///
/// @param inout_buffer_size_bytes  When calling, this is a pointer to the size of the buffer in bytes.
///                                 Upon return this value will be updated with the size of the constructed serialized
///                                 representation (in bytes); this value is then to be passed over to the transport
///                                 layer. In case of error this value is undefined.
///
/// @returns Negative on error, zero on success.
static inline int8_t uavcan_internet_udp_HandleIncomingPacket_Response_0_1_serialize_(
    const uavcan_internet_udp_HandleIncomingPacket_Response_0_1* const obj, uint8_t* const buffer,  size_t* const inout_buffer_size_bytes)
{
    if ((obj == NULL) || (buffer == NULL) || (inout_buffer_size_bytes == NULL))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    *inout_buffer_size_bytes = 0U;
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
static inline int8_t uavcan_internet_udp_HandleIncomingPacket_Response_0_1_deserialize_(
    uavcan_internet_udp_HandleIncomingPacket_Response_0_1* const out_obj, const uint8_t* buffer, size_t* const inout_buffer_size_bytes)
{
    if ((out_obj == NULL) || (inout_buffer_size_bytes == NULL) || ((buffer == NULL) && (0 != *inout_buffer_size_bytes)))
    {
        return -NUNAVUT_ERROR_INVALID_ARGUMENT;
    }
    if (buffer == NULL)
    {
        buffer = (const uint8_t*)"";
    }
    *inout_buffer_size_bytes = 0U;
    return NUNAVUT_SUCCESS;
}

/// Initialize an instance to default values. Does nothing if @param out_obj is NULL.
/// This function intentionally leaves inactive elements uninitialized; for example, members of a variable-length
/// array beyond its length are left uninitialized; aliased union memory that is not used by the first union field
/// is left uninitialized, etc. If full zero-initialization is desired, just use memset(&obj, 0, sizeof(obj)).
static inline void uavcan_internet_udp_HandleIncomingPacket_Response_0_1_initialize_(uavcan_internet_udp_HandleIncomingPacket_Response_0_1* const out_obj)
{
    if (out_obj != NULL)
    {
        size_t size_bytes = 0;
        const uint8_t buf = 0;
        const int8_t err = uavcan_internet_udp_HandleIncomingPacket_Response_0_1_deserialize_(out_obj, &buf, &size_bytes);

        (void) err;
    }
}

#ifdef __cplusplus
}
#endif
#endif // UAVCAN_INTERNET_UDP_HANDLE_INCOMING_PACKET_0_1_INCLUDED_
