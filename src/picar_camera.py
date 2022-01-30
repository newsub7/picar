#!/usr/bin/env python

import rospy
import sys
import pwd
import os
from std_msgs.msg import String
import cv2
from Libs import picarx
import time



if __name__ == '__main__':
    try:
        px = picarx.Picarx()
        px.forward(30)
        time.sleep(10)
        px.stop();
    except rospy.ROSInterruptException:
        pass