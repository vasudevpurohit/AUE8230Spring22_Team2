#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import CompressedImage
#from move_robot import MoveTurtlebot3

class LineFollower(object):

    def __init__(self):
        self.bridge_object = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/image_color/compressed",CompressedImage,self.camera_callback)
        #self.moveTurtlebot3_object = MoveTurtlebot3()
        self.vel_pub = rospy.Publisher("/cmd_vel",Twist,queue_size=10)
        self.lineMode_counter = 0
	
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

        # Define the Yellow Colour in HSV

        """
        To know which color to track in HSV use ColorZilla to get the color registered by the camera in BGR and convert to HSV. 
        """

        # Threshold the HSV image to get only yellow colors
        lower_yellow = np.array([22,90,100])
        upper_yellow = np.array([179,255,255])
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        
        #cropping the image
        height2, width2, channels2 = cv_image.shape
        crop_img2 = cv_image[int((height2/2)-300):int((height2/2))][1:int(width2)]
        
        #converting to a HSV
        stop_img = cv2.cvtColor(crop_img2, cv2.COLOR_BGR2HSV)
        
        #filtering out the red colored portion -- stop sign
        lower_red = np.array([90,0,95])	
        upper_red = np.array([179,255,255])
        red = cv2.inRange(stop_img, lower_red, upper_red)
        
        contours, hierarchy = cv2.findContours(red,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(crop_img2, contours, -1, (0, 255, 0), 3)
        num_sides = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area >= 10000:                #the area for the hexagon is roughly 5000 when it is first detected
                perimeter = cv2.arcLength(contour, True)
                e = 0.01*perimeter #The bigger the fraction, the more sides are chopped off the original polygon
                simple_contour = cv2.approxPolyDP(contour, epsilon=e, closed=True)
                num_sides = simple_contour.shape[0]
                #print(num_sides)
                #print(area)
     

        # Calculate centroid of the blob of binary image using ImageMoments
        m = cv2.moments(mask, False)

        try:
            cx, cy = m['m10']/m['m00'], m['m01']/m['m00']
            counter = 1
            self.lineMode_counter = self.lineMode_counter + 1
        except ZeroDivisionError:
            cx, cy = (height/2), (width/2)
            counter = 0
            
        if counter ==1 and m['m10'] >= 70000000 and m['m10'] <= 150000000 and self.lineMode_counter >= 10:
            print("Detected",m['m10'])
        else:
            print("Not Detected",m['m10'])
                
            
        # Draw the centroid in the resultut image
        # cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]]) 
        #cv2.circle(mask,(int(cx), int(cy)), 10,(0,0,255),-1)
        #cv2.imshow("Original", cv_image)
        #cv2.imshow("MASK", mask)
        #cv2.imshow("Crop", crop_img)
        cv2.waitKey(1)
        
        #controller to keep in lane
        twist_object = Twist()
        
    
        
        #distance of the centroid of the blob w.r.t image centre
        err = width/2 - cx
        if abs(err)>45:
        	twist_object.angular.z = 0.003*err
        	twist_object.linear.x = 0.002
        else:
        	twist_object.angular.z = 0.0045*err
        	twist_object.linear.x = 0.05
        #rospy.loginfo("ANGULAR VALUE SENT===>"+str(twist_object.angular.z))
        #rospy.loginfo(err)
        # Make it start turning
        #self.moveTurtlebot3_object.move_robot(twist_object)
        #self.vel_pub.publish(twist_object)
        #rospy.sleep(2)

    def clean_up(self):
        self.moveTurtlebot3_object.clean_class()
        cv2.destroyAllWindows()

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
