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
import urllib2
from std_msgs.msg import String

class CHECK_INTERNET():
    def __init__(self):
        self.node_name = rospy.get_name()

        self.send_no_internet = False
        self.url = 'http://site.baidu.com/'

        rospy.loginfo("[%s] Initializing " %(self.node_name))

        self.time_start = rospy.get_time()
        self.time_threshold = rospy.get_param("~sec", 4.0)
        self.pub_log_str = rospy.Publisher("internet/log_str",String, queue_size=1)

        rospy.Timer(rospy.Duration(1.2), self.event_cb)

    def event_cb(self, event):
        ss = String()
        if self.internet_on(self.url):
            self.time_start = rospy.get_time()
        if (rospy.get_time() - self.time_start) > self.time_threshold:
            ss.data = "No Internet"
            if not self.send_no_internet:
                print("No Internet")
                self.srv_no_internet()
        else:
            ss.data = "Got Internet"
            if self.send_no_internet:
                print("Got Internet")
                self.srv_got_internet()
        self.pub_log_str.publish(ss)

    def internet_on(self, url):
        try:
            urllib2.urlopen(url, timeout = self.time_threshold)
            return True
        except urllib2.URLError as err:
            return False

    def srv_no_internet(self):
        #rospy.wait_for_service('/set_path')
        rospy.loginfo("SRV: No signal")
        set_bool = SetBoolRequest()
        set_bool.data = True
        try:
            srv = rospy.ServiceProxy('estop', SetBool)
            resp = srv(set_bool)
            self.send_no_internet = True
            return resp
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def srv_got_internet(self):
        #rospy.wait_for_service('/set_path')
        rospy.loginfo("SRV: Got signal")
        set_bool = SetBoolRequest()
        set_bool.data = False
        try:
            srv = rospy.ServiceProxy('estop', SetBool)
            resp = srv(set_bool)
            self.send_no_internet = False
            return resp
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

if __name__ == '__main__':
    rospy.init_node('CHECK_INTERNET')
    foo = CHECK_INTERNET()
    rospy.spin()
