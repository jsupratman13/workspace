#Execution method
for initialization, activate the following (except for turtlesim)
```
roscore
roslaunch kobuki_gazebo kobuki_playground.launch
```

##for publisher
rosrun ros_start2 vel_publisher.py
(or)
python vel_publisher.py

##for bumper
rosrun ros_start2 vel_bumper.py
(or)
python vel_bumper.py

##for parameter
rosparam set /vel_bumper/vel_x 1.0
rosparam set /vel_bumper/vel_rot 1.5

##set paramter and excute program
./vel_bumper_parameter.py _vel_x:=1.0 (if using private paramter, use _ instead of ~)
(or) 
./vel_bumper_parameter.py /vel_bumper/vel_x:=1.0

##use pr2 robo instead
roscore
roslaunch pr2_gazebo pr2_empty_world.launch
rosrun ros_start2 vel_bumper.py /mobile_base/commands/velocity:=/base_controller/command

##use turtesim with paramter change
roscore
rosrun turtlesim turtlesim_node
rosrun ros_start2 vel_bumper_parameter.py /mobile_base/commands/velocity:=/turtle1/cmd_vel _vel_x:=1.5

