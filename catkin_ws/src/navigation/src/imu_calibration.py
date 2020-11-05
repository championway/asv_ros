#!/usr/bin/env python
import numpy as np
import roslib
import rospy
import tf
import struct
import math
import time
from geometry_msgs.msg import PoseArray, Pose, PoseStamped, Point
from visualization_msgs.msg import Marker, MarkerArray
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from std_msgs.msg import UInt32
from control.cfg import lookaheadConfig
from asv_msgs.srv import SetRobotPath, SetRobotPathResponse
from std_srvs.srv import SetBool, SetBoolResponse
import rospkg
import yaml
import os

class IMUCalibration():
	def __init__(self):
		self.start = False
		self.end = False

		self.node_name = rospy.get_name()
		self.imu_sum = 0
		self.imu_cnt = 0
		self.imu_avg = 0.
		self.imu_threshold = 0.75

		self.odom = []
		self.odom_start = 0
		self.odom_end = 0
		self.odom_slope = 0.

		self.calibrate_value = 0.

		rospack = rospkg.RosPack()
		self.imu_param_path = os.path.join(rospack.get_path('asv_config'), "calibration/imu.yaml")
		self.imu_param = None

		with open (self.imu_param_path, 'r') as file:
			self.imu_param = yaml.safe_load(file)

		rospy.loginfo("[%s] Initializing " %(self.node_name))
		
		self.start_srv = rospy.Service("start_imu_calibration", SetBool, self.start_cb)
		self.end_srv = rospy.Service("end_imu_calibration", SetBool, self.end_cb)
		self.save_srv = rospy.Service("save_imu_calibration", SetBool, self.save_cb)
		self.reset_srv = rospy.Service("reset_imu_calibration", SetBool, self.reset_cb)
		

		rospy.Subscriber("/ASV/odometry", Odometry, self.odom_cb, queue_size = 1, buff_size = 2**24)
		# rospy.Subscriber("/imu/data", Imu, self.imu_cb, queue_size = 1, buff_size = 2**24)
		
	def imu_cb(self, msg):
		if self.start and not self.end:
			quat = (msg.orientation.x,\
					msg.orientation.y,\
					msg.orientation.z,\
					msg.orientation.w)
			_, _, angle = tf.transformations.euler_from_quaternion(quat)
			while angle >= np.pi:
				angle = angle - 2*np.pi
			while angle < -np.pi:
				angle = angle + 2*np.pi
			if self.imu_cnt > 0:
				if abs(angle - self.imu_avg) < self.imu_threshold: # prevent noise
					self.imu_cnt += 1
					self.imu_sum += angle
					self.imu_avg = self.imu_sum / self.imu_cnt
			else: # first data
				self.imu_cnt += 1
				self.imu_sum += angle
				self.imu_avg = self.imu_sum / self.imu_cnt

	def odom_cb(self, msg):
		quat = (msg.pose.pose.orientation.x,\
				msg.pose.pose.orientation.y,\
				msg.pose.pose.orientation.z,\
				msg.pose.pose.orientation.w)
		_, _, angle = tf.transformations.euler_from_quaternion(quat)

		self.odom = [msg.pose.pose.position.x, msg.pose.pose.position.y]

		if self.start and not self.end:
			while angle >= np.pi:
				angle = angle - 2*np.pi
			while angle < -np.pi:
				angle = angle + 2*np.pi
			if self.imu_cnt > 0:
				if abs(angle - self.imu_avg) < self.imu_threshold: # prevent noise
					self.imu_cnt += 1
					self.imu_sum += angle
					self.imu_avg = self.imu_sum / self.imu_cnt
			else: # first data
				self.imu_cnt += 1
				self.imu_sum += angle
				self.imu_avg = self.imu_sum / self.imu_cnt

	def reset_cb(self, req):
		if req.data == True:
			self.start = False
			self.end = False
			self.imu_sum = 0
			self.imu_cnt = 0
			self.imu_avg = 0.
			self.imu_threshold = 0.75
			self.odom = []
			self.odom_start = 0
			self.odom_end = 0
			self.odom_slope = 0.
		res = SetBoolResponse()
		res.success = True
		res.message = "recieved"
		return res

	def start_cb(self, req):
		if req.data == True:
			self.odom_start = self.odom[:]
			self.start = True
		res = SetBoolResponse()
		res.success = True
		res.message = "recieved"
		return res

	def end_cb(self, req):
		if req.data == True:
			self.odom_end = self.odom[:]
			self.end = False
			self.calibration()
		res = SetBoolResponse()
		res.success = True
		res.message = "recieved"
		return res

	def save_cb(self, req):
		if req.data == True:
			self.save_calibrate_result()
		res = SetBoolResponse()
		res.success = True
		res.message = "recieved"
		return res

	def calibration(self):
		theta = self.get_angle()
		self.calibrate_value = self.imu_avg - theta
		print(self.imu_avg, theta, self.calibrate_value)

	def save_calibrate_result(self):
		try:
			self.imu_param["imu"] = float(self.calibrate_value)
			with open(self.imu_param_path, "w") as file:
				yaml.dump(self.imu_param, file)
			rospy.loginfo("Done calibration")
		except:
			pass

	def get_angle(self):
		delta_x = self.odom_end[0] - self.odom_start[0]
		delta_y = self.odom_end[1] - self.odom_start[1]
		theta = np.arctan2(delta_y, delta_x)
		return theta

	def get_odom_slope(self):
		x1 = self.odom_start[0]
		y1 = self.odom_start[1]
		x2 = self.odom_end[0]
		y2 = self.odom_end[1]
		delta_x = x2 - x1
		delta_y = y2 - y1
		m = None
		if delta_x != 0: # if not vertical
			m = (y2 - y1)/(x2 - x1)
			if delta_x < 0:
				m = -m
		return m

	# Calculate the angle difference between robot heading and vector start from start_pose, end at end_pose and unit x vector of odom frame, 
	# in radian
	def getAngle(self):
		if self.pre_pose == []:
			return
		delta_x = self.robot_position[0] - self.pre_pose[0]
		delta_y = self.robot_position[1] - self.pre_pose[1]
		theta = np.arctan2(delta_y, delta_x)
		angle = theta - self.imu_angle
		# Normalize in [-pi, pi)
		while angle >= np.pi:
			angle = angle - 2*np.pi
		while angle < -np.pi:
			angle = angle + 2*np.pi
		# print(theta, self.imu_angle, abs(angle))
		return abs(angle)

	def get_goal_angle(self, robot_yaw, robot, goal):
		robot_angle = np.degrees(robot_yaw)
		p1 = [robot[0], robot[1]]
		p2 = [robot[0], robot[1]+1.]
		p3 = goal
		angle = self.get_angle(p1, p2, p3)
		result = angle - robot_angle
		result = self.angle_range(-(result + 90.))
		return result

	def angle_range(self, angle): # limit the angle to the range of [-180, 180]
		if angle > 180:
			angle = angle - 360
			angle = self.angle_range(angle)
		elif angle < -180:
			angle = angle + 360
			angle = self.angle_range(angle)
		return angle

	def get_distance(self, p1, p2):
		return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

if __name__ == '__main__':
	rospy.init_node('IMUCalibration')
	foo = IMUCalibration()
	rospy.spin()
