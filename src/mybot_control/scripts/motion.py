#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('red_light_green_light')

red_light_twist = Twist()
green_light_twist = Twist()

green_light_twist.linear.x = 0.2
green_light_twist.angular.z = 0.0

red_light_twist.linear.x = -0.2
red_light_twist.linear.y = 0.0

driving_forward = False
light_change_time = rospy.Time.now()
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    if driving_forward:
        cmd_vel_pub.publish(green_light_twist)
        print "green light"
    else:
        # cmd_vel_pub.publish(red_light_twist)
        print "red light"

    time_now = rospy.Time.now()
    print("time: %d" % light_change_time.secs)

    if time_now > light_change_time:
        driving_forward = not driving_forward
        light_change_time = rospy.Time.now() + rospy.Duration(3)
    rate.sleep()
