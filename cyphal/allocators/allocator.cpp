#include "allocator.h"

AbstractAllocator* allocator = nullptr;

AbstractAllocator* get_allocator() {
    return allocator;
}