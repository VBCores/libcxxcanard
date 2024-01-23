#include "o1_allocator.h"

#ifdef __linux__
#include <new>
#endif
#include <stdlib.h>

#define CPP17 201703L

void* O1Allocator::allocate(CanardInstance* ins, size_t amount) {
    (void)ins;
    void* mem;

    CRITICAL_SECTION({ mem = o1heapAllocate(o1heap, amount); })

    return mem;
}

void O1Allocator::free(CanardInstance* ins, void* pointer) {
    (void)ins;
    CRITICAL_SECTION({ o1heapFree(o1heap, pointer); })
}

void O1Allocator::align_self(size_t size) {
    if (!is_self_allocated || __cplusplus < CPP17) {
        uintptr_t loc = (uintptr_t)memory_arena;
        auto shift = loc % O1HEAP_ALIGNMENT;
        if (shift != 0) {
            memory_arena = (void*)(loc + shift);
            size -= shift;
        }
    }

    O1HeapInstance* out = o1heapInit(memory_arena, size);
    if (out == nullptr) {
        utilities.error_handler();
    }
    o1heap = out;
}

O1Allocator::O1Allocator(size_t size, void* memory, UtilityConfig& utilities):
    AbstractAllocator(size, utilities),
    memory_arena(memory)
    {
    align_self(size);
}

O1Allocator::O1Allocator(size_t size, UtilityConfig& utilities): AbstractAllocator(size, utilities) {
#if __cplusplus >= CPP17
    memory_arena = new (std::align_val_t{O1HEAP_ALIGNMENT}) uint8_t[size];
#else
    memory_arena = new uint8_t[size];
#endif

    if (memory_arena == nullptr) {
        utilities.error_handler();
    }
    is_self_allocated = true;

    align_self(size);
}

O1Allocator::~O1Allocator() {
    if (!is_self_allocated) {
        return;
    }
#if __cplusplus >= CPP17
    ::operator delete[](memory_arena, std::align_val_t{O1HEAP_ALIGNMENT});
#else
    delete[] memory_arena;
#endif
}
