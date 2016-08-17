##Execution method
roscore

###For python in kobuki
rosrun teleop_twist_joy teleop_node
python py_joy_twist.py cmd_vel:=/mobile_base/commands/velocity

###for python in turtlesim
rosrun teleop_twist_joy teleop_node
python py_joy_twist.py cmd_vel:=/turtle1/cmd_vel

###for c++ turtlesim
rosrun joy joy_node
rosrun joy_stick joy_twist
