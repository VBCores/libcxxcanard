#pragma once

#include <functional>
#include <type_traits>
#include <utility>

#include "cyphal/interfaces.h"
#include "libcanard/canard.h"

class CyphalInterface;

template <typename T>
struct CyphalCallbackTraits : CyphalCallbackTraits<decltype(&T::operator())> {};

template <typename R, typename Payload>
struct CyphalCallbackTraits<R (*)(const Payload&, CanardRxTransfer*)> {
    using payload_type = Payload;
};

template <typename R, typename Payload>
struct CyphalCallbackTraits<R (*)(Payload&, CanardRxTransfer*)> {
    using payload_type = Payload;
};

template <typename R, typename Class, typename Payload>
struct CyphalCallbackTraits<R (Class::*)(const Payload&, CanardRxTransfer*) const> {
    using payload_type = Payload;
};

template <typename R, typename Class, typename Payload>
struct CyphalCallbackTraits<R (Class::*)(Payload&, CanardRxTransfer*) const> {
    using payload_type = Payload;
};

template <typename R, typename Class, typename Payload>
struct CyphalCallbackTraits<R (Class::*)(const Payload&, CanardRxTransfer*)> {
    using payload_type = Payload;
};

template <typename R, typename Class, typename Payload>
struct CyphalCallbackTraits<R (Class::*)(Payload&, CanardRxTransfer*)> {
    using payload_type = Payload;
};

template <typename Payload>
struct CyphalCallbackTraits<std::function<void(const Payload&, CanardRxTransfer*)>> {
    using payload_type = Payload;
};

template <typename CyphalPayload, typename Func>
class CyphalCallbackSubscription : public IListener<CanardRxTransfer*> {
private:
    CyphalInterface& interface;
    const CanardPortID port_id;
    const CanardTransferKind kind;
    CanardRxSubscription subscription = {};
    Func callback;

public:
    CyphalCallbackSubscription(
        CyphalInterface& interface,
        CanardPortID port_id,
        CanardTransferKind kind,
        Func&& callback
    )
        : interface(interface),
          port_id(port_id),
          kind(kind),
          callback(std::forward<Func>(callback)) {
        subscription.user_reference = static_cast<void*>(this);
        interface.template subscribe<CyphalPayload>(port_id, kind, &subscription);
    }

    void accept(CanardRxTransfer* transfer) override {
        CyphalPayload object{};
        interface.deserialize_transfer<CyphalPayload>(&object, transfer);
        callback(object, transfer);
    }

    ~CyphalCallbackSubscription() override {
        interface.unsubscribe(port_id, kind);
    }
};
