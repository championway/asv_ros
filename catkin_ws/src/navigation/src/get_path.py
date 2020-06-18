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
from asv_msgs.srv import SetString, SetStringResponse
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from sensor_msgs.msg import Imu, NavSatFix

class GET_PATH():
    def __init__(self):
        self.node_name = rospy.get_name()

        rospy.loginfo("[%s] Initializing " %(self.node_name))

        # file_name = ""

        # if len(sys.argv) != 2:
        #     file_name = "path"
        # else:
        #     file_name = sys.argv[1]


        # self.file = open(file_name + ".txt" , 'w')

        self.file = None

        self.flush_count = 0
        self.pose = Pose()
        self.pre_pose = Pose()
        self.pre_time = rospy.get_time()
        self.time_threshold = 3.5.
        self.dis_threshold = 5.
        self.first = True
        self.gps = NavSatFix()
        self.isRecording = False

        self.record_srv = rospy.Service("/ASV/record_path", SetString, self.record_cb)
        self.save_srv = rospy.Service("/ASV/save_path", SetBool, self.save_cb)

        self.lat_orig = rospy.get_param('~latitude', 0.0)
        self.long_orig = rospy.get_param('~longitude', 0.0)
        self.utm_orig = fromLatLong(self.lat_orig, self.long_orig)
        
        self.gps_sub = rospy.Subscriber("/mavros/global_position/raw/fix", NavSatFix, self.cb_gps, queue_size = 1, buff_size = 2**24)

    def save_file(self, fname):
        self.file = open(fname + ".txt", "w")
        self.isRecording = True

    def close_file(self):
        self.isRecording = False
        if self.file is None:
            return
        self.file.close()
        self.flush_count = 0
        self.first = True

    def cb_gps(self, msg_gps):
        if not self.isRecording:
            return
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
        rospy.loginfo("Save")
        self.pre_pose.position.x = self.pose.position.x
        self.pre_pose.position.y = self.pose.position.y
        self.pre_time = rospy.get_time()
        self.file.write(str(self.gps.latitude) + ", " + str(self.gps.longitude) + "\n")
        self.file.flush()

    def record_cb(self, req):
        if req.str != "":
            rospy.loginfo("Start Recording")
            self.save_file(req.str)
        res = SetStringResponse()
        res.success = True
        return res

    def save_cb(self, req):
        if req.data == True:
            rospy.loginfo("Save File") 
            self.close_file()          
        res = SetBoolResponse()
        res.success = True
        res.message = "recieved"
        return res

    def distance(self, p1, p2):
        return math.sqrt((p1.position.x - p2.position.x)**2 + (p1.position.y - p2.position.y)**2)

    def on_shutdown(self):
        if self.file is not None:
            self.file.close()

if __name__ == '__main__':
    rospy.init_node('GET_PATH')
    foo = GET_PATH()
    rospy.on_shutdown(foo.on_shutdown)
    rospy.spin()