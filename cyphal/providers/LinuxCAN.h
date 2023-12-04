#pragma once
#include "cyphal/definitions.h"
#ifdef __linux__

#include <string>

#include "provider.h"

class LinuxCAN : public AbstractCANProvider {
private:
    int socketcan_handler;

public:
    typedef const std::string& Handler;
    LinuxCAN(Handler can_interface);
    uint32_t len_to_dlc(size_t len) override;
    size_t dlc_to_len(uint32_t dlc) override;
    void can_loop() override;
    bool read_frame(CanardFrame*)  override;
    int write_frame(const CanardTxQueueItem* ti) override;
};
#endif
