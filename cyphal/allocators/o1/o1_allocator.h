#pragma once

#include "o1heap/o1heap.h"

#include "../allocator.h"

class O1Allocator : public AbstractAllocator {
   private:
    O1HeapInstance* o1heap;

   public:
    explicit O1Allocator(size_t size);
    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};
