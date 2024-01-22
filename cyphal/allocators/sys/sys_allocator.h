#pragma once

#include "../allocator.h"

class SystemAllocator : public AbstractAllocator {
public:
	// TODO: do something with size value?
	explicit SystemAllocator(size_t size): AbstractAllocator(size) {};
    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};
