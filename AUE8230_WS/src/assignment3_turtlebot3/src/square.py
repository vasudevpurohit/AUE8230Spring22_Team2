#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def move():
	rospy.init_node('turtlebot2',anonymous=True)
	rate = rospy.Rate(10)
	vel_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 10)
	bot_vel = Twist()

#finding the distance travelled by each robot based on the time elapsed
	i = 0
	while (i < 4):
		current_distance = 0
		while (current_distance < 2):
		    t0 = rospy.Time.now().to_sec()
		    #linear speed = 0.2 unit/s && angular speed = 0.2 rad/s
		    bot_vel.linear.x = 0.2
		    bot_vel.linear.y = 0
		    bot_vel.linear.z = 0
		    bot_vel.angular.x = 0
		    bot_vel.angular.y = 0
		    bot_vel.angular.z = 0
		    vel_publisher.publish(bot_vel)
		    t1 = rospy.Time.now().to_sec()
		    #calculating the distance travelled
		    current_distance = current_distance + 0.2*(t1-t0)

		bot_vel.linear.x = 0
		vel_publisher.publish(bot_vel)

		current_orientation = 0
		t0 = rospy.Time.now().to_sec()
	#turning the bot by 90deg to align with the next side
		while (current_orientation < ((math.pi)/2)):
		    bot_vel.angular.z = 0.2
		    vel_publisher.publish(bot_vel)
		    t1 = rospy.Time.now().to_sec()
		    current_orientation = 0.2*(t1-t0)

	bot_vel.angular.z = 0
	vel_publisher.publish(bot_vel)
	i = i+1


if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException: pass
