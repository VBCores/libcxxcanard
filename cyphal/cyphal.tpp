template <typename TypeAlias>
inline void CyphalInterface::send(
    typename TypeAlias::Type* obj,
    uint8_t buffer[],
    CanardPortID port,
    CanardTransferID *transfer_id,
    CanardPriority priority,
    CanardTransferKind transfer_kind,
    CanardNodeID to_node_id,
    uint64_t timeout_delta
) const {
    size_t cyphal_buf_size = TypeAlias::buffer_size;
    if (TypeAlias::serializer(obj, buffer, &cyphal_buf_size) < 0) {
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

template <typename TypeAlias>
inline void CyphalInterface::send_msg(
    typename TypeAlias::Type *obj,
    uint8_t buffer[],
    CanardPortID port,
    CanardTransferID *transfer_id,
    uint64_t timeout_delta,
    CanardPriority priority
) const {
    send<TypeAlias>(
        obj,
        buffer,
        port,
        transfer_id,
        priority,
        CanardTransferKindMessage,
        CANARD_NODE_ID_UNSET,
        timeout_delta
    );
}

template <typename TypeAlias>
inline void CyphalInterface::send_response(
    typename TypeAlias::Type *obj,
    uint8_t buffer[],
    CanardRxTransfer *transfer,
    CanardPortID port,
    uint64_t timeout_delta,
    CanardPriority priority
) const {
    size_t cyphal_buf_size = TypeAlias::buffer_size;
    if (TypeAlias::serializer(obj, buffer, &cyphal_buf_size) < 0) {
        utilities.error_handler();
    }
    const CanardTransferMetadata cyphal_transfer_metadata = {
            .priority = priority,
            .transfer_kind = CanardTransferKindResponse,
            .port_id = port,
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

template <typename TypeAlias>
inline void CyphalInterface::send_request(
    typename TypeAlias::Type* obj,
    uint8_t buffer[],
    CanardPortID port,
    CanardTransferID* transfer_id,
    CanardNodeID to_node_id,
    uint64_t timeout_delta,
    CanardPriority priority
) const {
    send<TypeAlias>(
        obj,
        buffer,
        port,
        transfer_id,
        priority,
        CanardTransferKindRequest,
        to_node_id,
        timeout_delta
    );
}

template <typename TypeAlias>
inline void CyphalInterface::deserialize_transfer(
    typename TypeAlias::Type *obj,
    CanardRxTransfer* transfer
) const {
    size_t inout_buf_size = TypeAlias::extent;
    if(TypeAlias::deserializer(obj, (uint8_t *) transfer->payload, &inout_buf_size) < 0 ) {
        utilities.error_handler();
    }
}
