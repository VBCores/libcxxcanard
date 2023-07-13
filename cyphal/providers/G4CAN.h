#pragma once
#include "definitions.h"
#if (defined(STM32G474xx) || defined(STM32_G)) && defined(HAL_FDCAN_MODULE_ENABLED)

#include "provider.h"

class G4CAN : public AbstractCANProvider {
   private:
    const FDCAN_HandleTypeDef* handler;

   public:
    G4CAN(FDCAN_HandleTypeDef* handler)
        : AbstractCANProvider(CANARD_MTU_CAN_FD, 72), handler(handler){};
    uint32_t len_to_dlc(size_t len) override;
    size_t dlc_to_len(uint32_t dlc) override;
    void can_loop() override;
    CanardFrame* read() override;
    int write(const CanardTxQueueItem* ti) override;
};

#endif