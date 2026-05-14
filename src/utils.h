#ifndef CRITICAL_SECTION
#define CRITICAL_SECTION(code_blk)          \
    uint32_t primask_bit = __get_PRIMASK(); \
    __disable_irq();                        \
    code_blk __set_PRIMASK(primask_bit);
#endif

#ifndef MICROS_S
    #define MICROS_S 1000000000ULL
#endif

#ifndef HAL_IMPORTANT
#define HAL_IMPORTANT(command) \
    if ((command) != HAL_OK) { \
        while(true) {}         \
    }
#endif

#ifndef EACH_N
#define EACH_N(_value, _counter, N, code_blk) \
    if ((_value - _counter) >= (N)) {         \
        code_blk                              \
        _counter = _value;                    \
    }
#endif

#ifndef EACH_N_MICROS
#define EACH_N_MICROS(_value, _counter, N, code_blk)         \
    int64_t diff_##_counter = subtract_64(_value, _counter); \
    if (diff_##_counter >= (int64_t)N) {                     \
        code_blk                                             \
        _counter = _value;                                   \
    }
#endif
