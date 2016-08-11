//This program publishes randomly-generated velocity message for turtlesim
#include <ros/ros.h>
#include <geometry_msgs/Twist.h> // For geometry_msg::Twist
#include <stdlib.h> //for rand() and RAND_MAx

int main(int argc, char **argv){
	//Initialize the ROS system and become node
	ros::init(argc, argv, "publish_velocity");
	ros::NodeHandle nh;

	//Create a publisher object
	ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 1000);

	//seed the random number generator
	srand(time(0));

	//Loop at 2Hz until the node is shut down
	ros::Rate rate(2);
	while(ros::ok()){
		//create and fill in the message
		//the other four fields, which are ignored by turtlesim, default to 0
		geometry_msgs::Twist msg;
		msg.linear.x = double(rand())/double(RAND_MAX);
		msg.angular.z = 2*double(rand())/double(RAND_MAX)-1;

		//publish the message
		pub.publish(msg);

		//send a message to rosout with the details
		ROS_INFO_STREAM("Send_random_velocity_command:"
			<< "_linear=" << msg.linear.x
			<<"_angular=" << msg.angular.z);

		//wait until its time for another iteration
		rate.sleep();
	}
}
