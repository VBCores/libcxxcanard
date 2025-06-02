#pragma once
#include "cyphal/definitions.h"
#ifdef __linux__

#include "provider.h"
#include "poll.h"

#include <string>
#include <utility>
#include <mutex>

/**
 * Реализация для linux, работает на основне SocketCAN.
 * Аргументы для конструкторов смотри в `CyphalInterface::create_bss / CyphalInterface::create_heap` (фабричные методы).
*/
class LinuxCAN : public AbstractCANProvider {
public:
    using Handler = const std::string&;

private:
    std::mutex canard_mutex;
    int socketcan_handler;
    pollfd can_pollfd;
    LinuxCAN(Handler can_interface, size_t queue_len, const UtilityConfig& utilities);
protected:
    void lock_canard() override;
    void unlock_canard() override;
public:
    template <class T, typename... Args>
    static LinuxCAN* create_bss(
        std::byte** inout_buffer,
        Handler handler,
        CanardNodeID node_id,
        size_t queue_len,
        Args&&... args,
        const UtilityConfig& utilities
    ) {
        std::byte* allocator_loc = *inout_buffer;
        // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)
        auto allocator_ptr = new (allocator_loc)
            T(static_cast<size_t>(queue_len * sizeof(CanardTxQueueItem) * QUEUE_SIZE_MULT),
              std::forward<Args>(args)...,
              utilities);

        std::byte* provider_loc = allocator_loc + sizeof(T);
        auto ptr = new (provider_loc) LinuxCAN(handler, queue_len, utilities);
        ptr->setup<T>(allocator_ptr, node_id);

        *inout_buffer = provider_loc + sizeof(LinuxCAN);
        // NOLINTEND(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)
        return ptr;
    }

    template <class T, typename... Args>
    static LinuxCAN* create_heap(
        Handler handler,
        CanardNodeID node_id,
        size_t queue_len,
        Args&&... args,
        const UtilityConfig& utilities
    ) {
        // NOLINTBEGIN(cppcoreguidelines-owning-memory,cppcoreguidelines-pro-bounds-pointer-arithmetic,bugprone-narrowing-conversions,cppcoreguidelines-narrowing-conversions)
        auto allocator_ptr = new T(
            static_cast<size_t>(queue_len * sizeof(CanardTxQueueItem) * QUEUE_SIZE_MULT),
            std::forward<Args>(args)...,
            utilities
        );
        auto ptr = new LinuxCAN(handler, queue_len, utilities);
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
#endif
