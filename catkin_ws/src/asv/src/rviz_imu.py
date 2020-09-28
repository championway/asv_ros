#!/usr/bin/env python
import numpy as np
import roslib
import rospy
import tf
import struct
import math
import time
from geometry_msgs.msg import Pose, PoseStamped
from sensor_msgs.msg import Imu, NavSatFix

class RVIZ_IMU():
    def __init__(self):
        self.node_name = rospy.get_name()

        rospy.loginfo("[%s] Initializing " %(self.node_name))

        self.pub_imu_pose = rospy.Publisher("/rviz/imu", PoseStamped, queue_size = 1)

        self.imu_sub = rospy.Subscriber("/mavros/imu/data", Imu, self.imu_cb, queue_size = 1, buff_size = 2**24)

    def imu_cb(self, msg):
        quat = (msg.orientation.x,\
                msg.orientation.y,\
                msg.orientation.z,\
                msg.orientation.w)
        _, _, yaw = tf.transformations.euler_from_quaternion(quat)
        p = PoseStamped()
        p.header = msg.header
        p.header.frame_id = "map"
        p.pose.position.x = 0
        p.pose.position.y = 0
        p.pose.position.z = 0
        p.pose.orientation.x = msg.orientation.x
        p.pose.orientation.y = msg.orientation.y
        p.pose.orientation.z = msg.orientation.z
        p.pose.orientation.w = msg.orientation.w
        self.pub_imu_pose.publish(p)


if __name__ == '__main__':
    rospy.init_node('rviz_imu')
    foo = RVIZ_IMU()
    rospy.spin()