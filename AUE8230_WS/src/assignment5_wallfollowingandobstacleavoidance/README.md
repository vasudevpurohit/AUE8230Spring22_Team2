## AuE8230 - Autonomy Sciences & Systems - Team 2

### assignment5_wallfollowingandobstacleavoidance (AUE8230WS/src/assignment5_wallfollowingandobstacleavoidance)

The implementation below uses packages that were built from the traditional method of catkin_create_pkg with the .py script included in the launch file<br /> 
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

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment5_wallfollowingandobstacleavoidance/videos/wander_2.gif)

#### Alternatively 
Stand-alone nodes can be created from a Simulink model that does the same job. For example, an obstacle avoidance node was created on Simulink using ROS libraries available on Simulink. A detailed presentation describing the steps involved is included in the 'Standalone_Node' directory of this repo.
