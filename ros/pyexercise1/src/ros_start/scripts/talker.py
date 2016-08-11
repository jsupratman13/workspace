#!/usr/bin/env python
import rospy
from std_msgs.msg import String #String type message module

#initialize the ROS system and become node
rospy.init_node('talker')

#create publisher instance
pub = rospy.Publisher('chatter', String, queue_size=10)

#loop at 10Hz until the node is shut down
rate = rospy.Rate(10)
while not rospy.is_shutdown():
	
	#create the message
	hello_str = String()
	hello_str.data = "hello world %s" %rospy.get_time()

	#publish the message
	pub.publish(hello_str)

	#wait until its time for another iteration
	rate.sleep()

