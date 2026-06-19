cmake_minimum_required(VERSION 3.15)
project(libcxxcanard_linux_examples)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Threads REQUIRED)

set(LIBCXXCANARD_DIR "" CACHE PATH "Path to libcxxcanard checkout")
if(NOT LIBCXXCANARD_DIR)
    if(DEFINED ENV{LIBCXXCANARD_DIR})
        set(LIBCXXCANARD_DIR "$ENV{LIBCXXCANARD_DIR}")
    elseif(EXISTS "${CMAKE_CURRENT_LIST_DIR}/../../CMakeLists.txt")
        set(LIBCXXCANARD_DIR "${CMAKE_CURRENT_LIST_DIR}/../..")
    elseif(EXISTS "${CMAKE_CURRENT_LIST_DIR}/libcxxcanard/CMakeLists.txt")
        set(LIBCXXCANARD_DIR "${CMAKE_CURRENT_LIST_DIR}/libcxxcanard")
    else()
        message(FATAL_ERROR "Set LIBCXXCANARD_DIR to the libcxxcanard checkout")
    endif()
endif()
get_filename_component(LIBCXXCANARD_DIR "${LIBCXXCANARD_DIR}" ABSOLUTE)

set(CYPHAL_TYPES_DIR "" CACHE PATH "Path to the project cyphal_types directory")
if(NOT CYPHAL_TYPES_DIR)
    if(DEFINED ENV{CYPHAL_TYPES_DIR})
        set(CYPHAL_TYPES_DIR "$ENV{CYPHAL_TYPES_DIR}")
    elseif(EXISTS "${CMAKE_CURRENT_LIST_DIR}/cyphal_types")
        set(CYPHAL_TYPES_DIR "${CMAKE_CURRENT_LIST_DIR}/cyphal_types")
    elseif(EXISTS "${LIBCXXCANARD_DIR}/../cyphal_types")
        set(CYPHAL_TYPES_DIR "${LIBCXXCANARD_DIR}/../cyphal_types")
    else()
        message(FATAL_ERROR "Set CYPHAL_TYPES_DIR to a directory with public_regulated_data_types and voltbro_types")
    endif()
endif()
get_filename_component(CYPHAL_TYPES_DIR "${CYPHAL_TYPES_DIR}" ABSOLUTE)

add_subdirectory("${LIBCXXCANARD_DIR}" "${CMAKE_BINARY_DIR}/libcxxcanard-build")
include("${LIBCXXCANARD_DIR}/examples/cyphal_types.cmake")

set(CYPHAL_TYPE_REPOS
    "${CYPHAL_TYPES_DIR}/public_regulated_data_types"
    "${CYPHAL_TYPES_DIR}/voltbro_types"
)

set(EXAMPLE_TARGETS
    simple_echo
    service_echo
    full_example
)

foreach(EXAMPLE_TARGET IN LISTS EXAMPLE_TARGETS)
    add_executable(${EXAMPLE_TARGET} ${EXAMPLE_TARGET}.cpp)
    target_link_libraries(${EXAMPLE_TARGET} PRIVATE libcxxcanard Threads::Threads)
    target_include_directories(${EXAMPLE_TARGET} PRIVATE
        "${CMAKE_CURRENT_LIST_DIR}"
        "${LIBCXXCANARD_DIR}"
        "${LIBCXXCANARD_DIR}/libs"
    )
    cyphal_add_dsdl_types(${EXAMPLE_TARGET} TYPE_REPOS ${CYPHAL_TYPE_REPOS})
endforeach()
