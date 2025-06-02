#include "o1_allocator.h"

#ifdef __linux__
#include <new>
#endif
#include <cstdlib>

void* O1Allocator::allocate(CanardInstance* ins, size_t amount) {
    (void)ins;
    void* mem = nullptr;

    CRITICAL_SECTION({ mem = o1heapAllocate(o1heap, amount); })

    return mem;
}

void O1Allocator::free(CanardInstance* ins, void* pointer) {
    (void)ins;
    CRITICAL_SECTION({ o1heapFree(o1heap, pointer); })
}

void O1Allocator::align_self(size_t size) {
    if (!is_self_allocated) {
        auto loc = reinterpret_cast<uintptr_t>(memory_arena);
        auto shift = loc % O1HEAP_ALIGNMENT;
        if (shift != 0) {
            // NOLINTBEGIN(performance-no-int-to-ptr)
            memory_arena = reinterpret_cast<void*>(loc + shift);
            // NOLINTEND(performance-no-int-to-ptr)
            size -= shift;
        }
    }

    O1HeapInstance* out = o1heapInit(memory_arena, size);
    if (out == nullptr) {
        utilities.error_handler();
    }
    o1heap = out;
}

O1Allocator::O1Allocator(size_t size, void* memory, const UtilityConfig& utilities)
    : AbstractAllocator(size, utilities), memory_arena(memory) {
    align_self(size);
}

O1Allocator::O1Allocator(size_t size, const UtilityConfig& utilities)
    : AbstractAllocator(size, utilities),
      memory_arena(operator new(size, std::align_val_t{O1HEAP_ALIGNMENT})) {
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
    operator delete(memory_arena, std::align_val_t{O1HEAP_ALIGNMENT});
}
