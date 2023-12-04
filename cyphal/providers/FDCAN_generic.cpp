#include "FDCAN_generic.h"

#ifdef __linux__
#define FDCAN_DLC_BYTES_0 ((uint32_t)0x00000000U)  /*!< 0 bytes data field  */
#define FDCAN_DLC_BYTES_1 ((uint32_t)0x00010000U)  /*!< 1 bytes data field  */
#define FDCAN_DLC_BYTES_2 ((uint32_t)0x00020000U)  /*!< 2 bytes data field  */
#define FDCAN_DLC_BYTES_3 ((uint32_t)0x00030000U)  /*!< 3 bytes data field  */
#define FDCAN_DLC_BYTES_4 ((uint32_t)0x00040000U)  /*!< 4 bytes data field  */
#define FDCAN_DLC_BYTES_5 ((uint32_t)0x00050000U)  /*!< 5 bytes data field  */
#define FDCAN_DLC_BYTES_6 ((uint32_t)0x00060000U)  /*!< 6 bytes data field  */
#define FDCAN_DLC_BYTES_7 ((uint32_t)0x00070000U)  /*!< 7 bytes data field  */
#define FDCAN_DLC_BYTES_8 ((uint32_t)0x00080000U)  /*!< 8 bytes data field  */
#define FDCAN_DLC_BYTES_12 ((uint32_t)0x00090000U) /*!< 12 bytes data field */
#define FDCAN_DLC_BYTES_16 ((uint32_t)0x000A0000U) /*!< 16 bytes data field */
#define FDCAN_DLC_BYTES_20 ((uint32_t)0x000B0000U) /*!< 20 bytes data field */
#define FDCAN_DLC_BYTES_24 ((uint32_t)0x000C0000U) /*!< 24 bytes data field */
#define FDCAN_DLC_BYTES_32 ((uint32_t)0x000D0000U) /*!< 32 bytes data field */
#define FDCAN_DLC_BYTES_48 ((uint32_t)0x000E0000U) /*!< 48 bytes data field */
#define FDCAN_DLC_BYTES_64 ((uint32_t)0x000F0000U) /*!< 64 bytes data field */
#endif

const uint32_t CanardFDCANLengthToDLC[65] = {
    // 0-8
    FDCAN_DLC_BYTES_0,
    FDCAN_DLC_BYTES_1,
    FDCAN_DLC_BYTES_2,
    FDCAN_DLC_BYTES_3,
    FDCAN_DLC_BYTES_4,
    FDCAN_DLC_BYTES_5,
    FDCAN_DLC_BYTES_6,
    FDCAN_DLC_BYTES_7,
    FDCAN_DLC_BYTES_8,
    // 9-12
    FDCAN_DLC_BYTES_12,
    FDCAN_DLC_BYTES_12,
    FDCAN_DLC_BYTES_12,
    FDCAN_DLC_BYTES_12,
    // 13-16
    FDCAN_DLC_BYTES_16,
    FDCAN_DLC_BYTES_16,
    FDCAN_DLC_BYTES_16,
    FDCAN_DLC_BYTES_16,
    // 17-20
    FDCAN_DLC_BYTES_20,
    FDCAN_DLC_BYTES_20,
    FDCAN_DLC_BYTES_20,
    FDCAN_DLC_BYTES_20,
    // 20-24
    FDCAN_DLC_BYTES_24,
    FDCAN_DLC_BYTES_24,
    FDCAN_DLC_BYTES_24,
    FDCAN_DLC_BYTES_24,
    // 24-32
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    FDCAN_DLC_BYTES_32,
    // 33-48
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    FDCAN_DLC_BYTES_48,
    // 49-64
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
    FDCAN_DLC_BYTES_64,
};

size_t fdcan_dlc_to_len(uint32_t dlc) {
    auto dlc_index = (uint8_t)(dlc / 65536);
    if (dlc_index <= 8) {
        return dlc_index;
    }
    if (dlc_index <= 12) {
        return 8 + 4 * (dlc_index - 8);
    }
    return 32 + 16 * (dlc_index - 13);
}
