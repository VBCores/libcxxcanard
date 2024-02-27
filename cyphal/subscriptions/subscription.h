#pragma once

#include <memory>
#include "cyphal/cyphal.h"
#include "cyphal/interfaces.h"
#include "libcanard/canard.h"

// COPIED FROM LIBCANARD
// NOLINTBEGIN(cppcoreguidelines-macro-to-enum,modernize-macro-to-enum)
#define OFFSET_PRIORITY 26U
#define OFFSET_SUBJECT_ID 8U
#define OFFSET_SERVICE_ID 14U
#define OFFSET_DST_NODE_ID 7U

#define FLAG_SERVICE_NOT_MESSAGE (UINT32_C(1) << 25U)
#define FLAG_ANONYMOUS_MESSAGE (UINT32_C(1) << 24U)
#define FLAG_REQUEST_NOT_RESPONSE (UINT32_C(1) << 24U)
#define FLAG_RESERVED_23 (UINT32_C(1) << 23U)
#define FLAG_RESERVED_07 (UINT32_C(1) << 7U)
// NOLINTEND(cppcoreguidelines-macro-to-enum,modernize-macro-to-enum)

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

    void subscribe(CanardPortID port_id, CanardTransferKind kind) {
        sub.user_reference = static_cast<void*>(this);
        interface->subscribe(port_id, T::extent, kind, &sub);
    }

    virtual void handler(const Type&, CanardRxTransfer*) = 0;

public:
    // NOLINTBEGIN(modernize-pass-by-value)
    AbstractSubscription(InterfacePtr& interface, CanardPortID port_id)
        : AbstractSubscription(interface, port_id, CanardTransferKindMessage){};
    AbstractSubscription(InterfacePtr& interface, CanardPortID port_id, CanardTransferKind kind)
        : interface(interface), kind(kind) {
        subscribe(port_id, kind);
    };
    // NOLINTEND(modernize-pass-by-value)

    CanardFilter make_filter(CanardNodeID node_id) {
        CanardFilter out = {0};

        switch (kind) {
            case CanardTransferKindMessage:
                out.extended_can_id = (((uint32_t)sub.port_id) << OFFSET_SUBJECT_ID) |
                                      (((uint32_t)node_id) << OFFSET_DST_NODE_ID);
                out.extended_mask = FLAG_SERVICE_NOT_MESSAGE | FLAG_RESERVED_07 |
                                    (CANARD_SUBJECT_ID_MAX << OFFSET_SUBJECT_ID) |
                                    (CANARD_NODE_ID_MAX << OFFSET_DST_NODE_ID);
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
};
