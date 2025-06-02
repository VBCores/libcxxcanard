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

// NOLINTBEGIN(cppcoreguidelines-pro-type-vararg,hicpp-vararg,cppcoreguidelines-pro-bounds-array-to-pointer-decay,hicpp-no-array-decay,cppcoreguidelines-pro-type-cstyle-cast,cppcoreguidelines-pro-bounds-constant-array-index)
LinuxCAN::LinuxCAN(
    const std::string& can_interface,
    size_t queue_len,
    const UtilityConfig& utilities
)
    : AbstractCANProvider(CANARD_MTU_CAN_FD, CANFD_MTU, queue_len, utilities),
      socketcan_handler(socket(PF_CAN, SOCK_RAW, CAN_RAW)) {
    if (socketcan_handler < 0) {
        perror("Could not open socket");
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
    strncpy(ifr.ifr_name, can_interface.c_str(), IFNAMSIZ);
    ioctl(socketcan_handler, SIOCGIFINDEX, &ifr);

    struct sockaddr_can addr {};
    memset(&addr, 0, sizeof(addr));
    addr.can_family = AF_CAN;
    addr.can_ifindex = ifr.ifr_ifindex;
    if (bind(socketcan_handler, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("Bind");
        exit(1);
    }

    can_pollfd.fd = socketcan_handler;
    can_pollfd.events = POLLIN;
}

void LinuxCAN::lock_canard() {
    canard_mutex.lock();
}

void LinuxCAN::unlock_canard() {
    canard_mutex.unlock();
}

uint32_t LinuxCAN::len_to_dlc(size_t len) {
    return CanardFDCANLengthToDLC[len];
}
// NOLINTEND(cppcoreguidelines-pro-type-vararg,hicpp-vararg,cppcoreguidelines-pro-bounds-array-to-pointer-decay,hicpp-no-array-decay,cppcoreguidelines-pro-type-cstyle-cast,cppcoreguidelines-pro-bounds-constant-array-index)

size_t LinuxCAN::dlc_to_len(uint32_t dlc) {
    return fdcan_dlc_to_len(dlc);
}

void LinuxCAN::can_loop(bool no_tx) {
    CanardFrame frame;
    struct canfd_frame raw_frame {};

    int status = poll(&can_pollfd, 1, 50);
    if (status == -1) {
        utilities.error_handler();
    }

    if (status && (can_pollfd.revents & POLLIN)) {
        while(read_frame(&frame, static_cast<void*>(&raw_frame))) {
            process_canard_rx(&frame);
        }
    }

    if (!no_tx) {
        process_canard_tx();
    }
}

bool LinuxCAN::read_frame(CanardFrame* rxf, void* data) {
    auto rxframe = static_cast<struct canfd_frame*>(data);
    uint8_t nbytes = read(socketcan_handler, rxframe, WIRE_MTU);
    if (nbytes != WIRE_MTU) {  // only complete CAN frames are accepted
        return false;
    }

    auto msg_id = (uint32_t)rxframe->can_id;
    // Magic line from the depths of socketcan docs
    // NOLINTBEGIN(cppcoreguidelines-avoid-magic-numbers,hicpp-signed-bitwise)
    msg_id = msg_id & ~(1 << 31);  // clear EFF flag
    // NOLINTEND(cppcoreguidelines-avoid-magic-numbers,hicpp-signed-bitwise)

    rxf->extended_can_id = msg_id;
    rxf->payload_size = (size_t)rxframe->len;
    rxf->payload = static_cast<void*>(&rxframe->data);

    return true;
}

int LinuxCAN::write_frame(const CanardTxQueueItem* ti) {
    struct canfd_frame txframe {};
    auto frame_size = sizeof(struct canfd_frame);
    txframe.len = ti->frame.payload_size;
    txframe.can_id = ti->frame.extended_can_id | CAN_EFF_FLAG;

    std::memcpy(&txframe.data, ti->frame.payload, ti->frame.payload_size);

    if (write(socketcan_handler, &txframe, frame_size) != frame_size) {
        return -1;  // If the driver is busy, break.
    }
    return static_cast<int>(frame_size);
}
#endif
