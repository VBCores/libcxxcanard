#pragma once

#include "o1heap/o1heap.h"

#include "../allocator.h"

class O1Allocator : public AbstractAllocator {
private:
    O1HeapInstance* o1heap = nullptr;
    void* memory_arena;
    void align_self(size_t size);
    bool is_self_allocated = false;

public:
    O1Allocator(size_t size, void* memory, UtilityConfig& utilities);
    explicit O1Allocator(size_t size, UtilityConfig& utilities);
    ~O1Allocator() override;

    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;

    const O1HeapInstance* const get_heap() const {
        return o1heap;
    }
};
