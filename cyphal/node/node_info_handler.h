#pragma once

#include <string>
#include <utility>

#include "cyphal/cyphal.h"
#include "cyphal/subscriptions/subscription.h"

#include <uavcan/node/GetInfo_1_0.hpp>

using NodeInfoRequest = uavcan_node_GetInfo_Request_1_0;
using NodeInfoResponse = uavcan_node_GetInfo_Response_1_0;

class NodeInfoReader : public AbstractSubscription<NodeInfoRequest> {
private:
    NodeInfoResponse node_info;
public:
    NodeInfoReader(
        InterfacePtr interface,
        std::string&& name,
        uavcan_node_Version_1_0&& protocol_version,
        uavcan_node_Version_1_0&& hardware_version,
        uavcan_node_Version_1_0&& software_version,
        uint64_t software_vcs_revision_id
    );
    void handler(const NodeInfoRequest&, CanardRxTransfer*) override;
};
