#!/usr/bin/env python
import numpy as np
import cv2
import roslib
import rospy
import tf
import math
import time
from geometry_msgs.msg import PoseArray, Pose, PoseStamped, Point
from visualization_msgs.msg import Marker, MarkerArray
from nav_msgs.msg import Odometry
import rospkg
from asv_msgs.msg import RobotGoal, MotorCmd
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest

from PID import PID_control

class DIVING_CONTROL():
	def __init__(self):
		self.node_name = rospy.get_name()
		rospy.loginfo("[%s] Initializing " %(self.node_name))
		self.start_diving = False
		self.time_start = time.time()
		self.dive_srv = rospy.Service("dive", SetBool, self.dive_cb)
		rospy.Timer(rospy.Duration(1), self.timer_cv)

	def timer_cv(self, event):
		if not self.start_diving:
			return
		duration = time.time() - self.time_start
		if (duration >= 10):
			self.time_start = time.time()
			self.finish_diving()
			#print "Time's up"

	def dive_cb(self, req):
		if req.data == True:
			rospy.loginfo("Start Diving")
			self.time_start = time.time()
			self.start_diving = True
		else:
			rospy.loginfo("Stop Diving")
			self.start_diving = False
		res = SetBoolResponse()
		res.success = True
		res.message = "recieved"
		return res

	def finish_diving(self):
		#rospy.wait_for_service('/set_path')
		rospy.loginfo("SRV: Send finish diving")
		set_bool = SetBoolRequest()
		set_bool.data = True
		try:
			srv = rospy.ServiceProxy('finish_diving', SetBool)
			resp = srv(set_bool)
			self.start_diving = False
			return resp
		except rospy.ServiceException, e:
			print "Service call failed: %s"%e

if __name__ == '__main__':
	rospy.init_node('Diving_control')
	foo = DIVING_CONTROL()
	rospy.spin()
