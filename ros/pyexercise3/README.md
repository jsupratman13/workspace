#Execution Method
at beginning of exercise, initialize the following
```
roscore
roslaunch kobuki_gazebo kobuki_playground.launch
```
##For service and client
rosrun ros_start3 velocity_server.py
rosrun ros_start3 velocity_client.py 0.5 0.0 (linear, angular velocity)

##For service only
rosservice call /set_velocity 1.0 0.0

##For action server
rosrun ros_start3 bumper_action.py
rosrun actionlib axclient.py /bumper_action

##For action client
rosrun ros_start3 bumper_action.py
rosrun ros_start3 bumper_client.py

##for action client with library
rosrun ros_start3 bumper_action_use_libs.py
rosrun ros_start3 bumper_client_use_libs.py
