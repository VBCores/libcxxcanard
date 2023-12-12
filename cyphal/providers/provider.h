#pragma once

#include "cyphal/allocators/allocator.h"
#include "cyphal/definitions.h"
#include "libcanard/canard.h"

class AbstractCANProvider {
    friend class CyphalInterface;

protected:
    const size_t CANARD_MTU;
    const size_t WIRE_MTU;
    CanardTxQueue queue;
    CanardInstance canard;

public:
    typedef void Handler;

    AbstractCANProvider() = delete;
    AbstractCANProvider(size_t canard_mtu, size_t wire_mtu)
        : WIRE_MTU(wire_mtu), CANARD_MTU(canard_mtu), canard{}, queue{} {};

    template <class T, class... Args>
    void setup(CanardNodeID node_id, Args&&... args) {
        auto memory_pair = get_memory_pair<T>(args...);
        canard = canardInit(std::get<0>(memory_pair), std::get<1>(memory_pair));
        canard.node_id = node_id;
        queue = canardTxInit(200, CANARD_MTU);
    }

    virtual uint32_t len_to_dlc(size_t len) = 0;
    virtual size_t dlc_to_len(uint32_t dlc) = 0;
    virtual void can_loop() = 0;
    virtual bool read_frame(CanardFrame*)  = 0;
    virtual int write_frame(const CanardTxQueueItem* ti) = 0;
    void process_canard_rx(CanardFrame*);
    void process_canard_tx();

    virtual ~AbstractCANProvider() {
        auto allocator_obj = get_allocator();
        if (allocator_obj != nullptr) {
            delete allocator_obj;
        }
    };
};

// Time to transmit one frame + delay for 25ns bit time ~ (25*29 (ext id) + 25*64 (body)) * 1.5
#define ONE_FULL_FRAME_T 2620
// Cycles = ONE_FULL_FRAME_T / 200 * 32
#define ONE_FULL_FRAME_CYCLES 420

// 32 cycles ~~ 200 ns delay for 160Mhz core clock
__attribute__((optimize("O1"))) static inline void delay_cycles(uint16_t cycles = 32) {
    /* Reference: https://developer.arm.com/documentation/ddi0439/b/Programmers-Model/Instruction-set-summary/Cortex-M4-instructions?lang=en
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
       bxeq    lr                 // 1 такт ("Conditional branch completes in a single cycle if the branch is not taken.")
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

    uint8_t real_cycles = (cycles - 8) / 5;
    while (real_cycles--) {
        __asm__("nop");
    }
}
