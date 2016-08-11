execute_process(COMMAND "/home/jsupratman13/github/workspace/ros/pyexercise3/build/ros_start3/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jsupratman13/github/workspace/ros/pyexercise3/build/ros_start3/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
