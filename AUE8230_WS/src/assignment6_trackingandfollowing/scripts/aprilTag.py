#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from apriltag_ros.msg import AprilTagDetectionArray


class tagFollow():
    def __init__(self):
        
        #initializing the node
        rospy.init_node('apriltag',anonymous=True)
        self.vel_pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)          #publisher - velocity commands
        self.scan_sub = rospy.Subscriber('/tag_detections',AprilTagDetectionArray,self.tag_update)    #subscriber - Laser scans, callback function that stores the subscribed data in a variable
        self.rate = rospy.Rate(10)
        self.x = 0
        self.z = 0
    
    def tag_update(self,data):
        self.x = data.detections[0].pose.pose.pose.position.x
        self.z = data.detections[0].pose.pose.pose.position.z

    def follow(self):
            self.vel_msg = Twist()
               
            while not rospy.is_shutdown():
               gain_x = 0.2
               gain_z = -5
               
               if self.z >= 0.4:
                   self.vel_msg.linear.x = self.z*gain_x
                   self.vel_msg.angular.z = self.x*gain_z
               
               else:
                   self.vel_msg.linear.x = 0
                   self.vel_msg.angular.z = 0
               
               #publishing these values
               self.vel_pub.publish(self.vel_msg)
               self.rate.sleep()
           
if __name__=='__main__':
    try:
        bot = tagFollow()
        bot.follow()
    except rospy.ROSInterruptException: pass
