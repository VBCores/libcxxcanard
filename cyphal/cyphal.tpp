template <typename CyphalPayload>
inline void CyphalInterface::send(
    CyphalPayload* obj,
    CanardPortID port,
    CanardTransferID* transfer_id,
    CanardPriority priority,
    CanardTransferKind transfer_kind,
    CanardNodeID to_node_id,
    uint64_t timeout_delta
) const {
    using TypeInfo = CyphalTypeTraits<CyphalPayload>;
    uint8_t buffer[TypeInfo::buffer_size];
    size_t cyphal_buf_size = TypeInfo::buffer_size;
    if (TypeInfo::serializer(obj, buffer, &cyphal_buf_size) < 0) {
        utilities.error_handler();
    }

    const CanardTransferMetadata cyphal_transfer_metadata = {
        .priority = priority,
        .transfer_kind = transfer_kind,
        .port_id = port,
        .remote_node_id = to_node_id,
        .transfer_id = *transfer_id,
    };
    push(
        utilities.micros_64() + timeout_delta,
        &cyphal_transfer_metadata,
        cyphal_buf_size,
        buffer
    );
    (*transfer_id)++;
}

template <typename ObjType>
inline void CyphalInterface::send_msg(
    ObjType* obj,
    CanardPortID port,
    CanardTransferID* transfer_id,
    uint64_t timeout_delta,
    CanardPriority priority
) const {
    send<ObjType>(
        obj,
        port,
        transfer_id,
        priority,
        CanardTransferKindMessage,
        CANARD_NODE_ID_UNSET,
        timeout_delta
    );
}

template <typename ObjType>
inline void CyphalInterface::send_response(
    ObjType* obj,
    CanardRxTransfer* transfer,
    uint64_t timeout_delta
) const {
    using TypeInfo = CyphalTypeTraits<ObjType>;
    uint8_t buffer[TypeInfo::buffer_size];
    size_t cyphal_buf_size = TypeInfo::buffer_size;
    if (TypeInfo::serializer(obj, buffer, &cyphal_buf_size) < 0) {
        utilities.error_handler();
    }

    const CanardTransferMetadata cyphal_transfer_metadata = {
        .priority = transfer->metadata.priority,
        .transfer_kind = CanardTransferKindResponse,
        .port_id = transfer->metadata.port_id,
        .remote_node_id = transfer->metadata.remote_node_id,
        .transfer_id = transfer->metadata.transfer_id,
    };
    push(
        utilities.micros_64() + timeout_delta,
        &cyphal_transfer_metadata,
        cyphal_buf_size,
        buffer
    );
}

template <typename ObjType>
inline void CyphalInterface::send_request(
    ObjType* obj,
    CanardPortID port,
    CanardTransferID* transfer_id,
    CanardNodeID to_node_id,
    uint64_t timeout_delta,
    CanardPriority priority
) const {
    send<ObjType>(
        obj,
        port,
        transfer_id,
        priority,
        CanardTransferKindRequest,
        to_node_id,
        timeout_delta
    );
}

template <typename CyphalPayload>
inline void CyphalInterface::deserialize_transfer(
    CyphalPayload* obj,
    CanardRxTransfer* transfer
) const {
    using TypeInfo = CyphalTypeTraits<CyphalPayload>;
    size_t inout_buf_size = TypeInfo::extent;
    if (TypeInfo::deserializer(obj, static_cast<uint8_t*>(transfer->payload), &inout_buf_size) < 0) {
        utilities.error_handler();
    }
}

template <typename CyphalPayload>
inline void CyphalInterface::subscribe(
    CanardPortID port_id,
    CanardTransferKind kind,
    CanardRxSubscription* subscription
) {
    using TypeInfo = CyphalTypeTraits<CyphalPayload>;
    if (canardRxSubscribe(
            (CanardInstance* const)&provider->canard,
            kind,
            port_id,
            TypeInfo::extent,
            CANARD_DEFAULT_TRANSFER_ID_TIMEOUT_USEC,
            subscription
        ) != 1) {
        utilities.error_handler();
    }
}
