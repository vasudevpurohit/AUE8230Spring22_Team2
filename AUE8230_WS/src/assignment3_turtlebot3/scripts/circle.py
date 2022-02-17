#!/usr/bin/env python3

#code to make a bot move in a circle with a constant twist velocity

#importing all the neccessary libraries


import rospy
from geometry_msgs.msg import Twist

def move():
    #initializing a node
    rospy.init_node('turtlebot1')
    rate = rospy.Rate(10)
    
    #publisher message
    vel_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    vel_msg = Twist()
        
    #moving the robot with the set speed
    while True:
    	vel_msg.linear.x = 0.3
    	vel_msg.linear.y = 0
    	vel_msg.linear.z = 0
    	vel_msg.angular.x = 0
    	vel_msg.angular.y = 0
    	vel_msg.angular.z =0.3
    
    	vel_pub.publish(vel_msg)
    	rate.sleep()
    
move()
