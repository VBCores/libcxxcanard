#pragma once

#include <functional>
#include <memory>
#ifdef __linux__
#include <iostream>
#endif

#include "cyphal/allocators/allocator.h"
#include "cyphal/definitions.h"
#include "libcanard/canard.h"

extern std::unique_ptr<AbstractAllocator> _alloc_ptr;

inline void* alloc_f(CanardInstance* ins, size_t amount) {
    if (!_alloc_ptr) {
#ifdef __linux__
        std::cerr << "Tried to allocate canard memory before creating provider&allocator!"
                  << std::endl;
#endif
        exit(1);
    }
    return _alloc_ptr->allocate(ins, amount);
}
inline void free_f(CanardInstance* ins, void* pointer) {
    if (!_alloc_ptr) {
#ifdef __linux__
        std::cerr << "Tried to free (?) canard memory before creating provider&allocator!"
                  << std::endl;
#endif
        exit(1);
    }
    return _alloc_ptr->free(ins, pointer);
}

// 1 for tx, 1 for rx, 0.5 for misc (subs, multipart msgs, etc.)
constexpr float QUEUE_SIZE_MULT = 2.5F;
constexpr size_t DEFAULT_QUEUE_SIZE = 200;

/**
 * Абстрактная обертка вокруг основного функционала CAN.
 */
class AbstractCANProvider {
    friend class CyphalInterface;

protected:
    const size_t CANARD_MTU;
    const size_t WIRE_MTU;
    CanardTxQueue queue;
    CanardInstance canard;
    const UtilityConfig& utilities;

    AbstractCANProvider(size_t canard_mtu, size_t wire_mtu, const UtilityConfig& utilities)
        : AbstractCANProvider(canard_mtu, wire_mtu, DEFAULT_QUEUE_SIZE, utilities){};
    AbstractCANProvider(
        size_t canard_mtu,
        size_t wire_mtu,
        size_t queue_len,
        const UtilityConfig& utilities
    )
        : CANARD_MTU(canard_mtu),
          WIRE_MTU(wire_mtu),
          queue(canardTxInit(queue_len, CANARD_MTU)),
          utilities(utilities){};

    template <class T>
    void setup(T* ptr, CanardNodeID node_id) {
        using namespace std::placeholders;

        if (_alloc_ptr) {
#ifdef __linux__
            std::cerr << "Tried to call setup in provider twice!" << std::endl;
#endif
            utilities.error_handler();
        }
        _alloc_ptr = std::unique_ptr<T>(ptr);

        canard = canardInit(alloc_f, free_f);
        canard.node_id = node_id;
    }

    virtual void lock_canard() {};
    virtual void unlock_canard() {};
public:
    using Handler = void;

    AbstractCANProvider() = delete;
    AbstractCANProvider(const AbstractCANProvider&) = delete;
    AbstractCANProvider& operator=(const AbstractCANProvider&) = delete;
    AbstractCANProvider(AbstractCANProvider&&) = delete;
    AbstractCANProvider& operator=(AbstractCANProvider&&) = delete;

    virtual uint32_t len_to_dlc(size_t len) = 0;
    virtual size_t dlc_to_len(uint32_t dlc) = 0;
    virtual void can_loop(bool no_tx=false) = 0;
    virtual bool read_frame(CanardFrame*, void* data) = 0;
    virtual int write_frame(const CanardTxQueueItem* ti) = 0;
    void process_canard_rx(CanardFrame*);
    void process_canard_tx();
    void clear_queue();

    virtual ~AbstractCANProvider();
};

// Time to transmit one frame + delay for 25ns bit time ~ (25*29 (ext id) + 25*64 (body)) * 1.5
constexpr int ONE_FULL_FRAME_T = 2620;
// Cycles = ONE_FULL_FRAME_T / 200 * 32
constexpr int ONE_FULL_FRAME_CYCLES = 420;
// 32 cycles ~~ 200 ns delay for 160MHz core clock
constexpr int CYCLES_200NS_DELAY_DEFAULT = 32;

__attribute__((optimize("O1"))) static inline void delay_cycles(
    uint16_t cycles = CYCLES_200NS_DELAY_DEFAULT
) {
    /* Reference:
     https://developer.arm.com/documentation/ddi0439/b/Programmers-Model/Instruction-set-summary/Cortex-M4-instructions?lang=en
     *
     * // 6 тактов на (cycles - 8) / 5
       sub     r3, r0, #5         // 1 такт
       ldr     r2, .L6            // 2 такта
       smull   r1, r2, r3, r2     // 1 такт
       asr     r3, r3, #31        // 1 такт
       rsb     r3, r3, r2, asr #1 // 1 такт
     *
     * // 2 такта на стартовую проверку
       ands    r3, r3, #255       // 1 такт
       bxeq    lr                 // 1 такт ("Conditional branch completes in a single cycle if the
     branch is not taken.")
     *
     * // ~5 тактов на цикл
       .L3:
       nop                       // 1 такт
       sub     r3, r3, #1        // 1 такт
       ands    r3, r3, #255      // 1 такт
       bne     .L3               // 1 + 1-3 такта, в среднем 2(3?)
     *
     * Всего 5 тактов на цикл + 8 в начале.
     */
    constexpr uint8_t SETUP_CYCLES = 8;
    constexpr uint8_t LOOP_CYCLES = 5;

    uint8_t real_cycles = (cycles - SETUP_CYCLES) / LOOP_CYCLES;
    while (real_cycles--) {
        // NOLINTBEGIN(hicpp-no-assembler)
        __asm__("nop");
        // NOLINTEND(hicpp-no-assembler)
    }
}
