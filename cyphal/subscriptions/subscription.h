#pragma once

#include <memory>
#include <functional>

#include "cyphal/cyphal.h"
#include "cyphal/interfaces.h"
#include "libcanard/canard.h"

using InterfacePtr = const std::shared_ptr<CyphalInterface>;
using TransferListener = IListener<CanardRxTransfer*>;

/**
 * TODO
*/
template <typename T>
class AbstractSubscription : public TransferListener {
    using Type = typename T::Type;

protected:
    const CanardTransferKind kind;
    const CanardPortID port_id;
    CanardRxSubscription sub = {};
    InterfacePtr interface;

    virtual void handler(const std::shared_ptr<Type>&, CanardRxTransfer*) = 0;

public:
    // NOLINTBEGIN(modernize-pass-by-value)
    AbstractSubscription(InterfacePtr& interface, CanardPortID port_id)
        : AbstractSubscription(interface, port_id, CanardTransferKindMessage){};
    AbstractSubscription(InterfacePtr& interface, CanardPortID port_id, CanardTransferKind kind)
        : port_id(port_id), kind(kind), interface(interface) {
        sub.user_reference = static_cast<void*>(this);
        interface->subscribe<T>(port_id, kind, &sub);
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
        auto object = std::make_shared<Type>();
        interface->deserialize_transfer<T>(object.get(), transfer);
        handler(object, transfer);
    }

    virtual ~AbstractSubscription() {
        interface->unsubscribe(port_id, kind);
    };
};
