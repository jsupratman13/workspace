cmake_minimum_required(VERSION 2.6)

project(prog4)

#this version number
set(PROG4_VERSION_MAJOR 1)
set(PROG4_VERSION_MINOR 0)

#make Prog4Config.h from Prog4Config.h.in and CMakeLists.txt
configure_file("${PROJECT_SOURCE_DIR}/Prog4Config.h.in" "${PROJECT_BINARY_DIR}/Prog4Config.h")

##add the binary tree to the search path for include files
include_directories("${PROJECT_BINARY_DIR}")

add_executable(prog4 prog4.cpp)

add_executable(prog5 prog5.cpp)
target_link_libraries(prog5 m) #linking prog5 to libm math library
