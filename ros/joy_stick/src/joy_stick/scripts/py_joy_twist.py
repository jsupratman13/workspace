#!/usr/env/bin python
#Program to receive command from Logicool controller and send as Twist
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyTwist(object):
	def __init__(self):
		self._joy_sub = rospy.Subscriber('joy', Joy, self.joy_callback, queue_size=1)
		self._twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

	def joy_callback(self, joy_msg):
		if joy_msg.buttons[0] == 1: #button 2
			twist = Twist()
			twist.linear.x = joy_msg.axes[1] * 0.5 #top,down arrow
			twist.angular.z = joy_msg.axes[0] * 1.0 #left right arrow
			self._twist_pub.publish(twist)

if __name__ == '__main__':
	rospy.init_node('joy_twist')
	joy_twist = JoyTwist()
	rospy.spin()
