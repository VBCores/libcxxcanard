#pragma once
#include "cyphal/definitions.h"
#if (defined(STM32G474xx) || defined(STM32_G)) && defined(HAL_FDCAN_MODULE_ENABLED)

#include "provider.h"

class G4CAN : public AbstractCANProvider {
private:
    FDCAN_HandleTypeDef* handler;

public:
    typedef FDCAN_HandleTypeDef* Handler;
    G4CAN(Handler handler) : AbstractCANProvider(CANARD_MTU_CAN_FD, 72), handler(handler){};
    uint32_t len_to_dlc(size_t len) override;
    size_t dlc_to_len(uint32_t dlc) override;
    void can_loop() override;
    bool read_frame(CanardFrame*)  override;
    int write_frame(const CanardTxQueueItem* ti) override;
};

#endif