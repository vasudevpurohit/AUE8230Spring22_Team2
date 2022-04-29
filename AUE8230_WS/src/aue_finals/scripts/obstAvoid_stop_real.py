#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:32:11 2022

@author: vasudev
"""
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import CompressedImage
from apriltag_ros.msg import AprilTagDetectionArray
import cv2
import time

err=0
line_switch = 0

class LineFollower(object):

    def __init__(self):
        self.bridge_object = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/image_color/compressed",CompressedImage,self.camera_callback)
        self.scan_sub = rospy.Subscriber('/tag_detections',AprilTagDetectionArray,self.tag_update)    #subscriber - Laser scans, callback function that stores the subscribed data in a variable
        self.pub_vel = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
        self.line_flag = 0
        self.switchtoLineMode = 0
        self.stop_flag = 0
        self.lineMode_counter = 0
        self.Xtag = 0
        self.Ztag = 0
        self.aprilTagflag = 0
        
    def tag_update(self,data):
        if len(data.detections) > 0:
            self.Xtag = data.detections[0].pose.pose.pose.position.x
            self.Ztag = data.detections[0].pose.pose.pose.position.z
        
    def camera_callback(self, data):
        # We select bgr8 because its the OpneCV encoding by default
        #cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        img_arr = np.frombuffer(data.data, np.uint8)
        cv_image = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

        # We get image dimensions and crop the parts of the image we dont need
        height, width, channels = cv_image.shape
        crop_img = cv_image[int((height/2)+30):int((height/2)+100)][1:int(width)]
        #crop_img = cv_image[340:360][1:640]

        # Convert from RGB to HSV
        hsv = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)

        # creating a perspective transform to get a better estimate of where the lanes begin
        #src = np.float32([[(width/2)-100,(height/2)+500],[(width/2)+100,(height/2)+500],[(width/2)-200,height],[(width/2)+200,height]])
        #dst = np.float32([[0,0],[width,0],[0,height],[width,height]])
        #T = cv2.getPerspectiveTransform(src,dst)
        #warp = cv2.warpPerspective(cv_image, T, (width,height))
        #warp = cv2.cvtColor(warp, cv2.COLOR_BGR2HSV)    

        # Define the Yellow Colour in HSV

        """
        To know which color to track in HSV use ColorZilla to get the color registered by the camera in BGR and convert to HSV. 
        """
        # Threshold the HSV image to get only yellow colors
        lower_yellow = np.array([26,102,50])	
        upper_yellow = np.array([68,255,255])
        #mask1 = cv2.inRange(warp, lower_yellow, upper_yellow)
        mask2 = cv2.inRange(hsv, lower_yellow, upper_yellow)
        pix = np.count_nonzero(mask2)                            #adding the number of illuminated pixels to prevent false switches to line-following
        

        ##-------------------STOP SIGN DETECTION-------------------------------
        #cropping the image
        height2, width2, channels2 = cv_image.shape
        crop_img2 = cv_image[int((height2/2)-300):int((height2/2))][1:int(width2)]
        black_mask = np.zeros(crop_img2.shape[:2], dtype="uint8")
        cv2.rectangle(black_mask, (0, 0), (int(width2/2),height), 255, -1)
        crop_img2 = cv2.bitwise_and(crop_img2, crop_img2, mask=black_mask)
        crop_img2 = cv2.GaussianBlur(crop_img2,(5,5),1)         #denoising
        gray = cv2.cvtColor(crop_img2, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        
        #converting to a HSV
        #stop_img = cv2.cvtColor(crop_img2, cv2.COLOR_BGR2HSV)
        
        #filtering out the red colored portion -- stop sign
        #lower_red = np.array([90,95,99])	
        #upper_red = np.array([179,255,255])
        #red = cv2.inRange(stop_img, lower_red, upper_red)
        
        contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(crop_img2, contours, -1, (0, 255, 0), 3)
        num_sides = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area >=720:      #the area for the hexagon is roughly 5000 when it is first detected
                perimeter = cv2.arcLength(contour, True)
                e = 0.01*perimeter #The bigger the fraction, the more sides are chopped off the original polygon
                simple_contour = cv2.approxPolyDP(contour, epsilon=e, closed=True)
                num_sides = simple_contour.shape[0]
                #print(num_sides)
                if num_sides == 8:
                    pass
                    #print(area, num_sides)

        twist_object = Twist()
        
        # Calculate the centroid only when the bot is right in front of it -- only then the line following mode will be exhibited
        #m1 = cv2.moments(mask1,False)

        # Calculate centroid of the blob of binary image using ImageMoments --- normal operation once the bot is near the yellow line
        m2 = cv2.moments(mask2, False)
        
        try:
            cx2, cy2 = (m2['m10']/m2['m00']), m2['m01']/m2['m00']
        except ZeroDivisionError:
            cx2, cy2 = height/2, width/2
            
        # if m1['m00'] ==0 and self.line_flag==0:simple_contour.shape
        #     #print("No Line in Bird's eye")
        #     pass
            
        # if m1['m00'] > 0:
        #     self.switchtoLineMode = 1
        #     #print("Line found in birds eye!")
            
        ##-----------line following normal behaviour--------------------------            
        if  m2['m00'] > 0 and pix>1500 and self.aprilTagflag == 0:
            global line_switch
            line_switch = 1
            #line_followSwitch = obsAvoid(self.line_switch)
            #self.line_flag = self.line_flag + 1
            global err
            err = width/2 - cx2
            #print(err)
            if abs(err)>45:
                twist_object.angular.z = 0.002*err
                twist_object.linear.x = 0.002
            else:
                twist_object.angular.z = 0.006*err
                twist_object.linear.x = 0.1
                
            self.pub_vel.publish(twist_object)
            print("Line Following Mode")
            
            ##-----------------stop sign detection---------------------------            
            if self.stop_flag == 0 and num_sides==8:
                self.stop_flag = 1
                #print("Time to rest!")
                t1 = rospy.Time.now().to_sec()
                time = 0
                print("Resting!")
                while time < 5:
                    t2 = rospy.Time.now().to_sec()
                    time= t2-t1
                    twist_object.angular.z = 0
                    twist_object.linear.x = 0
                    self.pub_vel.publish(twist_object)
                    
        elif self.Xtag !=0 and self.Ztag != 0:
            self.aprilTagflag = 1
            gain_x = 0.2
            gain_z = -5
            
            if self.Ztag >= 0.4:
                twist_object.linear.x = self.Ztag*gain_x
                twist_object.angular.z = self.Xtag*gain_z
                print("AprilTag Detected!")
                self.pub_vel.publish(twist_object)
            else:
                twist_object.linear.x = 0
                twist_object.angular.z = 0
                self.pub_vel.publish(twist_object)

                
        ##-----------line following mode but line searching-------------------    
        # elif m2['m00'] == 0 and self.switchtoLineMode == 1 and self.line_flag >= 0:
        #     twist_object.angular.z = 0.1
        #     twist_object.linear.x = 0
        #     self.pub_vel.publish(twist_object)
        #     #print("Line following -- searching for a line")
            
        ##---------------continue to obstacle avoidance-----------------------
        
        elif m2['m00'] == 0 and line_switch == 1:
            twist_object.angular.z = 0.09
            #line_switch = 0
            print("Obs-back!")
        
        else:
            #print(line_switch)
            ("Still in Obstacle Avoidance")
            pass

        cv2.circle(mask2,(int(cx2), int(cy2)), 5,(0,0,255),-1)
        cv2.imshow("MASK", mask2)
        #cv2.imshow("Crop", crop_img)
        #cv2.imshow("Original",cv_image)
        #cv2.imshow("Transformed",warp)
        cv2.imshow("Edges",edges)
        cv2.waitKey(1)
        
class obsAvoid():
    def __init__(self):
        self.pub = rospy.Publisher("/cmd_vel",Twist, queue_size=10)
        self.sub = rospy.Subscriber("/scan",LaserScan, self.laserCallback)
        self.start_mode = 0
        #self.line_switch = line_switch
        
    def laserCallback(self,data):
        twist_object=Twist()
        #taking out the unwanted values
        wanted_data = []
        for i in data.ranges:
            if i>3.5:
                wanted_data.append(3.5)
            else:
                wanted_data.append(i)
        
        #following values used only to move the bot in the first section
        scan90 = min(3.5,wanted_data[90])
        scan270 = min(3.5,wanted_data[270])    
        
        #straightahead distance
        window_str = 20
        straight = np.minimum(3.5,(np.mean(wanted_data[0:window_str])+np.mean(wanted_data[360-window_str:360]))/2)
        
        #left front and right front
        #window_fr = 30
        front_lfr = np.mean(wanted_data[15:40])           #left front
        front_rfr = np.mean(wanted_data[330:345])     #right front
        #print(front_lfr,front_rfr)
        
        #left and right
        #window_lr = 20
        left = np.mean(wanted_data[60:100])
        right = np.mean(wanted_data[260:300])
        
        #setting the base speeds for the bot
        lin_x = 0.2
        ang_z = 0.5
        
        if line_switch ==0:
            print("Obstacle Avoidance Mode")
        #exhibit different behaviors based on where the bot is wrt to the obstacles ahead
            if (scan90 >=2.5 and scan270>=2.5) and self.start_mode == 0:
                twist_object.linear.x = 0.22
                twist_object.angular.z = 0
                #print("Start Mode")
            

            elif front_lfr < 0.25 or front_rfr < 0.25:      
                twist_object.linear.x = 0                #the bot if it is too close to the obstacle and only rotate in free space
                twist_object.angular.z = ang_z*(front_lfr-front_rfr)*(1/straight)*0.7
                self.start_mode = 1
                #print("1",vel_msg.angular.z)
                #print("Too Close")
                
            elif (front_lfr >= 0.25 and front_lfr <= 0.8) or (front_rfr >=0.25 and front_rfr <= 0.8):
                twist_object.linear.x = straight*lin_x*0.8
                twist_object.angular.z = 0.95*(ang_z*(front_lfr-front_rfr)*2) + 0.09*(ang_z*(left-right)*1) + 0.065*(1/straight)*np.sign(front_lfr-front_rfr)
                self.start_mode = 1
                #print("Close")
                #print("2",vel_msg.angular.z)
            elif front_lfr > 0.8 and front_rfr > 0.8:
                twist_object.linear.x = lin_x*0.75
                twist_object.angular.z = ang_z*(left-right)*(1/straight)*0.85
                self.start_mode =1
                #print("Space Ahead")
                #print("3",vel_msg.angular.z)

            self.pub.publish(twist_object)
        
def main():
    
    rospy.init_node('line_following_node', anonymous=True)
    
    lineFollow = LineFollower()
    rate = rospy.Rate(5)
    
    if err==0 and line_switch == 0:
        obstacleAvoid=obsAvoid()
    
    ctrl_c = False
    def shutdownhook():
        # Works better than rospy.is_shutdown()
        obstacleAvoid.clean_up()
        rospy.loginfo("Shutdown time!")
        ctrl_c = True
    rospy.on_shutdown(shutdownhook)
    while not ctrl_c:
        rate.sleep()

if __name__ == '__main__':

        main()