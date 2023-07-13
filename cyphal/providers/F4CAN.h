#pragma once
#include "definitions.h"
#if (defined(STM32F446xx) || defined(STM32_F)) && defined(HAL_CAN_MODULE_ENABLED)

#include "provider.h"

class F4CAN : public AbstractCANProvider {
   private:
    const CAN_HandleTypeDef* handler;

   public:
    F4CAN(CAN_HandleTypeDef* handler)
        : AbstractCANProvider(CANARD_MTU_CAN_CLASSIC, 16), handler(handler){};
    uint32_t len_to_dlc(size_t len) override;
    size_t dlc_to_len(uint32_t dlc) override;
    void can_loop() override;
    CanardFrame* read() override;
    int write(const CanardTxQueueItem* ti) override;
};

#endif