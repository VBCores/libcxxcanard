cmake_minimum_required(VERSION 3.15)
project(simple_echo)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Threads REQUIRED)

add_executable(${CMAKE_PROJECT_NAME} simple_echo.cpp)

add_subdirectory(libcxxcanard)
include(${CMAKE_CURRENT_SOURCE_DIR}/cyphal_types/cyphal_types.cmake)

target_link_libraries(${CMAKE_PROJECT_NAME} PRIVATE libcxxcanard Threads::Threads)
target_include_directories(${CMAKE_PROJECT_NAME} PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/libcxxcanard
    ${CMAKE_CURRENT_SOURCE_DIR}/libcxxcanard/libs
)
cyphal_add_dsdl_types(${CMAKE_PROJECT_NAME}
    TYPE_REPOS
        ${CMAKE_CURRENT_SOURCE_DIR}/cyphal_types/public_regulated_data_types
        ${CMAKE_CURRENT_SOURCE_DIR}/cyphal_types/voltbro_types
)
