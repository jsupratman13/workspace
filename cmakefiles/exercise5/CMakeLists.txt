cmake_minimum_required(VERSION 2.6)

project(prog7)

##find package
find_package(Qt4 REQUIRED)

#Include headerfile for GUI signal/slot function communication
QT4_WRAP_CPP(prog7_h_moc ${prog7.h})
#include interface file for Qt Designer
QT4_WRAP_UI(prog7_ui_h prog1.ui)
#include .qrc file for icon
QT4_ADD_RESOURCES(prog7_rccC prog7.qrc)

#include all the above
include(${QT_USE_FILE})

add_executable(prog7 prog7.cpp)
#long method
#add_executable(prog7 prog7.cpp ${prog7_h_moc} ${porg7_ui_h} ${prog7_rcc})

include_directories(${CMAKE_CURRENT_BINARY_DIR})
target_link_libraries(prog7 ${QT_LIBRARIES})
