#pragma once

#include <optional>
#include <functional>

#include <cyphal/node/registers_handler.hpp>
#include <cyphal/node/registers_utils.hpp>

class RegistersProxy: public AbstractSubscription<RegisterAccessResponse> {
private:
    const CanardNodeID target_node_id;
    CanardTransferID register_access_transfer_id = 0;

    template <typename T>
    void request_generic(const std::string& name, std::optional<T> value, void(*filler)(uavcan_register_Value_1_0&, T)) {
        RegisterAccessRequest::Type request {0};
        size_t name_size = std::min(name.size(), size_t{255});
        memcpy(request.name.name.elements, name.c_str(), name_size);
        request.name.name.count = name_size;
        if (value) {
            filler(request.value, *value);
        }
        else {
            request.value._tag_ = REGISTER_EMPTY_TAG;
        }
        send_access_request(&request);
    }
public:
    RegistersProxy(
        InterfacePtr interface,
        CanardNodeID target_node_id
    ) :
        AbstractSubscription<RegisterAccessResponse>(
            interface,
            uavcan_register_Access_1_0_FIXED_PORT_ID_,
            CanardTransferKindResponse
        ),
        target_node_id(target_node_id)
    {}

    void send_access_request(RegisterAccessRequest::Type* request) {
        interface->send_request<RegisterAccessRequest>(
            request,
            uavcan_register_Access_1_0_FIXED_PORT_ID_,
            &register_access_transfer_id,
            target_node_id
        );
    }

    void request_real32_value(const std::string& name, std::optional<float> value) {
        request_generic<float>(name, value, &fill_register_real32);
    }

    void request_natural32_value(const std::string& name, std::optional<uint32_t> value) {
        request_generic<uint32_t>(name, value, &fill_register_natural32);
    }

    void handler(const RegisterAccessResponse::Type& register_response, CanardRxTransfer* transfer) override {
        if (transfer->metadata.remote_node_id != target_node_id) {
            return;
        }
        switch (register_response.value._tag_) {
            case REGISTER_REAL32_TAG:
                handle_float32(register_response.value.real32.value.elements[0], transfer);
                break;
            case REGISTER_NATURAL32_TAG:
                handle_natural32(register_response.value.natural32.value.elements[0], transfer);
                break;
            default:
                break;
        }
    };

    virtual void handle_float32(float value, CanardRxTransfer* transfer) = 0;
    virtual void handle_natural32(uint32_t value, CanardRxTransfer* transfer) = 0;
};
