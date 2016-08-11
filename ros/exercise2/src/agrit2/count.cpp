//This program periodically generates log messages at various severity levels

#include <log4cxx/logger.h>
#include <ros/ros.h>

int main(int argc, char **argv){
	//Initialize the ROS system and become a node
	ros::init(argc, argv, "count_and_log");
	ros::NodeHandle nh;

	log4cxx::Logger::getLogger(ROSCONSOLE_DEFAULT_NAME)->setLevel(
		ros::console::g_level_lookup[ros::console::levels::Debug]
	);
	ros::console::notifyLoggerLevelsChanged();

	//Generate log messages of varying severity regularly
	ros::Rate rate(10);
	for (int i=1; ros::ok(); i++){
		ROS_DEBUG_STREAM("Counted_to_" << i);
		if((i % 3) == 0){
			ROS_INFO_STREAM(i << "_is_divisible_by_3");
		}
		if((i % 5) == 0){
			ROS_WARN_STREAM(i << "_is_divisible_by_5");
		}
		if((i % 10) ==0){
			ROS_ERROR_STREAM(i << "_is_dvisible_by_10");
		}
		if((i % 20) ==0){
			ROS_FATAL_STREAM(i << "_is_divisible_by_20");
		}
		rate.sleep();
	}

}
