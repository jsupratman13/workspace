#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from kobuki_msgs.msg import BumperEvent

#callback function, execute when hit something
def callback(bumper):
	print bumper
	vel = Twist()
	vel.linear.x = -1.0
	pub.publish(vel)

if __name__=='__main__':
	rospy.init_node('vel_bumper')

	#create publihser instance
	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)

	#create subscriber instance
	sub = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback)

	#take keyboard command
	while not rospy.is_shutdown():
		vel = Twist()
		direction = raw_input("f: forward, b: backward, l: left, r: right > ")
		if 'f' in direction:
			vel.linear.x = 0.5
		if 'b' in direction:
			vel.linear.x = -0.5
		if 'l' in direction:
			vel.angular.z = 1.0
		if 'r' in direction:
			vel.angular.z = -1.0
		if 'q' in direction:
			break
		print vel
		pub.publish(vel)
