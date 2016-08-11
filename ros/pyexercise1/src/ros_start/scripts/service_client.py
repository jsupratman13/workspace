#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty

def call_service():
	rospy.loginfo('wait for service')
	
	#wait for 'call_me' service; if this is not included exception will occur
	rospy.wait_for_service('call_me')

	try:
		#create service client instance
		service = rospy.ServiceProxy('call_me', Empty)
		respond = service()
	
	#exception if service failed
	except rospy.ServiceException, e:
		print 'failed to call service: %s' % e

if __name__ == '__main__':
	call_service()

