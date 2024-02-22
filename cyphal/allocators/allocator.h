#pragma once

#include <tuple>
#include <type_traits>

#include "cyphal/definitions.h"
#include "libcanard/canard.h"

class AbstractAllocator {
protected:
    UtilityConfig& utilities;

public:
    AbstractAllocator(size_t size, UtilityConfig& utilities) : utilities(utilities){};
    AbstractAllocator(const AbstractAllocator&) = delete;
    AbstractAllocator& operator=(const AbstractAllocator&) = delete;
    AbstractAllocator(AbstractAllocator&&) = delete;
    AbstractAllocator& operator=(AbstractAllocator&&) = delete;

    virtual void* allocate(CanardInstance* ins, size_t amount) = 0;
    virtual void free(CanardInstance* ins, void* pointer) = 0;
    virtual ~AbstractAllocator() = default;
};
