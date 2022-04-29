#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:43:49 2022

@author: vasudev
"""
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import CompressedImage

class LineFollower(object):

    def __init__(self):
        self.bridge_object = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/image_color/compressed",CompressedImage,self.camera_callback)
        #self.moveTurtlebot3_object = MoveTurtlebot3()
        self.vel_pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
        
    def nothing(self):
        pass
	
    def camera_callback(self, data):
        # We select bgr8 because its the OpneCV encoding by default
        #cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        img_arr = np.frombuffer(data.data, np.uint8)
        cv_image = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        
        # We get image dimensions and crop the parts of the image we dont need
        height, width, channels = cv_image.shape
        crop_img = cv_image[int((height/2)+30):int((height/2)+200)][1:int(width)]
        #crop_img = cv_image[340:360][1:640]
        
        
        # Create a window
        cv2.namedWindow('image')
        
        cv2.createTrackbar('HMin', 'image', 0, 179, self.nothing)
        cv2.createTrackbar('SMin', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('VMin', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('HMax', 'image', 0, 179, self.nothing)
        cv2.createTrackbar('SMax', 'image', 0, 255, self.nothing)
        cv2.createTrackbar('VMax', 'image', 0, 255, self.nothing)

        # Set default value for Max HSV trackbars
        cv2.setTrackbarPos('HMax', 'image', 179)
        cv2.setTrackbarPos('SMax', 'image', 255)
        cv2.setTrackbarPos('VMax', 'image', 255)

        # Initialize HSV min/max values
        hMin = sMin = vMin = hMax = sMax = vMax = 0
        phMin = psMin = pvMin = phMax = psMax = pvMax = 0

        while(1):
            # Get current positions of all trackbars
            hMin = cv2.getTrackbarPos('HMin', 'image')
            sMin = cv2.getTrackbarPos('SMin', 'image')
            vMin = cv2.getTrackbarPos('VMin', 'image')
            hMax = cv2.getTrackbarPos('HMax', 'image')
            sMax = cv2.getTrackbarPos('SMax', 'image')
            vMax = cv2.getTrackbarPos('VMax', 'image')

            # Set minimum and maximum HSV values to display
            lower = np.array([hMin, sMin, vMin])
            upper = np.array([hMax, sMax, vMax])

            # Convert to HSV format and color threshold
            hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower, upper)
            result = cv2.bitwise_and(crop_img, crop_img, mask=mask)

            # Print if there is a change in HSV value
            if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
                print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
                phMin = hMin
                psMin = sMin
                pvMin = vMin
                phMax = hMax
                psMax = sMax
                pvMax = vMax

            # Display result image
            cv2.imshow('image', result)
            cv2.waitKey(1)
            #if cv2.waitKey(10) & 0xFF == ord('q'):
                #break

def main():
    rospy.init_node('line_following_node', anonymous=True)
    line_follower_object = LineFollower()
    rate = rospy.Rate(5)
    ctrl_c = False
    def shutdownhook():
        # Works better than rospy.is_shutdown()
        line_follower_object.clean_up()
        rospy.loginfo("Shutdown time!")
        ctrl_c = True
    rospy.on_shutdown(shutdownhook)
    while not ctrl_c:
        rate.sleep()

if __name__ == '__main__':
        main()