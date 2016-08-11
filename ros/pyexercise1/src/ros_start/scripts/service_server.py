#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty, EmptyResponse #standard service type

#call back function, execute
def handle_service(request):
	rospy.loginfo('called')

	#return value always
	return EmptyResponse()

def service_server():
	rospy.init_node('service_server')

	#Register service
	r = rospy.Service('call_me', Empty, handle_service)

	print 'ready to serve'
	rospy.spin()

if __name__=='__main__':
	service_server()
