#What version of CMake is needed?
cmake_minimum_required(VERSION 2.8.3)

#name of package
project(agitr)

#Find the catkin build system and any other packages on which we depend
#find_package(catkin REQUIRED COMPONENTS roscpp)
find_package(catkin REQUIRED COMPONENTS roscpp geometry_msgs)

#Declare our catkin package
catkin_package()

#spcify location of header files
include_directories(include ${catkin_INCLUDE_DIRS})

#Declare the executable along with its source files.
#If there are multiple executables, use multipls copis of this line
add_executable(hello hello.cpp)

#Specify libraries against which to link
#This line should be copied for each distinct executable in the package
target_link_libraries(hello ${catkin_LIBRARIES})

add_executable(pubvel pubvel.cpp)
target_link_libraries(pubvel ${catkin_LIBRARIES})

add_executable(subpose subpose.cpp)
target_link_libraries(subpose ${catkin_LIBRARIES})

add_executable(reverse_cmd_vel reverse_cmd_vel.cpp)
target_link_libraries(reverse_cmd_vel ${catkin_LIBRARIES})
