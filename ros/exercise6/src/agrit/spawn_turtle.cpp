//This program spawns a new turtlesim turtle by calling the appropriate service
#include <ros/ros.h>

//The srv class for the service
#include <turtlesim/Spawn.h>

int main(int argc, char **argv){
	ros::init(argc, argv, "spawn_turtle");
	ros::NodeHandle nh;

	//Create a client object for the spawn service. This needs to know the data type of the service and its name
	ros::ServiceClient spawnClient = nh.serviceClient<turtlesim::Spawn>("spawn");

	//Create the request and response objects (can check using rossrv show)
	turtlesim::Spawn::Request req;
	turtlesim::Spawn::Response resp;

	//Fill in the request data members
	req.x = 2;
	req.y = 3;
	req.theta = M_PI/2;
	req.name = "Leo";

	//Actually call the service. This wont return until the service is complete
	bool success = spawnClient.call(req,resp);

	//Check for success and use the response
	if (success) {
		ROS_INFO_STREAM("Spawn a turtle name " <<resp.name);
	}
	else{
		ROS_ERROR_STREAM("Failed to spawn.");
	}
}

