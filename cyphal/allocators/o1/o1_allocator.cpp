#include "o1_allocator.h"

void* O1Allocator::allocate(CanardInstance* ins, size_t amount) {
    (void)ins;
    void* mem;

    CRITICAL_SECTION({ mem = o1heapAllocate(o1heap, amount); })
    if (mem == nullptr) {
        error_handler();
    }
    return mem;
}

void O1Allocator::free(CanardInstance* ins, void* pointer) {
    (void)ins;
    CRITICAL_SECTION({ o1heapFree(o1heap, pointer); })
}

O1Allocator::O1Allocator(size_t size) {
    memory_arena = new uint8_t[size];
    O1HeapInstance* out = o1heapInit(memory_arena, size);
    if (out == nullptr) {
        error_handler();
    }
    o1heap = out;
}

O1Allocator::~O1Allocator() {
    delete (uint8_t*)memory_arena;
}
