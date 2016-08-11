#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist #get Twist message type
from kobuki_msgs.msg import BumperEvent #get BumperEvent message type
#Use actionlib
import actionlib
from ros_start3.msg import GoUntilBumperAction # use xxxAction class: define spec
from ros_start3.msg import GoUntilBumperResult # use xxxResult class: return results
from ros_start3.msg import GoUntilBumperFeedback # use xxxFeedback class: return progress result

class BumperAction(object):
	def __init__(self):
		#create publisher/subscriber instance
		self._pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=10)
		self._sub = rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, self.bumper_callback, queue_size=1)

		#create parameter
		self._max_vel = rospy.get_param('~max_vel', 0.5)

		#create action server: action name, action type, excuting process, auto_start flag)
		self._action_server = actionlib.SimpleActionServer('bumper_action', GoUntilBumperAction, execute_cb=self.go_until_bumper, auto_start=False)

		#initial value
		self._hit_bumper = False

		#activate server
		self._action_server.start()
	
	#call back function
	def bumper_callback(self, bumper):
		self._hit_bumper = True

	#main action server body
	def go_until_bumper(self, goal):
		#print target value
		print(goal.target_vel)

		#rate 10 Hz
		r = rospy.Rate(10.0)

		#define stop motion
		zero_vel = Twist()

		#since its 10Hz, looping for 10 times equals to 1 second
		for i in range(10*goal.timeout_sec):
			
			#since process takes time until completion, can be stopped from outside intervention
			if self._action_server.is_preempt_requested():
				#stop process
				self._action_server.set_preempted()
				break

			#if bumper is hit stop moving
			if self._hit_bumper:
				self._pub.publish(zero_vel)
				break

			else:
				#robot moves at target speed but less than max speed
				if goal.target_vel.linear.x > self._max_vel:
					goal.target_vel.linear.x = self._max_vel
				self._pub.publish(goal.target_vel)

				#feed back current velocity and pass to publish_feedback
				feedback = GoUntilBumperFeedback(current_vel=goal.target_vel)
				self._action_server.publish_feedback(feedback)
			
			#sleep
			r.sleep()

		#input bumper_hit result and call if result is successful
		result = GoUntilBumperResult(bumper_hit=self._hit_bumper)
		self._action_server.set_succeeded(result)

if __name__ == '__main__':
	rospy.init_node('bumper_action')
	#call instance and wait for action
	bumper_action = BumperAction()
	rospy.spin()

