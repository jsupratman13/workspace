#This ir ROS python version of the "hello world program
#ROS class module
import rospy

#initialize ros system and establish this program as ROS node
rospy.init_node('hello_world_node')

#send ouput log message
rospy.loginfo('hello ROS python!')

#loop, exit through ctrl+c
rospy.spin()
