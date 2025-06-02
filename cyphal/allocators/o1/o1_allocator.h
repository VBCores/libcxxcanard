#pragma once

#include "o1heap/o1heap.h"

#include "../allocator.h"

/**
 * Обертка вокруг O1Heap. Рекомендуемый аллокатор для cyphal. Можем аллоцировать память для себя сам при создании,
 * может принять указатель на заранее выделенный участок.
 */
class O1Allocator : public AbstractAllocator {
private:
    O1HeapInstance* o1heap = nullptr;
    void* memory_arena;
    void align_self(size_t size);
    bool is_self_allocated = false;

public:
    /**
     * Создать на основе заранее выделенной памяти.
     *
     * @param size Размер буффера
     * @param memory Указатель на выделенный сегмент
     */
    O1Allocator(size_t size, void* memory, const UtilityConfig& utilities);
    /**
     * Создать аллокатор, который выдеит себя память сам.
     *
     * @param size Размер буффера
     */
    explicit O1Allocator(size_t size, const UtilityConfig& utilities);
    ~O1Allocator() override;

    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;

    [[nodiscard]] const O1HeapInstance* const get_heap() const { return o1heap; }
};
