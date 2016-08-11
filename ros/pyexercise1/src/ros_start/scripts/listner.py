#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#call back function, executed each time a new message arrives
def callback(message):
	rospy.loginfo("I heard %s", message.data)

#initialize the ROS system and become a node
rospy.init_node('listner')

#create a subscriber instance
sub = rospy.Subscriber('chatter', String, callback)

#let ROS take over
rospy.spin()

