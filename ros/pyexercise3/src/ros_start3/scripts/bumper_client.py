#!/usr/bin/env python
import rospy
#use actionlib
import actionlib
from ros_start3.msg import GoUntilBumperAction #use xxxAction class: define spec
from ros_start3.msg import GoUntilBumperGoal #use xxxGoal class: define target


def go_until_bumper():
	#create action client: action name, actiontype
	action_client = actionlib.SimpleActionClient('bumper_action', GoUntilBumperAction)
	
	#REQUIRED: wait for server to be set up, if not it will think job is finished
	action_client.wait_for_server()

	#define goal
	goal = GoUntilBumperGoal()
	goal.target_vel.linear.x = 0.8
	goal.timeout_sec = 10

	#send goal, wait for result and get result
	action_client.send_goal(goal)
	action_client.wait_for_result()
	result = action_client.get_result()
	
	if result.bumper_hit:
		rospy.loginfo('bumper hit')
	else:	
		rospy.loginfo('failed')

if __name__=='__main__':
	try:
		rospy.init_node('bumper_client')
		go_until_bumper()
	
	#finished using Ctrl+C
	except rospy.ROSInterruptException:
		pass

