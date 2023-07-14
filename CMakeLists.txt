include_directories(.)
file(GLOB_RECURSE SOURCES "cyphal/*.c" "cyphal/*.cpp")

if(DEFINED ENV{<VBLIB_DIR>})
    set(VBLIB_DIR $ENV{VBLIB_DIR})
else()
    get_filename_component(VBLIB_DIR
            "../libvoltbro"
            ABSOLUTE)
endif()
message("${CMAKE_CURRENT_LIST_DIR} | Using <${VBLIB_DIR}> as directory of libvoltbro")

include_directories(${VBLIB_DIR})
add_subdirectory(${VBLIB_DIR}/libcanard ${PROJECT_BINARY_DIR}/build/libcanard)
add_subdirectory(${VBLIB_DIR}/o1heap ${PROJECT_BINARY_DIR}/build/o1heap)

add_library(libcyphal ${SOURCES} $<TARGET_OBJECTS:libcanard> $<TARGET_OBJECTS:o1heap>)
