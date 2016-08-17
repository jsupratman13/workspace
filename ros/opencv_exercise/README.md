#Execution Method
roscore
rosrun usb_cam usb_cam_node
rosrun image_view image_view image:=/blue_image &
rosrun image_view image_view image:=/red_image &
rosrun image_view image_view image:=/usb_cam/image_raw &
(use 'fg' if accidently use & when you dont want to)

##for kobuki
roslaunch kobuki_gazebo kobuki_playground.launch
python color_vel.py cmd_vel:=/mobile_base/commands/velocity

##for turtlesim
rosrun turtlesim turtlesim_node
python color_vel.py cmd_vel:=/turtle1/cmd_vel
