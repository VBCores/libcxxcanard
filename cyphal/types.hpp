#pragma once

#include <cstddef>
#include <cstdint>
#include <type_traits>

template <typename ObjType>
using cyphal_serializer = int8_t (*)(const ObjType* const, uint8_t* const, size_t* const);

template <typename ObjType>
using cyphal_deserializer = int8_t (*)(ObjType* const, const uint8_t*, size_t* const);

template <typename ObjType>
struct CyphalTypeTraits;

template <typename>
struct CyphalAlwaysFalse : std::false_type {};

template <typename T>
struct CyphalTypeTraits {
    static_assert(
        CyphalAlwaysFalse<T>::value,
        "Missing CyphalTypeTraits<T>. Include the generated C++ traits header for this DSDL type.");
};
