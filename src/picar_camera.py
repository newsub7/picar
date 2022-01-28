import rospy
from std_msgs.msg import String
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

if __name__ == '__main__':
    rospy.init_node('pi_camera_node')
    
    
    