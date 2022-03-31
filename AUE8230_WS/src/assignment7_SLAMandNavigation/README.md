## AuE8230 - Autonomy Sciences & Systems - Team 2

Complete implementation videos have been added [here](https://drive.google.com/drive/folders/14WX3gEQ5_MGe7tOSRgXkQndp_xGBLtUT)

### assignment6_trackingandfollowing (AUE8230WS/src/assignment6_trackingandfollowing)
#### Part 1
The implementation shown below is executed using the SLAM & Navigation launch files for two different mapping methods: 

For the purpose of SLAM we created an area using cardboard boxes as objects and walls of the room as bounding walls for the turtlebot to run

-(a) G-MAPPING 

The process below shows the turtlebot being operated via Tele-operation (bottom of the screen) and the SLAM map being built in the Rviz, all of this done using the Assignment7_slam_real.launch file

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/videos/Part1/G_Mapping/G_mapping_SLAM.gif) 

The same process shown above being run on the actual Turtlebot3

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/videos/Part1/G_Mapping/G_mapping_SLAM_real.gif) 

Once SLAM process was complete, the turtlebot was given the task to Navigate the same world setup by using the pre-defined turtlebot3_navigation node launched by the Assignment7_Navigation.launch as:\

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/videos/Part1/G_Mapping/G_mapping_Navigation.gif) 

The same process shown on the real turtlebot3\

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/videos/Part1/G_Mapping/G_mapping_Navigation_real.gif) 

-(b) Karto SLAM\

The process below shows the turtlebot being operated via Tele-operation (bottom of the screen) and the SLAM map being built in the Rviz, all of this done using the Assignment7_slam_karto_real.launch file

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/videos/Part1/Karto/Karto_SLAM.gif) 

The same process shown above being run on the actual Turtlebot3

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/videos/Part1/Karto/Karto_SLAM_real.gif) 

Once SLAM process was complete, the turtlebot was given the task to Navigate the same world setup by using the pre-defined turtlebot3_navigation node launched by the Assignment7_Navigation.launch as:

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/videos/Part1/Karto/Karto_Navigation.gif) 

The same process shown on the real turtlebot3

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/videos/Part1/Karto/Karto_Navigation_real.gif) 

##### CONCLUSION: 

-1. Karto SLAM method forms more dense occupancy grid compared to G-Mapping 

-2. Localization is difficult in both methods and requires to use the 2-D pose estimate functionality of Rviz 

-3. Navigation in Karto SLAM formed map is better as it even allows to traverse long path through a series of Obstacle as shown below: 

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/videos/Part1/Karto/Karto_navigation_Bonus.gif) 

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/videos/Part1/Karto/Karto_navigation_real_bonus.gif) 

#### Part2
The objective of part2 was to compare the performance of different LIDAR's in different Gazebo world setup. The performance is being compared on the visual quality of the SLAM map each method generate.

For the purpose of this assignment, the following LIDAR were used:

-1. LDS 
-2. Hukoyo 

For LDS Lidar, we ran gazebo simulation with raising level of compelxity in terms of object placement, 

The Assignment7_SLAM_Gazebo.launch file is used to acheive the following maps as end results

-1. Gazebo Default World 

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/images/Part2/map_world_lds.png)

-2. Gazebo Stage4 

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/images/Part2/map_stage4_lds.png)

-3. House 

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/images/Part2/map_house_lds.png)

For Hukoyo Lidar, we first added the provided stl file and update the urdf and xacro files to accomodate the new lidar.

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/images/Part2/hokuyo_turtlebot3.png)

The same Assignment7_SLAM_Gazebo.launch file is used to spawn the turtlebot, launch the default SLAM node and tele-op it to perform SLAM.

But, we were unable to visualize any MAP being built in Rviz. We encountered that following error: "Map not received" 

We used ros topic list to identify the topics being published and their value. After viewing the RQT graph for the new Hukoyo Lidar and comparing it with the LDS Lidar setup's RQT graph, 

we reached the consensus that the Hukoyo Lidar in Gazebo is publishing it's scan data on to the topic : hukoyo3d/points 

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/images/Part2/hukoyo_rqt_graph.jpeg)

where as the SLAM node subscribes to the topic "scan". as shown in LDS RQT shown below: 

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/images/Part2/lds_rqt_graph.png)

Therefore this change of Topic's name made the SLAM node incompatible with the Hukoyo Lidar and hence, even though we were able to visualize the point cloud of 

empty world, the map around thr turtlebot was not being build. 

We also tried remapping the frame and topic name in the SLAM node launch file as shown below: 

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/images/Part2/Remapping.png)

But still got the final error as this, here the tranform between the reframed topic and Map does not exist. 

![](https://github.com/vasudevpurohit/AUE8230Spring22_Team2/blob/master/AUE8230_WS/src/assignment7_SLAMandNavigation/images/Part2/Final_error.png)
 


