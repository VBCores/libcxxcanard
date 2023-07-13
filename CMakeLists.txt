cmake_minimum_required(VERSION 3.23)
project(libcyphal)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_C_STANDARD 11)

include_directories(cyphal)
include_directories(libs)

file(GLOB_RECURSE SOURCES "Cyphal/*.c" "Cyphal/*.cpp" "Cyphal/*.hpp"  "Cyphal/*.h" "Cyphal/*.tpp")

add_executable(libcyphal ${SOURCES})
