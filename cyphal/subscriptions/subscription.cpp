#include "subscription.h"

template <typename T>
void AbstractSubscription<T>::subscribe() {
    CanardRxSubscription* sub = new CanardRxSubscription();
    interface->subscribe(port_id, extent, sub);
    sub->user_reference = (void*)this;
}

template <typename T>
void AbstractSubscription<T>::accept(CanardRxTransfer* transfer) {
    T object;
    deserialize(&object, transfer);
    handler(object);
}
