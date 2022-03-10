## AuE8230 - Autonomy Sciences & Systems - Team 2

This repository consists of all the scripts during the duration of this course.

## Team 2 consists of the following members:
Chirag Mutha\
Rithvik Reddy Pindi\
Udit Rathee\
Vasudev Purohit

## A workspace has been created that holds all the packages developed during this course. Following is a list of all the packages:

### 1. assignment3_turltebot3 (AUE8230WS/src/assignment3_turtlebot3)

(a) 'square.py' - makes the turtlebot3 move in gazebo in a square with a constant linear velocity in x and constant angular velocity about z

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment3_turtlebot3/videos/square.gif)

(b) 'circle.py' - makes the turtlebot3 move in gazebo in a circle with a constant twist velocity

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment3_turtlebot3/videos/circle.gif)

(c) 'turtlebot3_wall.py' - emergency braking logic to make the turtlebot3 stop at a threshold distance defined by the user

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment3_turtlebot3/videos/emergency_brake.gif)

To run the codes, follow the steps mentioned below

(i) To simulate scenarios (a) and (b) run the command-<br /> 
'roslaunch assignment3_turtlebot3 move.launch code:=circle' --> to run the circle script\
'roslaunch assignment3_turtlebot3 move.launch code:=square' --> to run the square script

(ii) To simulate scenario (c) run the command-\
'roslaunch assignment3_turtlebot3 turtlebot3_wall.launch'

### 2. assignment5_wallfollowingandobstacleavoidance (AUE8230WS/src/assignment5_wallfollowingandobstacleavoidance)

The implementation below uses packages that were built from the traditional method of catkin_create_pkg with the .py script included in the launch file\ 
(a) 'wallFollowing.py' - makes the turtlebot3 burger follow the walls present in the Gazebo map

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment5_wallfollowingandobstacleavoidance/videos/wallFollowing.gif)

(b) 'obstacleAvoidance.py' - makes the turtlebot3 burger wander in a Gazebo environment

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment5_wallfollowingandobstacleavoidance/videos/wander.gif)

To run the codes, run the commands below mentioned below\

(i) Wall-following node-\
-'roslaunch assignment5_wallfollowingandobstacleavoidance turtlebot3_wallfollowing.launch

(ii) Wander node-\
-'roslaunch assignment5_wallfollowingandobstacleavoidance turtlebot3_obstacles.launch'

Results of deploying the node on actual H/W can be found [here](https://drive.google.com/drive/folders/1-5eiNoA9bVsNyNHob1AXqxvZAVP8I73d) 

Alternatively stand-alone nodes can be created from a Simulink model that does the same job. For example, an obstacle avoidance node was created on Simulink using\
ROS libraries available on Simulink. A detailed presentation describing the steps involved is included. Follow the steps mentioned below to run the node:

(i) The steps to build the package using the Simulink model are included in the presentation

(ii) Launch the world using the command 'roslaunch assignment5_wallfollowingandobstacleavoidance turtlebot3_obstacles.launch'

(iii) 'rosrun wander2 wander2' -- wander2 (package) & wander2 (node)

Results:

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/Standalone_Node/obstacleAvoidance.gif)

