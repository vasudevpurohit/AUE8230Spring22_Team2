### Files included in this directory:

(i)   build_ros_model.sh - shell command script that builds the package
(ii)  Creating Standalone Nodes.pptx - instructions to build the package
(iii) wander2.slx - Simulink node for obstacle avoidance
(iv)  wander.tgz - zip folder containing all the generated .cpp and associated header files

To build the package:

(i) The steps to build the package using the Simulink model are included in the presentation

(ii) Launch the world using the command 'roslaunch assignment5_wallfollowingandobstacleavoidance turtlebot3_obstacles.launch'

(iii) 'rosrun wander2 wander2' -- wander2 (package) & wander2 (node)

Results:

(i) Gazebo
![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/Standalone_Node/obstacleAvoidance.gif)

(ii) HW
