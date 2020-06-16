#!/usr/bin/env python
import numpy as np
import roslib
import rospy
import tf
import struct
import math
import sys
import time
from geodesy.utm import UTMPoint, fromLatLong
from geometry_msgs.msg import Pose, Point
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from sensor_msgs.msg import Imu, NavSatFix

class GET_PATH():
    def __init__(self):
        self.node_name = rospy.get_name()

        rospy.loginfo("[%s] Initializing " %(self.node_name))

        file_name = ""

        if len(sys.argv) != 2:
            file_name = "path"
        else:
            file_name = sys.argv[1]


        self.file = open(file_name + ".txt" , 'w')

        self.flush_count = 0
        self.pose = Pose()
        self.pre_pose = Pose()
        self.pre_time = rospy.get_time()
        self.time_threshold = 4.
        self.dis_threshold = 5.
        self.first = True
        self.gps = NavSatFix()

        self.lat_orig = rospy.get_param('~latitude', 0.0)
        self.long_orig = rospy.get_param('~longitude', 0.0)
        self.utm_orig = fromLatLong(self.lat_orig, self.long_orig)
        
        self.gps_sub = rospy.Subscriber("/mavros/global_position/raw/fix", NavSatFix, self.cb_gps, queue_size = 1, buff_size = 2**24)

    def cb_gps(self, msg_gps):
        self.gps = msg_gps
        if self.flush_count < 5:
            # rospy.loginfo("[%s] Flush Data" %self.node_name)
            self.flush_count = self.flush_count + 1
            self.utm_orig = fromLatLong(msg_gps.latitude, msg_gps.longitude)
            return

        utm_point = fromLatLong(msg_gps.latitude, msg_gps.longitude)
        self.pose.position.x = utm_point.easting - self.utm_orig.easting
        self.pose.position.y = utm_point.northing - self.utm_orig.northing
        self.pose.position.z = 0

        if self.first:
            self.first = False
            self.save_point()
            return

        if self.distance(self.pre_pose, self.pose) > self.dis_threshold:
            self.save_point()
        elif (rospy.get_time() - self.pre_time) > self.time_threshold:
            self.save_point()

    def save_point(self):
        # write to txt
        self.pre_pose.position.x = self.pose.position.x
        self.pre_pose.position.y = self.pose.position.y
        self.pre_time = rospy.get_time()
        self.file.write(str(self.gps.latitude) + ", " + str(self.gps.longitude) + "\n")
        self.file.flush()

    def distance(self, p1, p2):
        return math.sqrt((p1.position.x - p2.position.x)**2 + (p1.position.y - p2.position.y)**2)

    def on_shutdown(self):
        self.file.close()

if __name__ == '__main__':
    rospy.init_node('GET_PATH')
    foo = GET_PATH()
    rospy.on_shutdown(foo.on_shutdown)
    rospy.spin()