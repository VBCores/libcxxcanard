#include "o1_allocator.h"

#ifdef __linux__
#include <new>
#endif
#include <stdlib.h>

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

O1Allocator::O1Allocator(size_t size) {
#ifdef __linux__
    memory_arena = new(std::align_val_t{O1HEAP_ALIGNMENT}) uint8_t[size];
#else
    memory_arena = std::malloc(size);
#endif
    if (memory_arena == nullptr) {
        error_handler();
    }

#ifndef __linux__
    auto shift = (int)((uint8_t*)memory_arena) % O1HEAP_ALIGNMENT;
    if (shift != 0) {
        memory_arena = (void*)((uint8_t*)memory_arena + shift);
        size -= shift;
    }
#endif

    O1HeapInstance* out = o1heapInit(memory_arena, size);
    if (out == nullptr) {
        error_handler();
    }
    o1heap = out;
}

O1Allocator::~O1Allocator() {
#ifdef __linux__
    ::operator delete[](memory_arena, std::align_val_t{O1HEAP_ALIGNMENT});
#else
	std::free(memory_arena);
#endif
}
