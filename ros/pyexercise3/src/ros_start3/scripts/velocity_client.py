#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from ros_start3.srv import SetVelocity #import srv definition
import sys

if __name__ == '__main__':
	rospy.init_node('velocity_client')
	
	#Define Service Proxy
	set_velocity = rospy.ServiceProxy('set_velocity', SetVelocity)

	#define args parameter
	linear_vel = float(sys.argv[1])
	angular_vel = float(sys.argv[2])

	#call service and wait for response
	response = set_velocity(linear_vel, angular_vel)

	if response.success:
		rospy.loginfo('set [%f, %f] success' % (linear_vel, angular_vel))
	else:
		rospy.logerr('set [%f, %f] failed' % (linear_vel, angular_vel))
