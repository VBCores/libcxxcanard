#pragma once

#include "o1heap/o1heap.h"

#include "../allocator.h"

class O1Allocator : public AbstractAllocator {
private:
    O1HeapInstance* o1heap;
    void* memory_arena;
    void align_self(size_t size);
    bool is_self_allocated = false;
public:
    O1Allocator(void* memory, size_t size);
    explicit O1Allocator(size_t size);
    O1Allocator() : O1Allocator(200*72){};
    ~O1Allocator();

    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};
