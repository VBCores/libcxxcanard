#pragma once

#include "../allocator.h"

/**
 * Наивный менеджер памяти, просто обертка вокруг malloc и free.
 */
class SystemAllocator : public AbstractAllocator {
public:

    #pragma GCC diagnostic push
    #pragma GCC diagnostic ignored "-Wunused-parameter"
    // NOTE: <size> parameter required by the interface, but not used in this implementation
    // TODO: do something with size value?
    explicit SystemAllocator(size_t size, const UtilityConfig& utilities)
        : AbstractAllocator(utilities){};
    #pragma GCC diagnostic pop
    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};
