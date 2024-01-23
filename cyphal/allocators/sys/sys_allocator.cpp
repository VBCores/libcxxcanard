#include "sys_allocator.h"
#include <cstdlib>

void* SystemAllocator::allocate(CanardInstance* const ins, const size_t amount) {
    (void)ins;
    void* mem;

    CRITICAL_SECTION({ mem = std::malloc(amount); })
    if (mem == nullptr) {
        utilities.error_handler();
    }
    return mem;
}

void SystemAllocator::free(CanardInstance* const ins, void* const pointer) {
    (void)ins;
    CRITICAL_SECTION({ std::free(pointer); })
}
