#include "o1_allocator.h"

#include <new>

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
    memory_arena = new(std::align_val_t{O1HEAP_ALIGNMENT}) uint8_t[size];
    O1HeapInstance* out = o1heapInit(memory_arena, size);
    if (out == nullptr) {
        error_handler();
    }
    o1heap = out;
}

O1Allocator::~O1Allocator() {
    ::operator delete[](memory_arena, std::align_val_t{O1HEAP_ALIGNMENT});
}
