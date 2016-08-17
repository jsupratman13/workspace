#include <ros/ros.h>
#include <sensor_msgs/Joy.h>
#include <geometry_msgs/Twist.h>
#include <iostream>

class JoyTwist{
	public:
		//contructor
		JoyTwist(){
			ros::NodeHandle nh; //create node
			joy_sub = nh.subscribe("joy", 1, &JoyTwist::joyCallback, this); //generate subscriber
			twist_pub= nh.advertise<geometry_msgs::Twist>("cmd_vel", 1);	//generate publisher
		}
		//callback function
		void joyCallback(const sensor_msgs::Joy& joy_msgs){
			if(joy_msgs.buttons[0] == 1){
				geometry_msgs::Twist twist;
				twist.linear.x = joy_msgs.axes[1] * 0.5;
				twist.angular.z = joy_msgs.axes[0] * 1.0;
				twist_pub.publish(twist); //publish
			}
		}
	private:
		ros::Subscriber joy_sub;	//define subscriber
		ros::Publisher twist_pub;	//define publisher
};

int main(int argc, char **argv){
	ros::init(argc, argv, "joy_twist"); //initialize node
	JoyTwist joy_twist; //create instance
	ros::spin(); //let ros takeover (ros loop, deactivate through ctrl+c)
}
