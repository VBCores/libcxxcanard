#pragma once

#include <optional>
#include <functional>
#include <tuple>
#include <map>

#include <cyphal/node/registers_handler.hpp>
#include <cyphal/node/registers_utils.hpp>

class RegistersProxy: public AbstractSubscription<RegisterAccessResponse> {
private:
    std::map<CanardTransferID, std::tuple<std::string, uint64_t>> transfer_map;
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

        clean_transfer_map();
        transfer_map[register_access_transfer_id] = std::make_tuple(
            name,
            interface->get_utilities().micros_64() + DEFAULT_TIMEOUT_MICROS
        );
        interface->send_request<RegisterAccessRequest>(
            &request,
            uavcan_register_Access_1_0_FIXED_PORT_ID_,
            &register_access_transfer_id,
            target_node_id
        );
    }

    void clean_transfer_map() {
        std::erase_if(
            transfer_map,
            [this](const auto& item) {
                const auto& [key, val] = item;
                return interface->get_utilities().micros_64() > std::get<uint64_t>(val);
            }
        );
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

    size_t pending_requests() {
        return transfer_map.size();
    }

    void request_real32_value(const std::string& name, std::optional<float> value = std::nullopt) {
        request_generic<float>(name, value, &fill_register_real32);
    }

    void request_natural32_value(const std::string& name, std::optional<uint32_t> value = std::nullopt) {
        request_generic<uint32_t>(name, value, &fill_register_natural32);
    }

    void handler(const RegisterAccessResponse::Type& register_response, CanardRxTransfer* transfer) override {
        if (transfer->metadata.remote_node_id != target_node_id) {
            return;
        }
        CanardTransferID key = transfer->metadata.transfer_id;
        if (transfer_map.count(key) == 0) {
            return;
        }
        const std::string& reg_name = std::get<std::string>(transfer_map[key]);
        switch (register_response.value._tag_) {
            case REGISTER_REAL32_TAG:
                handle_float32(reg_name, register_response.value.real32.value.elements[0], transfer);
                break;
            case REGISTER_NATURAL32_TAG:
                handle_natural32(reg_name, register_response.value.natural32.value.elements[0], transfer);
                break;
            default:
                break;
        }
        transfer_map.erase(key);
    };

    virtual void handle_float32(const std::string& name, float value, CanardRxTransfer* transfer) = 0;
    virtual void handle_natural32(const std::string& name, uint32_t value, CanardRxTransfer* transfer) = 0;
};
