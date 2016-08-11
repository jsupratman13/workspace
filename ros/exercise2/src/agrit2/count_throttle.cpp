//this program generate log messages at varying severity levels, throttled to various maximum speeds (stream at interval)
//generally not good as it uses more computation speed

#include <ros/ros.h>

int main(int argc, char **argv){
	ros::init(argc, argv, "log_throttled");
	ros::NodeHandle nh;

	while(ros::ok()){
		ROS_DEBUG_STREAM_THROTTLE(0.1, "Debug appear every 0.1s");
		ROS_INFO_STREAM_THROTTLE(0.3, "Info appear every 0.3s");
		ROS_WARN_STREAM_THROTTLE(0.5, "Warn appear every 0.5s");
		ROS_ERROR_STREAM_THROTTLE(1.0, "Error appear every 1s");
		ROS_FATAL_STREAM_THROTTLE(2.0, "Fatal appear every 2s");
	}
}
