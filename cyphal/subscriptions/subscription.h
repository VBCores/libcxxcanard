#pragma once

#include <memory>
#include "cyphal/cyphal.h"
#include "cyphal/interfaces.h"
#include "libcanard/canard.h"

template <typename T>
class AbstractSubscription : public IListener<CanardRxTransfer*> {
protected:
    CanardRxSubscription sub = {};
    const CanardPortID port_id;
    const size_t extent;
    const CanardTransferKind kind = CanardTransferKindMessage;
    const CanardMicrosecond timeout = CANARD_DEFAULT_TRANSFER_ID_TIMEOUT_USEC;
    const std::shared_ptr<CyphalInterface> interface;

public:
    AbstractSubscription(const std::shared_ptr<CyphalInterface> interface)
        : interface(interface), port_id(0), kind(CanardTransferKindMessage), extent(0) {
        subscribe();
    };
    AbstractSubscription(const std::shared_ptr<CyphalInterface> interface, CanardPortID port_id, size_t extent)
        : interface(interface), port_id(port_id), kind(CanardTransferKindMessage), extent(extent) {
        subscribe();
    };
    AbstractSubscription(
        const std::shared_ptr<CyphalInterface> interface,
        CanardTransferKind kind,
        CanardPortID port_id,
        size_t extent
    )
        : interface(interface), port_id(port_id), kind(kind), extent(extent) {
        subscribe();
    };
    void subscribe() {
        sub.user_reference = (void*)this;
        interface->subscribe(port_id, extent, kind, &sub);
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
    CLASS_NAME(const std::shared_ptr<CyphalInterface> interface)                                                 \
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
        explicit CLASS_NAME(const std::shared_ptr<CyphalInterface> interface)                  \
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
