#pragma once

#include "cyphal/cyphal.h"
#include "cyphal/interfaces.h"
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
        interface->subscribe(
            port_id,
            extent,
            kind,
            sub
        );
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

#define DESERIALIZE_TYPE(TYPE, INTERFACE_POINTER)                        \
    inline void deserialize(TYPE* object, CanardRxTransfer* transfer) {  \
        INTERFACE_POINTER->DESERIALIZE_TRANSFER(TYPE, object, transfer); \
    }

#define SUBSCRIPTION_BODY(CLASS_NAME, TYPE, TRANSFER_KIND, PORT_ID)                        \
   private:                                                                                \
    DESERIALIZE_TYPE(TYPE, interface)                                                      \
   public:                                                                                 \
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

/*
#include "uavcan/_register/Access_1_0.h"
class MotorService : public AbstractSubscription<uavcan_register_Access_Request_1_0> {
    SUBSCRIPTION_BODY_RESPONSE(
        MotorService,
        uavcan_register_Access_Request_1_0,
        uavcan_register_Access_1_0_FIXED_PORT_ID_
    )
    void handler(const uavcan_register_Access_Request_1_0&);
};
 */