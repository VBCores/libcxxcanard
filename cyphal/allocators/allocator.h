#pragma once

#include <tuple>
#include <type_traits>

#include "definitions.h"
#include "libcanard/canard.h"

class AbstractAllocator {
   public:
    virtual void* allocate(CanardInstance* ins, size_t amount) = 0;
    virtual void free(CanardInstance* ins, void* pointer) = 0;
};

extern AbstractAllocator* allocator;
inline void* allocate(CanardInstance* ins, size_t amount) {
    return allocator->allocate(ins, amount);
}
inline void free(CanardInstance* ins, void* ptr) {
    return allocator->free(ins, ptr);
}
template <class T>
std::tuple<CanardMemoryAllocate, CanardMemoryFree> get_memory_pair() {
    static_assert(
        std::is_convertible<T, AbstractAllocator>::value,
        "Must be a subclass of AbstractAllocator"
    );
    if (allocator != nullptr) {
        perror("Tried to reinitialize allocator");
    }
    allocator = new T();
    return {allocate, free};
}
