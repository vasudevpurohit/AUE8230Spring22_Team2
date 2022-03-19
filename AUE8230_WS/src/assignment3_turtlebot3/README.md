## AuE8230 - Autonomy Sciences & Systems - Team 2


### assignment3_turltebot3 (AUE8230WS/src/assignment3_turtlebot3)

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
