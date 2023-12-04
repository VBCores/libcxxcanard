template <typename ObjType>
inline void CyphalInterface::send_cyphal(
    ObjType *obj,
    uint8_t buf[],
    CanardPortID port,
    CanardTransferID *transfer_id,
    CanardPriority priority,
    CanardTransferKind transfer_kind,
    CanardNodeID to_node_id,
    unsigned long buffer_size,
    cyphal_serializer<ObjType> serializer
) const {
    size_t cyphal_buf_size = buffer_size;
    if (serializer(obj, buf, &cyphal_buf_size) < 0) {
        error_handler();
    }
    const CanardTransferMetadata cyphal_transfer_metadata = {
        .priority = priority,
        .transfer_kind = transfer_kind,
        .port_id = port,
        .remote_node_id = to_node_id,
        .transfer_id = *transfer_id,
    };
    push(
        micros_64() + DEFAULT_TIMEOUT_MICROS,
        &cyphal_transfer_metadata,
        cyphal_buf_size,
        buf
    );
    (*transfer_id)++;
}
#define SEND_TRANSFER(TYPE, obj, buf, port, transfer_id, priority, transfer_kind, dest_id) \
send_cyphal<TYPE>(obj, buf, port, transfer_id, priority, transfer_kind, dest_id, TYPE##_SERIALIZATION_BUFFER_SIZE_BYTES_, TYPE##_serialize_)

template <typename ObjType>
inline void CyphalInterface::send_cyphal_default_msg(
    ObjType *obj,
    uint8_t buf[],
    CanardPortID port,
    CanardTransferID *transfer_id,
    unsigned long buffer_size,
    cyphal_serializer<ObjType> serializer
) const {
    send_cyphal<ObjType>(
        obj,
        buf,
        port,
        transfer_id,
        CanardPriorityNominal,
        CanardTransferKindMessage,
        CANARD_NODE_ID_UNSET,
        buffer_size,
        serializer
    );
}
#define SEND_MSG(TYPE, obj, buf, port, transfer_id) \
send_cyphal_default_msg<TYPE>(obj, buf, port, transfer_id, TYPE##_SERIALIZATION_BUFFER_SIZE_BYTES_, TYPE##_serialize_)

template <typename ObjType>
inline void CyphalInterface::send_cyphal_default_msg_to(
    ObjType *obj,
    uint8_t buf[],
    CanardPortID port,
    CanardTransferID *transfer_id,
    CanardNodeID to_node_id,
    unsigned long buffer_size,
    cyphal_serializer<ObjType> serializer
) const {
    send_cyphal<ObjType>(
        obj,
        buf,
        port,
        transfer_id,
        CanardPriorityNominal,
        CanardTransferKindMessage,
        to_node_id,
        buffer_size,
        serializer
    );
}
#define SEND_MSG_TO(TYPE, obj, buf, port, transfer_id, dest_id) \
send_cyphal_default_msg_to<TYPE>(obj, buf, port, transfer_id, dest_id, TYPE##_SERIALIZATION_BUFFER_SIZE_BYTES_, TYPE##_serialize_)

template <typename ObjType>
inline void CyphalInterface::send_cyphal_response(
    ObjType *obj,
    uint8_t buf[],
    CanardRxTransfer *transfer,
    CanardPortID port,
    unsigned long buffer_size,
    cyphal_serializer<ObjType> serializer
) const {
    size_t cyphal_buf_size = buffer_size;
    if (serializer(obj, buf, &cyphal_buf_size) < 0) {
        error_handler();
    }
    const CanardTransferMetadata cyphal_transfer_metadata = {
            .priority = CanardPriorityNominal,
            .transfer_kind = CanardTransferKindResponse,
            .port_id = port,
            .remote_node_id = transfer->metadata.remote_node_id,
            .transfer_id = transfer->metadata.transfer_id,
    };
    push(
        DEFAULT_TIMEOUT_MICROS,
        &cyphal_transfer_metadata,
        cyphal_buf_size,
        buf
    );
}
#define SEND_RESPONSE(TYPE, obj, buf, transfer, port) \
send_cyphal_response<TYPE>(obj, buf, transfer, port, TYPE##_SERIALIZATION_BUFFER_SIZE_BYTES_, TYPE##_serialize_)

template <typename ObjType>
inline void CyphalInterface::cyphal_deserialize_transfer(
    ObjType *obj,
    CanardRxTransfer* transfer,
    size_t buf_size,
    cyphal_deserializer<ObjType> deserializer
) const {
    size_t inout_buf_size = buf_size;
    if( deserializer(obj,(uint8_t *) transfer->payload, &inout_buf_size) < 0 ) {
        error_handler();
    }
}
#define DESERIALIZE_TRANSFER(TYPE, obj, transfer) \
cyphal_deserialize_transfer<TYPE>(obj, transfer, TYPE##_EXTENT_BYTES_, TYPE##_deserialize_)
