#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import cv2
#import picarx from Picarx

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('pi_camera_node')
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        hello_str = "Hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass