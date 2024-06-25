#if (defined(STM32G474xx) || defined(STM32_G))
#include "node_info_handler.h"

#include "stm32g4xx_ll_utils.h"

NodeInfoReader::NodeInfoReader(
    InterfacePtr interface,
    std::string&& name,
    uavcan_node_Version_1_0&& protocol_version,
    uavcan_node_Version_1_0&& hardware_version,
    uavcan_node_Version_1_0&& software_version,
    uint64_t software_vcs_revision_id
): AbstractSubscription<NodeInfoRequest>(
    interface,
    uavcan_node_GetInfo_1_0_FIXED_PORT_ID_,
    CanardTransferKindRequest
) {
    node_info.protocol_version = std::move(protocol_version);
    node_info.hardware_version = std::move(hardware_version);
    node_info.software_version = std::move(software_version);
    node_info.software_vcs_revision_id = software_vcs_revision_id;

    node_info.certificate_of_authenticity.count = 0;
    node_info.software_image_crc.count = 0;

    strcpy((char*)node_info.name.elements, name.c_str());
    node_info.name.count = name.size();

    uint32_t word0 = LL_GetUID_Word0();
    uint32_t word1 = LL_GetUID_Word1();
    uint32_t word2 = LL_GetUID_Word2();
    memcpy(node_info.unique_id, &word0, 4);
    memcpy(node_info.unique_id + 4, &word1, 4);
    memcpy(node_info.unique_id + 8, &word2, 4);
};

void NodeInfoReader::handler(
    const uavcan_node_GetInfo_Request_1_0& object,
    CanardRxTransfer* transfer
) {
    interface->send_response<NodeInfoResponse>(&node_info, transfer);
}
#endif
