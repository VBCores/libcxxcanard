#include "LinuxCAN.h"
#ifdef __linux__
#include <fcntl.h>
#include <linux/can.h>
#include <linux/can/raw.h>
#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <cstring>
#include <iostream>

#include "FDCAN_generic.h"

LinuxCAN::LinuxCAN(const std::string& can_interface, size_t queue_len, UtilityConfig& utilities)
    : AbstractCANProvider(CANARD_MTU_CAN_FD, CANFD_MTU, queue_len, utilities) {
    struct sockaddr_can addr;
    if ((socketcan_handler = socket(PF_CAN, SOCK_RAW, CAN_RAW)) < 0) {
        perror("Socket");
        exit(1);
    }
    int enable_canfd = 1;
    if (setsockopt(
            socketcan_handler,
            SOL_CAN_RAW,
            CAN_RAW_FD_FRAMES,
            &enable_canfd,
            sizeof(enable_canfd)
        )) {
        perror("error when enabling CAN FD support\n");
        exit(1);
    }

    // non-blocking CAN frame receiving => reading from this socket does not
    // block execution
    fcntl(socketcan_handler, F_SETFL, O_NONBLOCK);

    struct ifreq ifr {};
    strcpy(ifr.ifr_name, can_interface.c_str());
    ioctl(socketcan_handler, SIOCGIFINDEX, &ifr);

    memset(&addr, 0, sizeof(addr));
    addr.can_family = AF_CAN;
    addr.can_ifindex = ifr.ifr_ifindex;
    if (bind(socketcan_handler, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("Bind");
        exit(1);
    }
}

uint32_t LinuxCAN::len_to_dlc(size_t len) {
    return CanardFDCANLengthToDLC[len];
}

size_t LinuxCAN::dlc_to_len(uint32_t dlc) {
    return fdcan_dlc_to_len(dlc);
}

void LinuxCAN::can_loop() {
    CanardFrame frame;
    // read frames, but no more then 10 in a row
    for (int i = 0; i < 10 && read_frame(&frame); i++) {
        process_canard_rx(&frame);
    }

    process_canard_tx();
}

struct canfd_frame rxframe;
bool LinuxCAN::read_frame(CanardFrame* rxf) {
    uint8_t nbytes = read(socketcan_handler, &rxframe, WIRE_MTU);
    if (nbytes != WIRE_MTU) {  // only complete CAN frames are accepted
        return false;
    }

    auto msg_id = (uint32_t)rxframe.can_id;
    msg_id = msg_id & ~(1 << 31);  // clear EFF flag

    rxf->extended_can_id = msg_id;
    rxf->payload_size = (size_t)rxframe.len;
    rxf->payload = (void*)&rxframe.data;

    return true;
}

int LinuxCAN::write_frame(const CanardTxQueueItem* ti) {
    struct canfd_frame txframe;
    auto frame_size = sizeof(struct canfd_frame);
    txframe.len = ti->frame.payload_size;
    txframe.can_id = ti->frame.extended_can_id | CAN_EFF_FLAG;

    std::memcpy(&txframe.data, (uint8_t*)ti->frame.payload, ti->frame.payload_size);

    if (write(socketcan_handler, &txframe, frame_size) != frame_size) {
        return -1;  // If the driver is busy, break.
    }
    return frame_size;
}
#endif
