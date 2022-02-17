#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class wallAvoidance():
    def __init__(self):
        
        #initializing the wall avoidance node
        rospy.init_node('wallAvoidance',anonymous=True)
        self.vel_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)          #publisher - velocity commands
        self.scan_sub = rospy.Subscriber('/scan',LaserScan,self.scan_update)    #subscriber - Laser scans
        self.rate = rospy.Rate(10)
        self.laser_currentDistance = 1 #random value
        
        
    def scan_update(self,data):
        self.laser_currentDistance = data.ranges[0]
        print(self.laser_currentDistance, data.ranges[0])
        
    def emergencyBrake(self):
        print(self.laser_currentDistance)
        self.vel_msg = Twist()
        #first setting a speed
        self.vel_msg.linear.x = 0.2
        self.vel_msg.linear.y = 0
        self.vel_msg.linear.z = 0
        self.vel_msg.angular.x = 0
        self.vel_msg.angular.y = 0
        self.vel_msg.angular.z = 0
        self.vel_pub.publish(self.vel_msg)
        threshold = 0.8
        
        #checking for the distance to apply brakes
        while  self.laser_currentDistance >= threshold:
            self.vel_msg.linear.x = 0.2   
            self.vel_pub.publish(self.vel_msg)
            
        self.vel_msg.linear.x = 0
        self.vel_pub.publish(self.vel_msg)
        
        rospy.spin()
if __name__=='__main__':
    try:
        x = wallAvoidance()
        x.emergencyBrake()
    except rospy.ROSInterruptException: pass
