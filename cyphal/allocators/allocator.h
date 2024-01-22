#pragma once

#include <tuple>
#include <type_traits>

#include "cyphal/definitions.h"
#include "libcanard/canard.h"

class AbstractAllocator {
public:
    explicit AbstractAllocator(size_t size) {};
    virtual void* allocate(CanardInstance* ins, size_t amount) = 0;
    virtual void free(CanardInstance* ins, void* pointer) = 0;
    virtual ~AbstractAllocator() {}
};
