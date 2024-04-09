#pragma once

#include <memory>
#include "cyphal/cyphal.h"
#include "cyphal/interfaces.h"
#include "libcanard/canard.h"

using InterfacePtr = const std::shared_ptr<CyphalInterface>;

/**
 * TODO
*/
template <typename T>
class AbstractSubscription : public IListener<CanardRxTransfer*> {
    using Type = typename T::Type;

protected:
    const CanardTransferKind kind;
    CanardRxSubscription sub = {};
    InterfacePtr interface;

    void subscribe(CanardPortID port_id) {
        sub.user_reference = static_cast<void*>(this);
        interface->subscribe(port_id, T::extent, kind, &sub);
    }

    virtual void handler(const Type&, CanardRxTransfer*) = 0;

public:
    // NOLINTBEGIN(modernize-pass-by-value)
    AbstractSubscription(InterfacePtr& interface, CanardPortID port_id)
        : AbstractSubscription(interface, port_id, CanardTransferKindMessage){};
    AbstractSubscription(InterfacePtr& interface, CanardPortID port_id, CanardTransferKind kind)
        : kind(kind), interface(interface) {
        subscribe(port_id);
    };
    // NOLINTEND(modernize-pass-by-value)

    virtual CanardFilter make_filter(CanardNodeID node_id) {
        CanardFilter out = {};

        switch (kind) {
            case CanardTransferKindMessage:
                out = canardMakeFilterForSubject(sub.port_id);
                break;
            case CanardTransferKindRequest:
            case CanardTransferKindResponse:
                out = canardMakeFilterForService(sub.port_id, node_id);
                break;
        }

        return out;
    }
    void accept(CanardRxTransfer* transfer) override {
        Type object;
        interface->deserialize_transfer<T>(&object, transfer);
        handler(object, transfer);
    }

    virtual ~AbstractSubscription() {};
};
