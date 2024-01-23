#pragma once

#include <memory>
#include "cyphal/cyphal.h"
#include "cyphal/interfaces.h"
#include "libcanard/canard.h"

typedef const std::shared_ptr<CyphalInterface> InterfacePtr;

template <typename T>
class AbstractSubscription : public IListener<CanardRxTransfer*> {
    typedef typename T::Type Type;
protected:
    CanardRxSubscription sub = {};
    InterfacePtr interface;

    void subscribe(CanardPortID port_id, CanardTransferKind kind) {
        sub.user_reference = reinterpret_cast<void*>(this);
        interface->subscribe(port_id, T::extent, kind, &sub);
    }

    virtual void handler(const Type&, CanardRxTransfer*) = 0;
public:
    AbstractSubscription(InterfacePtr interface, CanardPortID port_id)
        : AbstractSubscription(interface, port_id, CanardTransferKindMessage) {};
    AbstractSubscription(
        InterfacePtr interface,
        CanardPortID port_id,
        CanardTransferKind kind
    ): interface(interface) {
        subscribe(port_id, kind);
    };

    void accept(CanardRxTransfer* transfer) {
        Type object;
        interface->cyphal_deserialize_transfer<T>(&object, transfer);
        handler(object, transfer);
    }
};
