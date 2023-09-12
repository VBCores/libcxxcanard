#pragma once

#include "../allocator.h"

class SystemAllocator : public AbstractAllocator {
public:
    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};
