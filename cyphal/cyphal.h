#pragma once

#include <memory>

#include "cyphal/definitions.h"
#include "providers/provider.h"

constexpr uint64_t DEFAULT_TIMEOUT_MICROS = 1000000;  // 1 sec

template <typename ObjType>
using cyphal_serializer = int8_t (*)(const ObjType* const, uint8_t* const, size_t* const);
template <typename ObjType>
using cyphal_deserializer = int8_t (*)(ObjType* const, const uint8_t*, size_t* const);

// NOLINTBEGIN(cppcoreguidelines-macro-usage)
#define TYPE_ALIAS(ALIAS_NAME, T)                                                   \
    class(ALIAS_NAME) {                                                             \
    public:                                                                         \
        typedef T Type;                                                             \
        typedef cyphal_serializer<T> serializer_type;                               \
        typedef cyphal_deserializer<T> deserializer_type;                           \
        static constexpr serializer_type serializer = T##_serialize_;               \
        static constexpr deserializer_type deserializer = T##_deserialize_;         \
        static constexpr size_t extent = T##_EXTENT_BYTES_;                         \
        static constexpr size_t buffer_size = T##_SERIALIZATION_BUFFER_SIZE_BYTES_; \
    };
// NOLINTEND(cppcoreguidelines-macro-usage)

/**
 * Main class, providing all common communication functions.
 */
class CyphalInterface {
private:
    const CanardNodeID node_id;
    UtilityConfig& utilities;
    std::unique_ptr<AbstractCANProvider> provider;

public:
    CyphalInterface(CanardNodeID node_id, UtilityConfig& config, AbstractCANProvider* provider)
        : node_id(node_id), utilities(config), provider(provider){};

    template <typename Provider, class Allocator, class... Args>
    static CyphalInterface* create_bss(
        std::byte* buffer,
        CanardNodeID node_id,
        typename Provider::Handler handler,
        size_t queue_len,
        Args&&... args,
        UtilityConfig& config
    ) {
        std::byte** inout_buffer = &buffer;
        AbstractCANProvider* provider = Provider::template create_bss<Allocator>(
            inout_buffer,
            handler,
            node_id,
            queue_len,
            std::forward<Args>(args)...,
            config
        );

        std::byte* interface_ptr = *inout_buffer;
        // NOLINTBEGIN(cppcoreguidelines-owning-memory)
        auto interface = new (interface_ptr) CyphalInterface(node_id, config, provider);
        // NOLINTEND(cppcoreguidelines-owning-memory)

        return interface;
    }
    template <typename Provider, class Allocator, class... Args>
    static std::shared_ptr<CyphalInterface> create_heap(
        CanardNodeID node_id,
        typename Provider::Handler handler,
        size_t queue_len,
        Args&&... args,
        UtilityConfig& config
    ) {
        AbstractCANProvider* provider = Provider::template create_heap<Allocator>(
            handler,
            node_id,
            queue_len,
            std::forward<Args>(args)...,
            config
        );

        return std::make_shared<CyphalInterface>(node_id, config, provider);
    }

    bool is_up() { return bool(provider); }
    size_t queue_size() { return provider->queue.size; }
    bool has_unsent_frames() {
        if (!provider) {
            return false;
        }
        return canardTxPeek(&provider->queue) != nullptr;
    }
    void process_tx_once() {  // needed for finalization of the whole program
        if (!provider) {
            return;
        }
        provider->process_canard_tx();
    }

    void loop();
    void push(
        CanardMicrosecond tx_deadline_usec,
        const CanardTransferMetadata* metadata,
        size_t payload_size,
        const void* payload
    ) const;
    void subscribe(
        CanardPortID port_id,
        size_t extent,
        CanardTransferKind kind,
        CanardRxSubscription* subscription
    ) const;

    // TEMPLATES
    template <typename TypeAlias>
    inline void send(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardPriority priority,
        CanardTransferKind transfer_kind,
        CanardNodeID to_node_id,
        uint64_t timeout_delta
    ) const;
    template <typename TypeAlias>
    inline void send_msg(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        uint64_t timeout_delta = DEFAULT_TIMEOUT_MICROS,
        CanardPriority priority = CanardPriorityNominal
    ) const;
    template <typename TypeAlias>
    inline void send_response(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardRxTransfer* transfer,
        CanardPortID port,
        uint64_t timeout_delta = DEFAULT_TIMEOUT_MICROS,
        CanardPriority priority = CanardPriorityNominal
    ) const;
    template <typename TypeAlias>
    inline void send_request(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardNodeID to_node_id,
        uint64_t timeout_delta = DEFAULT_TIMEOUT_MICROS,
        CanardPriority priority = CanardPriorityNominal
    ) const;
    template <typename TypeAlias>
    inline void deserialize_transfer(typename TypeAlias::Type* obj, CanardRxTransfer* transfer)
        const;
};

#include "cyphal.tpp"
