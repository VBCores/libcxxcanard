#pragma once

#include "providers/provider.h"
#include "cyphal/definitions.h"

#define DEFAULT_TIMEOUT_MICROS 1000000 // 1 sec

template <typename ObjType>
using cyphal_serializer = int8_t (*)(const ObjType* const, uint8_t* const, size_t* const);
template <typename ObjType>
using cyphal_deserializer = int8_t (*)(ObjType* const, const uint8_t*, size_t* const);

class CyphalInterface {
    const CanardNodeID node_id;
    AbstractCANProvider* provider = nullptr;

public:
    CyphalInterface(CanardNodeID node_id) : node_id(node_id){};
    bool is_up() { return provider != nullptr; }
    bool has_unsent_frames() {
        if (provider == nullptr)
            return false;
        return canardTxPeek(&provider->queue) != NULL;
    }
    void process_tx_once() {  // needed for finalization of the whole program
        if (provider == nullptr)
            return;
        provider->process_canard_tx();
    }

    template <typename Provider, class Allocator, class... Args>
    void setup(typename Provider::Handler handler, Args&&... args) {
        provider = new Provider(handler);
        provider->setup<Allocator>(node_id, args...);
    }

    ~CyphalInterface() {
        delete provider;
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
    template <typename ObjType>
    inline void send_cyphal(
        ObjType* obj,
        uint8_t buf[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardPriority priority,
        CanardTransferKind transfer_kind,
        CanardNodeID to_node_id,
        unsigned long buffer_size,
        cyphal_serializer<ObjType> serializer
    ) const;
    template <typename ObjType>
    inline void send_cyphal_default_msg(
        ObjType* obj,
        uint8_t buf[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        unsigned long buffer_size,
        cyphal_serializer<ObjType> serializer
    ) const;
    template <typename ObjType>
    inline void send_cyphal_default_msg_to(
        ObjType* obj,
        uint8_t buf[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardNodeID to_node_id,
        unsigned long buffer_size,
        cyphal_serializer<ObjType> serializer
    ) const;
    template <typename ObjType>
    inline void send_cyphal_response(
        ObjType* obj,
        uint8_t buf[],
        CanardRxTransfer* transfer,
        CanardPortID port,
        unsigned long buffer_size,
        cyphal_serializer<ObjType> serializer
    ) const;
    template <typename ObjType>
    inline void cyphal_deserialize_transfer (
        ObjType* obj,
        CanardRxTransfer* transfer,
        size_t buf_size,
        cyphal_deserializer<ObjType> deserializer
    ) const;
};

#include "cyphal.tpp"

#define PREPARE_MESSAGE(TYPE, VAR_NAME)           \
    uint8_t VAR_NAME##_buf[TYPE##_EXTENT_BYTES_]; \
    CanardTransferID VAR_NAME##_transfer_id = 0;
