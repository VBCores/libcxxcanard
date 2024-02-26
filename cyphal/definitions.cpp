#include "definitions.h"

#include <chrono>

#ifdef __linux__

uint64_t _micros_64() {
    using namespace std::chrono;
    int64_t microseconds_since_epoch =
        duration_cast<microseconds>(system_clock::now().time_since_epoch()).count();
    return static_cast<uint64_t>(microseconds_since_epoch);
}

// NOLINTBEGIN(cppcoreguidelines-avoid-non-const-global-variables)
const UtilityConfig DEFAULT_CONFIG(_micros_64, []() { exit(1); });
// NOLINTEND(cppcoreguidelines-avoid-non-const-global-variables)

#endif
