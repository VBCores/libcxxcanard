#pragma once

#include <memory>
#include <functional>

#include "cyphal/cyphal.h"
#include "cyphal/interfaces.h"
#include "libcanard/canard.h"

using InterfacePtr = const std::shared_ptr<CyphalInterface>;
using TransferListener = IListener<CanardRxTransfer*>;

class IHasFilter {
public:
    virtual CanardFilter make_filter(CanardNodeID node_id) = 0;
    virtual ~IHasFilter() = default;
};

/**
 * TODO docs
*/
template <typename T>
class AbstractSubscription : public TransferListener, public IHasFilter {
    using Type = typename T::Type;

protected:
    const CanardPortID port_id;
    const CanardTransferKind kind;
    InterfacePtr interface;
    CanardRxSubscription sub = {};

    virtual void handler(const Type&, CanardRxTransfer*) = 0;

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

    CanardFilter make_filter(CanardNodeID node_id) override{
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
        // NOTE: I would like to NOT initialize this object to save cpu cycles
        //       but whatever else I do triggers a compiler warning -Wmaybe-uninitialized.
        //       Its somehow related to flto step? Since it appears at linking step after flto logs,
        //       even with "GNU push ignore warning" pragmas. Weird stuff.
        Type object{};
        interface->deserialize_transfer<T>(&object, transfer);
        handler(object, transfer);
    }

    virtual ~AbstractSubscription() {
        interface->unsubscribe(port_id, kind);
    };
};
