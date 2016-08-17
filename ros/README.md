#Installing ROS (indigo package)
--adding the ROS repository
sudo vi /etc/apt/sources.list.d/ros-latest.list
```deb http://packages.ros.org/ros/ubuntu trusty main``` (in ros-latest.list)

--install package authentication key
wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key
sudo apt-key add ros.key
rm ros.key

--download package list
sudo apt-get update

--install ROS package
sudo apt-get install ros-indigo-desktop-full

--install simple simulator turtlesim
sudo apt-get install ros-indigo-turtlesim

--install gazebo (actually installing software for ROS and Gazebo to work together)
sudo apt-get install ros-indigo-gazebo-ros-pkgs ros-indigo-gazebo-ros-control

--initialize rosdep
sudo rosdep init
rosedep update

--setting environment variabls
source /opt/ros/indigo/setup.bash (add this to .bashrc also)
export |grep ROS (for checking)

##Package
--list and locate
rospack list

--find package
rospack find [package-name]

--inspect package
rosls [package-name]

--move to package file
roscd [package-name]

##executing
--initialize ROS
roscore (this should not be exit except when finishing with ROS)

--for python
python [filename].py
(or convert to executable file to be used on rosrun)
chmod 755 [filename].py (need to have #!/usr/bin/env python at top of file)

--executing node
rosrun [package-name] [executable-name]

--list running node
rosnode list

--inspect node
rosnode info [node-name] (obtain from rosnode list)

--kill node
rosnode kill [node-name] (avoid using Ctrl-C)

--kill unknown node (useful for eliminating any unwanted node)
rosnode cleanup

--see relationchart
rqt_graph

--edit node
rosed [package-name] [filename]

--check topic list (same as rqt_graph but as text)
rostopic list (-v: all info, -p: publish info only, -s:subscribe info only)

--publish topic
rostopic pub [topic-name] [message-type] [message]

--echo message
rostopic echo [topic-name] (obtain from rostopic list)

--publication rate
rostopic hz [topic-name] (message per second)
rostopic bw [topic-name] (bytes per second)

--inspect topic
-rostopic info [topic-name]

--inspect message type
rosmsg show [message-type-name] ( obtained from insepct topic)

--publish message manually 
rostopic pub [topic-name] [message-type] [message-content] (YAML method)
-or-
(bash method, cannot use tab for auto command)
rostopic pub -r [rate-in-hz] [topic-name] [message-type] [message-content]
rostopic pub -r 1 /turtle1/cmd_vel geometry_msg/Twist '[2,0,0]' '[0,0,0]' (ex)

--override default name (useful for activating same package multiple times)
rosrun [package-name] [executable-name] __name:=[new name]

--check for erros
roswtf

##Create own package
* mkdir [your workspace]
* mkdir src in your [workspace]
catkin_create_pkg [package-name] (your own package name, execute in src/)
(or)
catkin_create_pkg [package-name] roscpp rospy etc (for build, run depend)

###writin program
* have header file ros/ros.h for every ROS program
* register program as node

###Compile method
--Declare dependencies
(on CMakeList.txt)
find_package(catkin REQUIRED COMPONENTS package-names)
(on package.xml)
<build_depend>package-names</build_depend> (dependcies during build)
<run_depend>package-names</run_depend> (dependcies during execution)

--declare executable
(on CMakeList.txt)
add_executable(executable-name source-files)
target_link_libraries(executable-name ${catkin_LIBRARIES})

--make
(on your workspace directory)
catkin_make

--create changelog.rst
catkin_generate_changelog

--preparation for putting into ROS repository or upgrade version (need changelog)
catkin_prepare_release

--initialize workspace (only needs to be done once)
catkin_init_workspace

--find workspace
catkin_find
(or)
catkin_find [package-name]


--sourcing
source devel/setup.bash (only needed to do once for each terminal)

--execute
rosrun [package-name] [executable files] (make sure roscore is on!)

##Publisher
```
ros::NodeHandle [node-handle];
ros::Publisher pub = *node-handler*.advertise<message_type>(topic_name, queue_size)
```

##Subscriber
subscriber need callback function since it does not know when topic is publish therefore
```
void *function_name*(const *package_name*::*type_name* &msg){
...}
```
to subscride,
```
ros::Subscriber sub = *node_handler*.subscribe(*topic_name*, *queue_size*, *pointer_to_callback_funtion*)
```

###places where stem goes
* console or file
* rosout
* log files

--put to file
use ROS_INFO_STREAM
command > file (for normal)
command & > file (for normal and error)
stdbuf -oL command & > file (to put normal and error in normal order)
(ros inset ansi color codes. to view with them )
less -r file

--adjust file output
```
export ROSCONSOLE_FORMANT='[${severity}] [${time}]: ${message}'
```
(other option: thread, logger, file, line, function node)

--see all stream output on rosout
rostopic echo /rosout
(or)
rqt_console

--see on log files
(on roscore at the end of file)
setting /run_id to [run-id]
(or)
rosparam get /run_id

vi ~/.ros/log[run-id]/rosout.log

--deleting log files
files will accumulate over time, taking disk space
roscore and roslaunch will warn you but will not delete files
(to check)
rosclean check
(to delete log files)
rosclean purge

--enable, disable log level
(while node is executed)
```
rosservice call /node-name/set_logger_level ros.packate-name level
```
(level: DEBUG, INFO, WARN, ERROR, FATAL)
(on gui might be better)
rqt_logger_level
(level can also be change directly on program)

##Graph resource name
* Global name (Begin with /. ROS's default namespace)
* Relative name (Begin without /. If possible create your own to avoid name collison. Also create flexibility, easier to build complicated system tby composing smaller part)
* Private name (Begin with ~. often used for parameters. can be access if one knows full address)
* Anonymous names (ROS automatically create unique name for each node, same program can be run multiple times)

##ROS Launch files
Instead of having to one by one activate roscore and other nodes use roslaunch
save [filename].launch on the workspace/src/[package-name] directory
no need to start roscore
rosrun is start one node, roslaunch is start many node at once

--executing
roslaunch [package-name] [launch-file-name] (can use direct directory to launch files instead but use only during experiment)

-for verbosity (extra info)
roslanch -v [package-name] [launch-file-name]

--how to create launch files
save as [filename].launch. it is xml file
all command should be written within the root element, 
```
<launch>
...
</launch>
```
launching node is
```
<node
	pkg="package-name"
	type="executable-name"
	name="node-name" (name="$(anon [base-name])" for anonoymous name in launch file. be careful to use different base name)
/>
```
--log files
standard output is redirected to log files which can be found in
~/.ros/log/[run-id]/[node-name-number]-stdout.log
to override this put
```
output="screen"
```
in node section of launch file
(or)
roslaunch --screen [package-name] [launch-file-name] (for all node)

--respawn
```
respawn="true"
```
if node terminate prematurarely, ROS automatically re activate the node

--requried
```
required="true"
```
if node terminate permaturearly, ROS terminate other node. useful for abandoning session instead due inability to gracfully restart.

--launching node in their own windows
roslaunch activate all node in a single terminal. to hav seperate window for node use
```
launch-prefix="[command-prefix]"
```
ex. xterm -e (equal to xterm -e rosrun ...)
can also be gdb or valgrind etc.

--renampping name(useful for changing publisher/subscriber without directly changing the source code)
[command] [original-name]:=[new-name]
(or in launch file)
<node [node-attribute]>
	<remap from="[original-name]" to="[new-name"] />
	...
</node>

--including other launch files
<include file="[path to file]"i/>
(or)
<include file="$(find [package-name])/[filename]"/>
(also allow namespace change)
<include file="..." ns="[namespace]" />

--argument or args
<arg name="[arg-name]" default="[arg-value]"/> (default can be override)
<arg name="[arg-name]" value="[arg-value]"/> (value cannot be ovverride)
(to access args value)
$(arg [arg-name])

--sending argument value to include launch files
<include files=...>
	<arg name="[arg-name]" value="$(arg [arg-name])" />
</include>

--creating group(useful for pushing several nodes in same ns and conditionally enable or disable node)
(latter ns will be used)
<group ns="[namespace]" />
...
</group>
(conditional if 1 include, if 0 ignore)
<group if="[0 or 1]"/>
...
</group>
(opposite of if)
<group unless="[1 or 0]"/>
...
</group>

##parameter server
--listing parameters
rosparam list

--read parameter value
rosparam get [parameter-name]

--read all parameter value
rosparam get [namespace]

--set parameters to server (if using new parameters, set this before running program)
rosparam set [parameter-name] [parameter-value]

--update new parameters
rosservice call /clear

--save parameters to file
rosparam dump [filename] [namespace]

--load file to parameters
rosparam load [filename] [namespace]

--set param through launch file
<param name="[param-name]" value="[param-value"] />

--set private param through launch file (children of node element)
<node ...>
	<param name..>
</node>

--read parameter through launch file
<rosparam command="load" file="[path to file"]/>
(or)
<rosparam command="load" file="$(find [package-name])/[param file]" />


--execute param through python
python [filename].py _[parameter_name]:=[parameter_value]

##Service
client -> request -> server
server -> respond -> client

--list all service
rosservice list

--list service of node
rosnode info [node-name]

--list node offering service
rosservice node [service-name]

--show service data type
rosservice info [service-name]

--inspect service data type
rossrv show [service-data-type-name]
(data before --- is request, after --- is respond)

     |Topics|Services
-----|------|--------
active things|rostopics|rosservice
data types|rosmsg|rosserv

--call service from command line
rosservice call [service-name] [request-content] (content depend on type)

--initialize own service
roscd [package-name]
mkdir srv/
touch [filename].srv
(in package.xml)
	<build_depend>message_generation</build_depend>
	<run_depend>message_runtime</run_depend>
(in CMakeLists.txt)
		find_packate(catkin REQUIRED COMPONENTS
			roscpp
			...
			message_generation
		)
		add_service_files(
			FILES
			[filename].srv
		)
		generate_messages(
			DEPENDENCIES
			std_msgs
		)
catkin_make

--in [filename].srv
[message-type] [name] (INPUT)
---
[message-type] [name] (OUTPUT)

##Recording and prelaying messages

--Recording bag files
rosbag record -O [filename].bag [topic-names] (use -a to record all topics)

--replay bag files
rosbag play [filename].bag

--inspect bag files
rosbag info [filename].bag

--compress rosbag file
rosbag compress [filename].bag

--decompress rosbag file
rosbag decompress [filename].bag

--filter only one topic (when you record all and need only one)
rosbag filter [filename].bag [newfilename].bag "topic=='[topic-name]'"

--filter multiple topic
rosbag filter [filename].bag [newfilename].bag "topic=='[topic-name]'" or "topic== ...

--revert bag files to origin
rosbag reindx [filename].bag

--check if bag file can be used in current ROS system
rosbag check [filename].bag

--migrate bag files if version is different
rosbag fix [filename].bag [newfilename].bag

--record from launch files--
<node 
	pkg="rosbag"
	name="record"
	type="record"
	arg="-o [filename].bag [topic-names]"
/>

--replay from launch files--
<node
	pkg="rosbag"
	name="play"
	type="play"
	arg="[filename].bag"
/>

###Actionlib
Topic is sending or receiving message without knowing who or what is happening.Service is used between two parties where client wait until processs is finished. However in a case where process takes too long, service will not proceed until a response is obtained. For process that takes a while but still want some sort of periodic response or do some other task while waiting for process, use ActionLib

--initialize actionlib
rosed [package-name]
mkdir action/
touch [filename].action
(in CMakeLists.txt)
	find_packages(catkin REQUIRED COMPONENTS
		roscpp
		...
		message_generation
		actionlib_msgs
	)
	add_action_files(
		FILES
		[filename].action
	)
	generate_messages(
		DEPENDENCIES
		...
		actionlib_msgs
	)
catkin_make

--in [filename].action
[message-type] [name] (GOAL)
---
[message-type] [name] (RESULT)
---
[message-type] [name] (FEEDBACK)


###create python library in ROS
roscd [package-name]
mkdir -p src/[package-name] (there should be two folders with same name)
touch src/[package-name]/__init__.py
(create setup.py)
```python
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
setup_args = generate_distutils_setup(
	packages=['ros_start'], #your package name
	package_dir={'':'src'},
)
setup(**setup_args)
```
(in CMakeLists.txt)
	catkin_python_setup()
catkin_make

###GUIs
--activate RViz
rosrun rviz rviz

--rosrun rqt ez publisher
rosrun rqt_ez_publisher rqt_ez_publisher

--activate rqt plot
rqt_plot [topic-name]

###connect to controllers
--install joy package
sudo apt-get install ros-indigo-joy
sudo apt-get install ros-indigo-teleop-twist-joy

--check connection
ls /dev/input (should have jsX where X = 0,1,2...n)
sudo jstest /dev/input/jsX (X in input found in ls)
ls -l /dev/input/jsX
(if crw-rw--- then sudo chmod a+rw /dev/input/jsX)
rosrun joy joy_node
rostopic echo joy



