## AuE8230 - Autonomy Sciences & Systems - Team 2

### assignment6_trackingandfollowing (AUE8230WS/src/assignment6_trackingandfollowing)

The implementation below uses packages that were built from the traditional method of catkin_create_pkg with the .py script included in the launch file<br /> 
(a) 'follow_line_step_hsv.py' - makes the turtlebot3 burger wander until it finds a line, and then tracks the line

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment6_trackingandfollowing/videos/lineFollowing.gif)

(b) 'follow_line_step_hsv_hw.py' - Lane-following implementation on actual TurtleBot3 burger

Results of deploying the node on actual H/W can be found [here](https://drive.google.com/drive/folders/1fWwCdGmC59jA5oUrCSfM3Srx6M4Gqdbt)

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment6_trackingandfollowing/videos/lineFollowing_hw.gif)


(c) 'aprilTag.py' - AprilTag following implementation on actual TurtleBot3 burger

Results of deploying the node on actual H/W can be found [here](https://drive.google.com/drive/folders/1--Xq9xvodqCL1KsBRXHhZ6JZGmKQe2g9)

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment6_trackingandfollowing/videos/aprilTag_hw.gif)

To run the codes, run the commands below mentioned below\

(i) Lane-following node-\
-'roslaunch assignment6_trackingandfollowing turtlebot3_follow_line.launch

(ii) AprilTag node-\
-'roslaunch assignment6_trackingandfollowing aprilTag.launch'
