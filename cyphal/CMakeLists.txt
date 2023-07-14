include_directories(.)
file(GLOB_RECURSE SOURCES "./*.c" "./*.cpp")

if(DEFINED ENV{<COMMON_LIBS_DIR>})
    set(COMMON_LIBS_DIR $ENV{COMMON_LIBS_DIR})
else()
    get_filename_component(COMMON_LIBS_DIR
                           "../libs"
                           ABSOLUTE)
endif()
message("Using <${COMMON_LIBS_DIR}> as directory of common Cyphal libs - libcanard, uavcan, o1heap, etc.")

include_directories(${COMMON_LIBS_DIR})
add_subdirectory(${COMMON_LIBS_DIR}/libcanard ${PROJECT_BINARY_DIR}/build/libcanard)
add_subdirectory(${COMMON_LIBS_DIR}/o1heap ${PROJECT_BINARY_DIR}/build/o1heap)

add_library(libcyphal ${SOURCES} $<TARGET_OBJECTS:libcanard> $<TARGET_OBJECTS:o1heap>)
