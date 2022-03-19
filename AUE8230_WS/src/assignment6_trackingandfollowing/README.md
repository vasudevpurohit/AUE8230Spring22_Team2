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

Following set steps need to be run before launching the nodes mentioned above:\
(a) Launching the camera node on the turtlebot\
(b) Carrying out the extrinsic and intrinsic calibration to get the entire set of topics available from the camera\
(c) Running the tag detection node -- (since the apriltag package contains certain non-catkin files, catkin_make_isolated was used instead of catkin_make. Include 'source devel_isolated/setup.bash' to the .bashrc file for the apriltag packages to be included

Challenges faced:

(i)  The control frequency for the lane-following implementation was pretty low and was improved by increasing the rate at which the data was being published. This improved the performance significantly\
(ii) For the april tag implementation on actual bot, a major hurdle faced by the team was that of data transfer rate from the turtlebot3 to the remote PC being very low. This did not allow the tag pose to be detected. This is because the camera data is being published by the camera on the turtlebot and the tag detection package runs on the remote PC. To improve performance here, an image with a lesser information was used i.e., /camera/mono was used in place of /camera/image_color 

The LiDAR can be disconnected for this implementation to save battery!
