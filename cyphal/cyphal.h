#pragma once

#include <memory>

#include "providers/provider.h"
#include "cyphal/definitions.h"

#define DEFAULT_TIMEOUT_MICROS 1000000 // 1 sec

template <typename ObjType>
using cyphal_serializer = int8_t (*)(const ObjType* const, uint8_t* const, size_t* const);
template <typename ObjType>
using cyphal_deserializer = int8_t (*)(ObjType* const, const uint8_t*, size_t* const);

#define TYPE_ALIAS(ALIAS_NAME, T)                                               \
class ALIAS_NAME {                                                              \
public:                                                                         \
    typedef T Type;                                                             \
    typedef cyphal_serializer<T> serializer_type;                               \
    typedef cyphal_deserializer<T> deserializer_type;                           \
    static constexpr serializer_type serializer = T##_serialize_;               \
    static constexpr deserializer_type deserializer = T##_deserialize_;         \
    static constexpr size_t extent = T##_EXTENT_BYTES_;                         \
    static constexpr size_t buffer_size = T##_SERIALIZATION_BUFFER_SIZE_BYTES_; \
};

class CyphalInterface {
private:
    const CanardNodeID node_id;
    std::unique_ptr<AbstractCANProvider> provider;
    CyphalInterface(CanardNodeID node_id, UtilityConfig& config) : node_id(node_id), utilities(config) {};
    UtilityConfig& utilities;
public:
    template <typename Provider, class Allocator, class... Args> static CyphalInterface* create(
        std::byte* buffer,
        CanardNodeID node_id,
        typename Provider::Handler handler,
        size_t queue_len,
        Args&&... args,
        UtilityConfig& config
    ) {
        std::byte** inout_buffer = &buffer;
        auto provider  = std::unique_ptr<Provider>(Provider::template create<Allocator>(inout_buffer, handler, node_id, queue_len, args..., config));
    
        std::byte* interface_ptr = *inout_buffer;
        auto interface = new (interface_ptr) CyphalInterface(node_id, config);

        interface->provider = std::move(provider);
        return interface;
    }

    bool is_up() { return bool(provider); }
    size_t queue_size() { return provider->queue.size; }
    bool has_unsent_frames() {
        if (!provider)
            return false;
        return canardTxPeek(&provider->queue) != NULL;
    }
    void process_tx_once() {  // needed for finalization of the whole program
        if (!provider)
            return;
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
    inline void send_cyphal(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardPriority priority,
        CanardTransferKind transfer_kind,
        CanardNodeID to_node_id
    ) const;
    template <typename TypeAlias>
    inline void send_cyphal_default_msg(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardPortID port,
        CanardTransferID* transfer_id
    ) const;
    template <typename TypeAlias>
    inline void send_cyphal_default_msg_to(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardNodeID to_node_id
    ) const;
    template <typename TypeAlias>
    inline void send_cyphal_response(
        typename TypeAlias::Type* obj,
        uint8_t buffer[],
        CanardRxTransfer* transfer,
        CanardPortID port
    ) const;
    template <typename TypeAlias>
    inline void cyphal_deserialize_transfer (
        typename TypeAlias::Type* obj,
        CanardRxTransfer* transfer
    ) const;
};

#include "cyphal.tpp"

#define PREPARE_MESSAGE(TYPE, VAR_NAME)           \
    uint8_t VAR_NAME##_buf[TYPE##_EXTENT_BYTES_]; \
    CanardTransferID VAR_NAME##_transfer_id = 0;
