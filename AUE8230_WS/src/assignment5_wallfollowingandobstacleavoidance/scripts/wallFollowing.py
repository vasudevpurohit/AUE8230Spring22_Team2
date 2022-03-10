#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WallFollowing():
    def __init__(self):
        
        #initializing the node
        rospy.init_node('wallFollowing',anonymous=True)
        self.vel_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)          #publisher - velocity commands
        self.scan_sub = rospy.Subscriber('/scan',LaserScan,self.scan_update)    #subscriber - Laser scans, callback function that stores the subscribed data in a variable
        self.rate = rospy.Rate(10)
        self.laser_scan90 = 1 #random value
        self.laser_scan270 = 1 #random value
        self.lookahead_dist = 1 #random value
        
    def scan_update(self,data):
        window = 15
        self.lookahead_dist = data.ranges[0]
        self.laser_scan90 = (sum(data.ranges[89-window:89+window]))/30
        self.laser_scan270 = (sum(data.ranges[269-window:269+window]))/30
        
    def currentError(self):
        d_90 = self.laser_scan90
        d_270 = self.laser_scan270
        return d_90-d_270
    
    def pController_lat(self,error_lat):
        pGain_lat = 0.2
        return pGain_lat*error_lat
    
    def pController_long(self,dist):
        pGain_long = 0.1
        return pGain_long*dist

    def wallFollowing(self):
        self.vel_msg = Twist()
           
        while not rospy.is_shutdown():
           lin_x = self.pController_long(min(3.5,self.lookahead_dist))
           #changing the angular about z based on the error value
           self.vel_msg.linear.x = lin_x
           error_lat = self.currentError()
           ang_z = min(self.pController_lat(error_lat),0.15)
           self.vel_msg.angular.z = ang_z
            
           #publishing these values
           self.vel_pub.publish(self.vel_msg)
           self.rate.sleep()
           
if __name__=='__main__':
    try:
        x = WallFollowing()
        x.wallFollowing()
    except rospy.ROSInterruptException: pass
