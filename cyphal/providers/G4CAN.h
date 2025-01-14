#pragma once
#include "cyphal/definitions.h"
#if (defined(STM32G474xx) || defined(STM32_G)) && defined(HAL_FDCAN_MODULE_ENABLED)

#include "provider.h"

#include <utility>

/**
 * Реализация для stm32g4, работает на основне SocketCAN.
 * Аргументы для конструкторов смотри в `CyphalInterface::create_bss / CyphalInterface::create_heap` (фабричные методы).
*/
class G4CAN : public AbstractCANProvider {
public:
    using Handler = FDCAN_HandleTypeDef*;

private:
    FDCAN_HandleTypeDef* handler;
    G4CAN(Handler handler, size_t queue_len, const UtilityConfig& utilities)
        : AbstractCANProvider(CANARD_MTU_CAN_FD, 72, queue_len, utilities), handler(handler){};

public:
    template <class T, typename... Args>
    static G4CAN* create_bss(
        std::byte** inout_buffer,
        Handler handler,
        CanardNodeID node_id,
        size_t queue_len,
        Args&&... args,
        const UtilityConfig& utilities
    ) {
        std::byte* allocator_loc = *inout_buffer;
        // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)
        auto allocator_ptr = new (allocator_loc) T(
            static_cast<size_t>(queue_len * sizeof(CanardTxQueueItem) * QUEUE_SIZE_MULT),
            std::forward<Args>(args)...,
            utilities
        );

        std::byte* provider_loc = allocator_loc + sizeof(T);
        auto ptr = new (provider_loc) G4CAN(handler, queue_len, utilities);
        // NOLINTEND(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)

        ptr->setup<T>(allocator_ptr, node_id);

        *inout_buffer = provider_loc + sizeof(G4CAN);
        return ptr;
    }

    template <class T, typename... Args>
    static G4CAN* create_heap(
        Handler handler,
        CanardNodeID node_id,
        size_t queue_len,
        Args&&... args,
        const UtilityConfig& utilities
    ) {
        // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)
        auto allocator_ptr = new T(
            static_cast<size_t>(queue_len * sizeof(CanardTxQueueItem) * QUEUE_SIZE_MULT),
            args...,
            utilities
        );
        auto ptr = new G4CAN(handler, queue_len, utilities);
        // NOLINTEND(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)
        ptr->setup<T>(allocator_ptr, node_id);

        return ptr;
    }

    uint32_t len_to_dlc(size_t len) override;
    size_t dlc_to_len(uint32_t dlc) override;
    void can_loop(bool no_tx=false) override;
    bool read_frame(CanardFrame* frame, void* data) override;
    int write_frame(const CanardTxQueueItem* ti) override;
};

HAL_StatusTypeDef apply_filter(G4CAN::Handler hfdcan, FDCAN_FilterTypeDef* hw_filter, const CanardFilter& filter);

#endif
