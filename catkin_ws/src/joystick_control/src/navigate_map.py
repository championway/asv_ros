#!/usr/bin/env python
import numpy as np
import roslib
import rospy
import tf
import struct
import math
import time
from geometry_msgs.msg import PoseArray, Pose, PoseStamped, Point
from nav_msgs.msg import Odometry
from asv_msgs.msg import RobotGoal
from asv_msgs.srv import SetRobotPath, SetRobotPathResponse
from std_srvs.srv import SetBool, SetBoolResponse
from cv_bridge import CvBridge, CvBridgeError

class NAVIGATE_MAP():
	def __init__(self):
		self.node_name = rospy.get_name()
		self.goals = []
		self.robot_position = []
        self.map_img = np.zeros((180, 280, 3), np.uint8)
        self.map_img[:,:] = (255, 255, 255)

		rospy.loginfo("[%s] Initializing " %(self.node_name))
		
		# self.pub_robot_goal = rospy.Publisher("robot_goal", RobotGoal, queue_size = 1)
		self.path_srv = rospy.Service("set_path", SetRobotPath, self.path_cb)
		rospy.Subscriber("odometry", Odometry, self.odom_cb, queue_size = 1, buff_size = 2**24)

	def odom_cb(self, msg):
		self.robot_position = [msg.pose.pose.position.x, msg.pose.pose.position.y]

	def path_cb(self, req):
		res = SetRobotPathResponse()
		if len(req.data.list) > 0:
			self.goals = req.data.list
			self.get_path = True
		res.success = True
		return res

	def map(self):
		x_range = (max_x - min_x) + 10
		y_range = (max_y - min_y) + 10
		w = self.map_img.shape[1]
        h = self.map_img.shape[0]
        ratio_w = w/float(x_range)
        ratio_h = h/float(y_range)
        ratio = min(ratio_w, ratio_h)
        if ratio
        cv_image = cv2.resize(cv_image, (w, h), interpolation=cv2.INTER_CUBIC)

if __name__ == '__main__':
	rospy.init_node('NAVIGATE_MAP')
	foo = NAVIGATE_MAP()
	rospy.spin()