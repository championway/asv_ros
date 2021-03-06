#!/usr/bin/env python
import numpy as np
import roslib
import rospy
import tf
import struct
import math
import time
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from sensor_msgs.msg import Imu, NavSatFix
from std_msgs.msg import String

class CHECK_SIGNAL():
    def __init__(self):
        self.node_name = rospy.get_name()

        self.send_no_signal = False
        self.start = False

        rospy.loginfo("[%s] Initializing " %(self.node_name))

        self.time_start = rospy.get_time()
        self.time_threshold = rospy.get_param("~sec", 4.0)
        
        # self.pub_lookahead = rospy.Publisher("lookahead_point", Marker, queue_size = 1)
        # self.pub_robot_goal = rospy.Publisher("robot_goal", RobotGoal, queue_size = 1)
        self.pub_log_str = rospy.Publisher("signal/log_str",String, queue_size=1)

        self.gps_sub = rospy.Subscriber("/mavros/global_position/raw/fix", NavSatFix, self.gps_cb, queue_size = 1, buff_size = 2**24)
        self.imu_sub = rospy.Subscriber("/mavros/imu/data", Imu, self.imu_cb, queue_size = 1, buff_size = 2**24)

        rospy.Timer(rospy.Duration(1), self.event_cb)

    def event_cb(self, event):
        if not self.start:
            return
        ss = String()
        if (rospy.get_time() - self.time_start) > self.time_threshold:
            ss.data = "No signal"
            if not self.send_no_signal:
                self.srv_no_signal()
        else:
            ss.data = "Got signal"
            if self.send_no_signal:
                self.srv_got_signal()
        self.pub_log_str.publish(ss)

    def gps_cb(self, msg):
        if not self.start:
            self.start = True
            rospy.loginfo("Start to check signal!!!")
        self.time_start = rospy.get_time()


    def imu_cb(self, msg):
        quat = (msg.orientation.x,\
                msg.orientation.y,\
                msg.orientation.z,\
                msg.orientation.w)
        _, _, yaw = tf.transformations.euler_from_quaternion(quat)

    def srv_no_signal(self):
        #rospy.wait_for_service('/set_path')
        rospy.loginfo("SRV: No signal")
        set_bool = SetBoolRequest()
        set_bool.data = True
        try:
            srv = rospy.ServiceProxy('no_signal', SetBool)
            resp = srv(set_bool)
            self.send_no_signal = True
            return resp
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def srv_got_signal(self):
        #rospy.wait_for_service('/set_path')
        rospy.loginfo("SRV: Got signal")
        set_bool = SetBoolRequest()
        set_bool.data = False
        try:
            srv = rospy.ServiceProxy('no_signal', SetBool)
            resp = srv(set_bool)
            self.send_no_signal = False
            return resp
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

if __name__ == '__main__':
    rospy.init_node('CHECK_SIGNAL')
    foo = CHECK_SIGNAL()
    rospy.spin()