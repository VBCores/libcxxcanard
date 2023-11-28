#pragma once

#include <tuple>
#include <type_traits>

#include "cyphal/definitions.h"
#include "libcanard/canard.h"

class AbstractAllocator {
public:
    virtual void* allocate(CanardInstance* ins, size_t amount) = 0;
    virtual void free(CanardInstance* ins, void* pointer) = 0;
    virtual ~AbstractAllocator() {}
};

extern AbstractAllocator* allocator;
inline void* allocate(CanardInstance* ins, size_t amount) {
    return allocator->allocate(ins, amount);
}
inline void free(CanardInstance* ins, void* ptr) {
    return allocator->free(ins, ptr);
}

AbstractAllocator* get_allocator();

template <class T, class... Args>
std::tuple<CanardMemoryAllocate, CanardMemoryFree> get_memory_pair(Args&&... args) {
    if (allocator != nullptr) {
        error_handler();
    }
    allocator = new T(args...);
    return {allocate, free};
}
