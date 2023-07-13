#include "o1_allocator.h"

void* O1Allocator::allocate(CanardInstance* ins, size_t amount) {
    (void)ins;
    void* mem;

    CRITICAL_SECTION({ mem = o1heapAllocate(o1heap, amount); })
    if (mem == nullptr) {
        Error_Handler();
    }
    return mem;
}

void O1Allocator::free(CanardInstance* ins, void* pointer) {
    (void)ins;
    CRITICAL_SECTION({ o1heapFree(o1heap, pointer); })
}

O1Allocator::O1Allocator(size_t size) {
    o1heapInit(o1heap, size);
}
