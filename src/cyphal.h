
#undef Error_Handler
#undef Error_Handler()
#define STM32_G
#define HAL_FDCAN_MODULE_ENABLED

#if defined(STM32G474xx) || defined(STM32_G)
#include "stm32g4xx_hal.h"
#include "utils.h"
#elif defined(STM32F446xx) || defined(STM32_F)
#include "stm32f4xx_hal.h"
#include "utils.h"
#else
#define CRITICAL_SECTION(code) code
#include <unistd.h>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <stdint.h>
#endif

// timestamp conversion macros
#define SEC_TO_US(sec) ((sec) * 1000000)
#define NS_TO_US(ns) ((ns) / 1000)

extern void error_handler();

#ifdef __linux__
uint64_t micros_64();
#else
extern uint64_t micros_64();
#endif

template <typename T>
class IListener {
public:
    virtual void accept(T) = 0;
};
#include <tuple>
#include <type_traits>

#include "libcanard/canard.h"

class AbstractAllocator {
public:
    virtual void* allocate(CanardInstance* ins, size_t amount) = 0;
    virtual void free(CanardInstance* ins, void* pointer) = 0;
};

extern AbstractAllocator* allocator;
inline void* allocate(CanardInstance* ins, size_t amount) {
    return allocator->allocate(ins, amount);
}
inline void free(CanardInstance* ins, void* ptr) {
    return allocator->free(ins, ptr);
}
template <class T>
std::tuple<CanardMemoryAllocate, CanardMemoryFree> get_memory_pair() {
    if (allocator != nullptr) {
        error_handler();
    }
    allocator = new T();
    return {allocate, free};
}

#include "o1heap/o1heap.h"


class O1Allocator : public AbstractAllocator {
private:
    O1HeapInstance* o1heap;
    void* memory_arena;

public:
    explicit O1Allocator(size_t size);
    O1Allocator() : O1Allocator(200*64){};
    ~O1Allocator();

    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};


class SystemAllocator : public AbstractAllocator {
public:
    void* allocate(CanardInstance* ins, size_t amount) override;
    void free(CanardInstance* ins, void* pointer) override;
};

#include <cstdint>

extern const uint32_t CanardFDCANLengthToDLC[65];
extern size_t fdcan_dlc_to_len(uint32_t);

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
    template <class T>
    void setup(CanardNodeID node_id) {
        auto memory_pair = get_memory_pair<T>();
        canard = canardInit(std::get<0>(memory_pair), std::get<1>(memory_pair));
        canard.node_id = node_id;
        queue = canardTxInit(200, CANARD_MTU);
    }

    virtual uint32_t len_to_dlc(size_t len) = 0;
    virtual size_t dlc_to_len(uint32_t dlc) = 0;
    virtual void can_loop() = 0;
    virtual CanardFrame* read_frame() = 0;
    virtual int write_frame(const CanardTxQueueItem* ti) = 0;
    void process_canard_rx(CanardFrame*);
    void process_canard_tx();
};
#if (defined(STM32G474xx) || defined(STM32_G)) && defined(HAL_FDCAN_MODULE_ENABLED)


class G4CAN : public AbstractCANProvider {
private:
    FDCAN_HandleTypeDef* handler;

public:
    typedef FDCAN_HandleTypeDef* Handler;
    G4CAN(Handler handler) : AbstractCANProvider(CANARD_MTU_CAN_FD, 72), handler(handler){};
    uint32_t len_to_dlc(size_t len) override;
    size_t dlc_to_len(uint32_t dlc) override;
    void can_loop() override;
    CanardFrame* read_frame() override;
    int write_frame(const CanardTxQueueItem* ti) override;
};

#endif

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
    void process_tx_once() {  // needed for finalization of the whole programm
        if (provider == nullptr)
            return;
        provider->process_canard_tx();
    }
    template <typename Provider, class Allocator>
    void setup(typename Provider::Handler handler) {
        provider = new Provider(handler);
        provider->setup<Allocator>(node_id);
    }
    void loop();
    void push(
        CanardMicrosecond tx_deadline_usec,
        const CanardTransferMetadata* metadata,
        size_t payload_size,
        const void* payload
    );
    void subscribe(
        CanardPortID port_id,
        size_t extent,
        CanardTransferKind kind,
        CanardRxSubscription* subscription
    );

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
    );
    template <typename ObjType>
    inline void send_cyphal_default_msg(
        ObjType* obj,
        uint8_t buf[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        unsigned long buffer_size,
        cyphal_serializer<ObjType> serializer
    );
    template <typename ObjType>
    inline void send_cyphal_default_msg_to(
        ObjType* obj,
        uint8_t buf[],
        CanardPortID port,
        CanardTransferID* transfer_id,
        CanardNodeID to_node_id,
        unsigned long buffer_size,
        cyphal_serializer<ObjType> serializer
    );
    template <typename ObjType>
    inline void send_cyphal_response(
        ObjType* obj,
        uint8_t buf[],
        CanardRxTransfer* transfer,
        CanardPortID port,
        unsigned long buffer_size,
        cyphal_serializer<ObjType> serializer
    );
    template <typename ObjType>
    inline void cyphal_deserialize_transfer(
        ObjType* obj,
        CanardRxTransfer* transfer,
        size_t buf_size,
        cyphal_deserializer<ObjType> deserializer
    );
};


#define PREPARE_MESSAGE(TYPE, VAR_NAME)           \
    uint8_t VAR_NAME##_buf[TYPE##_EXTENT_BYTES_]; \
    CanardTransferID VAR_NAME##_transfer_id = 0;
template <typename ObjType>
inline void CyphalInterface::send_cyphal(
    ObjType *obj,
    uint8_t buf[],
    CanardPortID port,
    CanardTransferID *transfer_id,
    CanardPriority priority,
    CanardTransferKind transfer_kind,
    CanardNodeID to_node_id,
    unsigned long buffer_size,
    cyphal_serializer<ObjType> serializer
) {
    size_t cyphal_buf_size = buffer_size;
    if (serializer(obj, buf, &cyphal_buf_size) < 0) {
        error_handler();
    }
    const CanardTransferMetadata cyphal_transfer_metadata = {
        .priority = priority,
        .transfer_kind = transfer_kind,
        .port_id = port,
        .remote_node_id = to_node_id,
        .transfer_id = *transfer_id,
    };
    push(
        micros_64() + DEFAULT_TIMEOUT_MICROS,
        &cyphal_transfer_metadata,
        cyphal_buf_size,
        buf
    );
    (*transfer_id)++;
}
#define SEND_TRANSFER(TYPE, obj, buf, port, transfer_id, priority, transfer_kind, dest_id) \
send_cyphal<TYPE>(obj, buf, port, transfer_id, priority, transfer_kind, dest_id, TYPE##_SERIALIZATION_BUFFER_SIZE_BYTES_, TYPE##_serialize_)

template <typename ObjType>
inline void CyphalInterface::send_cyphal_default_msg(
    ObjType *obj,
    uint8_t buf[],
    CanardPortID port,
    CanardTransferID *transfer_id,
    unsigned long buffer_size,
    cyphal_serializer<ObjType> serializer
) {
    send_cyphal<ObjType>(
        obj,
        buf,
        port,
        transfer_id,
        CanardPriorityNominal,
        CanardTransferKindMessage,
        CANARD_NODE_ID_UNSET,
        buffer_size,
        serializer
    );
}
#define SEND_MSG(TYPE, obj, buf, port, transfer_id) \
send_cyphal_default_msg<TYPE>(obj, buf, port, transfer_id, TYPE##_SERIALIZATION_BUFFER_SIZE_BYTES_, TYPE##_serialize_)

template <typename ObjType>
inline void CyphalInterface::send_cyphal_default_msg_to(
    ObjType *obj,
    uint8_t buf[],
    CanardPortID port,
    CanardTransferID *transfer_id,
    CanardNodeID to_node_id,
    unsigned long buffer_size,
    cyphal_serializer<ObjType> serializer
) {
    send_cyphal<ObjType>(
        obj,
        buf,
        port,
        transfer_id,
        CanardPriorityNominal,
        CanardTransferKindMessage,
        to_node_id,
        buffer_size,
        serializer
    );
}
#define SEND_MSG_TO(TYPE, obj, buf, port, transfer_id, dest_id) \
send_cyphal_default_msg_to<TYPE>(obj, buf, port, transfer_id, dest_id, TYPE##_SERIALIZATION_BUFFER_SIZE_BYTES_, TYPE##_serialize_)

template <typename ObjType>
inline void CyphalInterface::send_cyphal_response(
    ObjType *obj,
    uint8_t buf[],
    CanardRxTransfer *transfer,
    CanardPortID port,
    unsigned long buffer_size,
    cyphal_serializer<ObjType> serializer
) {
    size_t cyphal_buf_size = buffer_size;
    if (serializer(obj, buf, &cyphal_buf_size) < 0) {
        error_handler();
    }
    const CanardTransferMetadata cyphal_transfer_metadata = {
            .priority = CanardPriorityNominal,
            .transfer_kind = CanardTransferKindResponse,
            .port_id = port,
            .remote_node_id = transfer->metadata.remote_node_id,
            .transfer_id = transfer->metadata.transfer_id,
    };
    push(
        DEFAULT_TIMEOUT_MICROS,
        &cyphal_transfer_metadata,
        cyphal_buf_size,
        buf
    );
}
#define SEND_RESPONSE(TYPE, obj, buf, transfer, port) \
send_cyphal_response<TYPE>(obj, buf, transfer, port, TYPE##_SERIALIZATION_BUFFER_SIZE_BYTES_, TYPE##_serialize_)

template <typename ObjType>
inline void CyphalInterface::cyphal_deserialize_transfer(
    ObjType *obj,
    CanardRxTransfer* transfer,
    size_t buf_size,
    cyphal_deserializer<ObjType> deserializer
) {
    size_t inout_buf_size = buf_size;
    if( deserializer(obj,(uint8_t *) transfer->payload, &inout_buf_size) < 0 ) {
        error_handler();
    }
}
#define DESERIALIZE_TRANSFER(TYPE, obj, transfer) \
cyphal_deserialize_transfer<TYPE>(obj, transfer, TYPE##_EXTENT_BYTES_, TYPE##_deserialize_)

#include "libcanard/canard.h"

template <typename T>
class AbstractSubscription : public IListener<CanardRxTransfer*> {
protected:
    const CanardPortID port_id;
    const size_t extent;
    const CanardTransferKind kind = CanardTransferKindMessage;
    const CanardMicrosecond timeout = CANARD_DEFAULT_TRANSFER_ID_TIMEOUT_USEC;
    CyphalInterface* interface;

public:
    AbstractSubscription(CyphalInterface* interface)
        : interface(interface), port_id(0), kind(CanardTransferKindMessage), extent(0) {
        subscribe();
    };
    AbstractSubscription(CyphalInterface* interface, CanardPortID port_id, size_t extent)
        : interface(interface), port_id(port_id), kind(CanardTransferKindMessage), extent(extent) {
        subscribe();
    };
    AbstractSubscription(
        CyphalInterface* interface,
        CanardTransferKind kind,
        CanardPortID port_id,
        size_t extent
    )
        : interface(interface), port_id(port_id), kind(kind), extent(extent) {
        subscribe();
    };
    virtual void subscribe() {
        CanardRxSubscription* sub = new CanardRxSubscription();
        sub->user_reference = (void*)this;
        interface->subscribe(port_id, extent, kind, sub);
    }
    virtual void accept(CanardRxTransfer* transfer) {
        T object;
        deserialize(&object, transfer);
        handler(object, transfer);
    }
    virtual void deserialize(T*, CanardRxTransfer*) = 0;
    virtual void handler(const T&, CanardRxTransfer*) = 0;
};

/*
 * Все макросы, заданные далее, могут упростить написание типового кода,
 * но усложнить дебаг если вам нужно делать что-то сложное с сообщениями.
 * Если макросы вам мешают - просто не используйте их.
 */

#define DESERIALIZE_TYPE(TYPE, INTERFACE_POINTER)                                \
    inline void deserialize(TYPE* object, CanardRxTransfer* transfer) override { \
        INTERFACE_POINTER->DESERIALIZE_TRANSFER(TYPE, object, transfer);         \
    }

#define SUBSCRIPTION_BODY(CLASS_NAME, TYPE, TRANSFER_KIND, PORT_ID)                        \
private:                                                                                   \
    DESERIALIZE_TYPE(TYPE, interface)                                                      \
public:                                                                                    \
    CLASS_NAME(CyphalInterface* interface)                                                 \
        : AbstractSubscription(interface, TRANSFER_KIND, PORT_ID, TYPE##_EXTENT_BYTES_){}; \
                                                                                           \
private:

#define SUBSCRIPTION_BODY_FIXED(CLASS_NAME, TYPE, TRANSFER_KIND) \
    SUBSCRIPTION_BODY(CLASS_NAME, TYPE, TRANSFER_KIND, TYPE##_FIXED_PORT_ID_)

#define SUBSCRIPTION_BODY_RESPONSE(CLASS_NAME, TYPE, PORT_ID) \
    SUBSCRIPTION_BODY(CLASS_NAME, TYPE, CanardTransferKindResponse, PORT_ID)

#define SUBSCRIPTION_BODY_MESSAGE(CLASS_NAME, TYPE, PORT_ID) \
    SUBSCRIPTION_BODY(CLASS_NAME, TYPE, CanardTransferKindMessage, PORT_ID)

#define SUBSCRIPTION_BODY_FIXED_RESPONSE(CLASS_NAME, TYPE) \
    SUBSCRIPTION_BODY_RESPONSE(CLASS_NAME, TYPE, TYPE##_FIXED_PORT_ID_)

#define SUBSCRIPTION_BODY_FIXED_MESSAGE(CLASS_NAME, TYPE) \
    SUBSCRIPTION_BODY_MESSAGE(CLASS_NAME, TYPE, TYPE##_FIXED_PORT_ID_)

#define SUBSCRIPTION_CLASS(CLASS_NAME, TYPE, TRANSFER_KIND, PORT_ID)                           \
    class CLASS_NAME : public AbstractSubscription<TYPE> {                                     \
    private:                                                                                   \
        DESERIALIZE_TYPE(TYPE, interface)                                                      \
    public:                                                                                    \
        explicit CLASS_NAME(CyphalInterface* interface)                                        \
            : AbstractSubscription(interface, TRANSFER_KIND, PORT_ID, TYPE##_EXTENT_BYTES_){}; \
                                                                                               \
    public:                                                                                    \
        void handler(const TYPE& object, CanardRxTransfer* transfer) override;                 \
    };

#define SUBSCRIPTION_CLASS_FIXED(CLASS_NAME, TYPE, TRANSFER_KIND) \
    SUBSCRIPTION_CLASS(CLASS_NAME, TYPE, TRANSFER_KIND, TYPE##_FIXED_PORT_ID_)

#define SUBSCRIPTION_CLASS_REQUEST(CLASS_NAME, TYPE, PORT_ID) \
    SUBSCRIPTION_CLASS(CLASS_NAME, TYPE, CanardTransferKindRequest, PORT_ID)

#define SUBSCRIPTION_CLASS_MESSAGE(CLASS_NAME, TYPE, PORT_ID) \
    SUBSCRIPTION_CLASS(CLASS_NAME, TYPE, CanardTransferKindMessage, PORT_ID)

#define SUBSCRIPTION_CLASS_FIXED_RESPONSE(CLASS_NAME, TYPE) \
    SUBSCRIPTION_CLASS_RESPONSE(CLASS_NAME, TYPE, TYPE##_FIXED_PORT_ID_)

#define SUBSCRIPTION_CLASS_FIXED_MESSAGE(CLASS_NAME, TYPE) \
    SUBSCRIPTION_CLASS_MESSAGE(CLASS_NAME, TYPE, TYPE##_FIXED_PORT_ID_)
