#include "sys_allocator.h"
#include <cstdlib>

void* SystemAllocator::allocate(CanardInstance* const ins, const size_t amount) {
    (void)ins;
    void* mem = nullptr;

    // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-no-malloc,hicpp-no-malloc)
    CRITICAL_SECTION({ mem = std::malloc(amount); })
    // NOLINTEND(cppcoreguidelines-owning-memory,cppcoreguidelines-no-malloc,hicpp-no-malloc)

    if (mem == nullptr) {
        utilities.error_handler();
    }
    return mem;
}

void SystemAllocator::free(CanardInstance* const ins, void* const pointer) {
    (void)ins;

    // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-no-malloc,hicpp-no-malloc)
    CRITICAL_SECTION({ std::free(pointer); })
    // NOLINTEND(cppcoreguidelines-owning-memory,cppcoreguidelines-no-malloc,hicpp-no-malloc)
}
