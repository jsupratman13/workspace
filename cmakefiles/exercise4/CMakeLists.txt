cmake_minimum_required(VERSION 2.6)

project(prog6)

#find/use package/library/header
find_package(GLUT)
find_package(OpenGL)

#set option, see debug status
set(CMAKE_CXX_FLAGS "-g -Wall")

add_executable(prog6 prog6.cpp)
target_link_libraries(prog6 ${GLUT_LIBRARY} ${OPENGL_LIBRARY} m)
