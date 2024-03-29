#pragma once

#include <tuple>
#include <functional>
#include <utility>
#include <array>

#include "cyphal/cyphal.h"
#include "cyphal/subscriptions/subscription.h"
#include "uavcan/_register/Name_1_0.h"

#include <uavcan/_register/Access_1_0.h>
#include <uavcan/_register/List_1_0.h>

TYPE_ALIAS(RegisterAccessRequest, uavcan_register_Access_Request_1_0)
TYPE_ALIAS(RegisterAccessResponse, uavcan_register_Access_Response_1_0)
TYPE_ALIAS(RegisterListRequest, uavcan_register_List_Request_1_0)
TYPE_ALIAS(RegisterListResponse, uavcan_register_List_Response_1_0)

using RegisterCallback = std::function<void(
    const uavcan_register_Value_1_0&,
    uavcan_register_Value_1_0&,
    RegisterAccessResponse::Type&
)>;
using RegisterDefinition = std::pair<std::string, RegisterCallback>;

template<size_t N>
class RegistersHandler:
        public AbstractSubscription<RegisterListRequest>,
        public AbstractSubscription<RegisterAccessRequest> {
private:
    std::array<RegisterDefinition, N> registers;
public:
    RegistersHandler(std::array<RegisterDefinition, N>&& registers_list, InterfacePtr interface):
        AbstractSubscription<RegisterListRequest>(
            interface,
            uavcan_register_List_1_0_FIXED_PORT_ID_,
            CanardTransferKindRequest
        ),
        AbstractSubscription<RegisterAccessRequest>(
            interface,
            uavcan_register_Access_1_0_FIXED_PORT_ID_,
            CanardTransferKindRequest
        ),
        registers(std::move(registers_list))
    {}

    virtual CanardFilter make_filter(CanardNodeID node_id) override {
        CanardFilter access_filter = AbstractSubscription<RegisterAccessRequest>::make_filter(node_id);
        CanardFilter list_filter = AbstractSubscription<RegisterListRequest>::make_filter(node_id);
        return canardConsolidateFilters(&access_filter, &list_filter);
    }

    void handler(const RegisterListRequest::Type& register_list_request, CanardRxTransfer* transfer) override {
        RegisterListResponse::Type register_list_response = {};

        uavcan_register_Name_1_0 name = {};

        if (register_list_request.index < registers.size()) {
            auto register_name = std::get<std::string>(registers[register_list_request.index]);
            memcpy(name.name.elements, register_name.c_str(), register_name.size());
            name.name.count = register_name.size();
        }
        register_list_response.name = name;

        AbstractSubscription<RegisterListRequest>::interface->send_response<RegisterListResponse>(
            &register_list_response, transfer
        );
    };

    void handler(const RegisterAccessRequest::Type& register_access_request, CanardRxTransfer* transfer) override {
        RegisterAccessResponse::Type register_access_response = {};

        InterfacePtr interface = AbstractSubscription<RegisterAccessRequest>::interface;

        register_access_response.timestamp.microsecond = interface->get_utilities().micros_64();
        uavcan_register_Value_1_0 value = {};

        bool is_found = false;
        for (auto& register_def : registers) {
            auto& register_name = std::get<std::string>(register_def);
            if(memcmp(
                register_name.c_str(),
                register_access_request.name.name.elements,
                register_access_request.name.name.count
            ) != 0) {
                continue;
            }
            is_found = true;
            auto& register_handler = std::get<RegisterCallback>(register_def);
            register_handler(register_access_request.value, value, register_access_response);
            break;
        }
        if (!is_found) {
            value._tag_ = 0;
            value.empty = (uavcan_primitive_Empty_1_0){};
        }

        register_access_response.value = value;
        AbstractSubscription<RegisterAccessRequest>::interface->send_response<RegisterAccessResponse>(
            &register_access_response, transfer
        );
    };
};
