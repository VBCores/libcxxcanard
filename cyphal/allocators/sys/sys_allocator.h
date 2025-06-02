#pragma once

#include "../allocator.h"

/**
 * Наивный менеджер памяти, просто обертка вокруг malloc и free.
 */
class SystemAllocator : public AbstractAllocator {
public:
    // TODO: do something with size value?
    explicit SystemAllocator(size_t size, const UtilityConfig& utilities)
        : AbstractAllocator(size, utilities){};
    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};
