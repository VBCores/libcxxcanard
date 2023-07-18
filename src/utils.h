#define CRITICAL_SECTION(code_blk)          \
    uint32_t primask_bit = __get_PRIMASK(); \
    __disable_irq();                        \
    code_blk __set_PRIMASK(primask_bit);
