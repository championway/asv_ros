#!/usr/bin/env python
import numpy as np
import cv2
import roslib
import rospy
import rospkg
import yaml
import tf
import os
import struct
import math
import time
from sensor_msgs.msg import Image, LaserScan
from sensor_msgs.msg import CameraInfo
from geometry_msgs.msg import PoseArray, Pose, PoseStamped, Point
from visualization_msgs.msg import Marker, MarkerArray
from nav_msgs.msg import OccupancyGrid, MapMetaData, Odometry
import rospkg
from cv_bridge import CvBridge, CvBridgeError
from dynamic_reconfigure.server import Server
from control.cfg import pos_PIDConfig, ang_PIDConfig
from asv_msgs.msg import RobotGoal, MotorCmd
from std_srvs.srv import SetBool, SetBoolResponse
from asv_msgs.srv import SetValue, SetValueResponse, SetString, SetStringResponse

from PID import PID_control

class Robot_PID():
	def __init__(self):
		self.node_name = rospy.get_name()
		self.motor_mode = rospy.get_param("~motor_mode", 0)
		rospy.loginfo("Motor Mode: " + str(self.motor_mode))
		self.small_angle_thres = 0.35
		self.angle_mag = 1/2.5
		self.dis4constV = 5. # Distance for constant velocity
		self.alpha_p = 1.2
		self.alpha_a = 1.3
		self.pos_ctrl_max = 3
		self.pos_ctrl_min = 0.0
		# self.alpha_v = 1.0
		# self.pos_station_max = 0.8
		# self.pos_station_min = -0.8
		self.cmd_ctrl_max = 2.5
		self.cmd_ctrl_min = -2.5
		self.station_keeping_dis = 3.5 # meters
		self.frame_id = 'map'
		self.goal = None
		self.pid_parent = ["pos", "ang", "pos_bridge", "ang_bridge"]
		self.pid_child = ["kp", "ki", "kd"]
		rospack = rospkg.RosPack()
		if self.motor_mode == 0:
			self.pid_param_path = os.path.join(rospack.get_path('asv_config'), "pid/pid_0.yaml")
		elif self.motor_mode == 1:
			self.pid_param_path = os.path.join(rospack.get_path('asv_config'), "pid/pid_1.yaml")
		self.pid_param = None

		with open (self.pid_param_path, 'r') as file:
			self.pid_param = yaml.safe_load(file)

		rospy.loginfo("[%s] Initializing " %(self.node_name))

		# self.alpha_srv = rospy.Service("alphaV", SetValue, self.alpha_cb)
		self.param_srv = rospy.Service("param", SetString, self.param_cb)

		self.pub_cmd = rospy.Publisher("cmd_drive", MotorCmd, queue_size = 1)
		rospy.Subscriber('robot_goal', RobotGoal, self.robot_goal_cb, queue_size = 1, buff_size = 2**24)

		self.pub_goal = rospy.Publisher("goal_point", Marker, queue_size = 1)
		
		self.pos_control = PID_control("Position")
		self.ang_control = PID_control("Angular")

		self.pos_bridge_control = PID_control("Position_Bridge")
		self.ang_bridge_control = PID_control("Angular_Bridge")

		self.set_pid_param()

		# self.ang_station_control = PID_control("Angular_station")
		# self.pos_station_control = PID_control("Position_station")

		# self.pos_srv = Server(pos_PIDConfig, self.pos_pid_cb, "Position")
		# self.ang_srv = Server(ang_PIDConfig, self.ang_pid_cb, "Angular")
		# self.pos_station_srv = Server(pos_PIDConfig, self.pos_station_pid_cb, "Angular_station")
		# self.ang_station_srv = Server(ang_PIDConfig, self.ang_station_pid_cb, "Position_station")
		
		self.initialize_PID()

	def robot_goal_cb(self, msg):
		self.goal = [msg.goal.position.x, msg.goal.position.y]
		self.robot_position = [msg.robot.position.x, msg.robot.position.y]
		
		if msg.goal.position.x == msg.robot.position.x and msg.goal.position.y == msg.robot.position.y:
			# if station keeping
			cmd_msg = MotorCmd()
			cmd_msg.right = 0
			cmd_msg.left = 0
			cmd_msg.horizontal = 0
			self.pub_cmd.publish(cmd_msg)
			self.publish_goal(self.goal)
			return

		quat = (msg.robot.orientation.x,\
				msg.robot.orientation.y,\
				msg.robot.orientation.z,\
				msg.robot.orientation.w)
		_, _, yaw = tf.transformations.euler_from_quaternion(quat)

		if len(self.goal) == 0 or len(self.robot_position) == 0: # if the robot hasn't recieve any goal
			return

		#yaw = yaw + np.pi/2
		goal_distance = self.get_distance(self.robot_position, self.goal)
		goal_angle = self.get_goal_angle(yaw, self.robot_position, self.goal)
		
		pos_output, ang_output = 0, 0
		if goal_distance < self.station_keeping_dis:
			# rospy.loginfo("Station Keeping")
			# pos_output, ang_output = self.station_keeping(goal_distance, goal_angle)
			if (msg.mode.data == "bridge"):
				if (abs(goal_angle) < self.small_angle_thres):
					neg = (goal_angle < 0)
					goal_angle = self.small_angle_thres*((abs(goal_angle)/self.small_angle_thres)**self.angle_mag)
					if neg:
						goal_angle = -goal_angle
				pos_output, ang_output = self.bridge_control(goal_distance, goal_angle)
			else:
				pos_output, ang_output = self.control(goal_distance, goal_angle)
		else:
			if (msg.mode.data == "bridge"):
				if (abs(goal_angle) < self.small_angle_thres):
					neg = (goal_angle < 0)
					goal_angle = self.small_angle_thres*((abs(goal_angle)/self.small_angle_thres)*self.angle_mag)
					if neg:
						goal_angle = -goal_angle
				pos_output, ang_output = self.bridge_control(goal_distance, goal_angle)
			else:
				pos_output, ang_output = self.control(goal_distance, goal_angle)

		cmd_msg = MotorCmd()
		if self.motor_mode == 0: # three motors mode
			if not msg.only_angle.data: # for navigation
				cmd_msg.right = self.cmd_constarin(pos_output + ang_output)
				cmd_msg.left = self.cmd_constarin(pos_output - ang_output)
			else: # if only for rotation, instead of moving forward
				cmd_msg.right = self.cmd_constarin(ang_output)
				cmd_msg.left = self.cmd_constarin(ang_output)
		elif self.motor_mode == 1: # four motors mode
			if not msg.only_angle.data: # for navigation
				cmd_msg.right = self.cmd_constarin(pos_output)
				cmd_msg.left = self.cmd_constarin(pos_output)
				cmd_msg.horizontal = self.cmd_constarin(ang_output)
			else: # if only for rotation, instead of moving forward
				cmd_msg.horizontal = self.cmd_constarin(ang_output)
		self.pub_cmd.publish(cmd_msg)
		self.publish_goal(self.goal)

	def control(self, goal_distance, goal_angle):
		self.pos_control.update(goal_distance)
		self.ang_control.update(goal_angle)

		# pos_output will always be positive
		pos_output = self.pos_constrain(self.alpha_p*(-self.pos_control.output/self.dis4constV))

		# -1 = -180/180 < output/180 < 180/180 = 1
		ang_output = self.alpha_a*(self.ang_control.output/180.)
		return pos_output, ang_output

	def bridge_control(self, goal_distance, goal_angle):
		self.pos_bridge_control.update(goal_distance)
		self.ang_bridge_control.update(goal_angle)

		# pos_output will always be positive
		pos_output = self.pos_constrain(self.alpha_p*(-self.pos_bridge_control.output/self.dis4constV))

		# -1 = -180/180 < output/180 < 180/180 = 1
		ang_output = self.alpha_a*(self.ang_bridge_control.output/180.)
		return pos_output, ang_output

	def station_keeping(self, goal_distance, goal_angle):
		self.pos_station_control.update(goal_distance)
		self.ang_station_control.update(goal_angle)

		# pos_output will always be positive
		pos_output = self.pos_station_constrain(self.alpha_p*(-self.pos_station_control.output/self.dis4constV))

		# -1 = -180/180 < output/180 < 180/180 = 1
		ang_output = self.alpha_a*(self.ang_station_control.output/180.)

		# if the goal is behind the robot
		if abs(goal_angle) > 90: 
			pos_output = - pos_output
			ang_output = - ang_output
		return pos_output, ang_output

	def param_cb(self, req):
		s = req.str
		ss = s.split('/')
		string_valid = False
		if len(ss) == 3:
			if ss[0] in self.pid_parent:
				if ss[1] in self.pid_child:
					try:
						string_valid = True
						self.pid_param[ss[0]][ss[1]] = float(ss[2])
						with open(self.pid_param_path, "w") as file:
							yaml.dump(self.pid_param, file)
						self.set_pid_param()
					except:
						pass
		res = SetStringResponse()
		if string_valid:
			res.success = True
		else:
			res.success = False
		return res

	def cmd_constarin(self, input):
		if input > self.cmd_ctrl_max:
			return self.cmd_ctrl_max
		if input < self.cmd_ctrl_min:
			return self.cmd_ctrl_min
		return input

	def pos_constrain(self, input):
		if input > self.pos_ctrl_max:
			return self.pos_ctrl_max
		if input < self.pos_ctrl_min:
			return self.pos_ctrl_min
		return input

	def pos_station_constrain(self, input):
		if input > self.pos_station_max:
			return self.pos_station_max
		if input < self.pos_station_min:
			return self.pos_station_min
		return input

	def initialize_PID(self):
		self.pos_control.setSampleTime(1)
		self.ang_control.setSampleTime(1)
		# self.pos_station_control.setSampleTime(1)
		# self.ang_station_control.setSampleTime(1)

		self.pos_control.SetPoint = 0.0
		self.ang_control.SetPoint = 0.0
		# self.pos_station_control.SetPoint = 0.0
		# self.ang_station_control.SetPoint = 0.0

		self.pos_bridge_control.setSampleTime(1)
		self.ang_bridge_control.setSampleTime(1)
		# self.pos_station_control.setSampleTime(1)
		# self.ang_station_control.setSampleTime(1)

		self.pos_bridge_control.SetPoint = 0.0
		self.ang_bridge_control.SetPoint = 0.0

	def get_goal_angle(self, robot_yaw, robot, goal):
		robot_angle = np.degrees(robot_yaw)
		p1 = [robot[0], robot[1]]
		p2 = [robot[0], robot[1]+1.]
		p3 = goal
		angle = self.get_angle(p1, p2, p3)
		result = angle - robot_angle
		result = self.angle_range(-(result + 90.))
		return result

	def get_angle(self, p1, p2, p3):
		v0 = np.array(p2) - np.array(p1)
		v1 = np.array(p3) - np.array(p1)
		angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
		return np.degrees(angle)

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

	def publish_goal(self, goal):
		marker = Marker()
		marker.header.frame_id = self.frame_id
		marker.header.stamp = rospy.Time.now()
		marker.ns = "pure_pursuit"
		marker.type = marker.SPHERE
		marker.action = marker.ADD
		marker.pose.orientation.w = 1
		marker.pose.position.x = goal[0]
		marker.pose.position.y = goal[1]
		marker.id = 0
		marker.scale.x = 1.5
		marker.scale.y = 1.5
		marker.scale.z = 1.5
		marker.color.a = 1.0
		marker.color.g = 1.0
		marker.color.r = 1.0
		self.pub_goal.publish(marker)

	def set_pid_param(self):
		self.pos_control.setKp(self.pid_param['pos']['kp'])
		self.pos_control.setKi(self.pid_param['pos']['ki'])
		self.pos_control.setKd(self.pid_param['pos']['kd'])
		self.ang_control.setKp(self.pid_param['ang']['kp'])
		self.ang_control.setKi(self.pid_param['ang']['ki'])
		self.ang_control.setKd(self.pid_param['ang']['kd'])

		self.pos_bridge_control.setKp(self.pid_param['pos_bridge']['kp'])
		self.pos_bridge_control.setKi(self.pid_param['pos_bridge']['ki'])
		self.pos_bridge_control.setKd(self.pid_param['pos_bridge']['kd'])
		self.ang_bridge_control.setKp(self.pid_param['ang_bridge']['kp'])
		self.ang_bridge_control.setKi(self.pid_param['ang_bridge']['ki'])
		self.ang_bridge_control.setKd(self.pid_param['ang_bridge']['kd'])
		rospy.loginfo("PID parameters:")
		print("pos: ", self.pid_param['pos'])
		print("ang: ", self.pid_param['ang'])
		print("pos_bridge: ", self.pid_param['pos_bridge'])
		print("ang_bridge: ", self.pid_param['ang_bridge'])

	def pos_pid_cb(self, config, level):
		print("Position: [Kp]: {Kp}   [Ki]: {Ki}   [Kd]: {Kd}\n".format(**config))
		Kp = float("{Kp}".format(**config))
		Ki = float("{Ki}".format(**config))
		Kd = float("{Kd}".format(**config))
		self.pos_control.setKp(Kp)
		self.pos_control.setKi(Ki)
		self.pos_control.setKd(Kd)
		return config

	def ang_pid_cb(self, config, level):
		print("Angular: [Kp]: {Kp}   [Ki]: {Ki}   [Kd]: {Kd}\n".format(**config))
		Kp = float("{Kp}".format(**config))
		Ki = float("{Ki}".format(**config))
		Kd = float("{Kd}".format(**config))
		self.ang_control.setKp(Kp)
		self.ang_control.setKi(Ki)
		self.ang_control.setKd(Kd)
		return config

	def pos_station_pid_cb(self, config, level):
		print("Position: [Kp]: {Kp}   [Ki]: {Ki}   [Kd]: {Kd}\n".format(**config))
		Kp = float("{Kp}".format(**config))
		Ki = float("{Ki}".format(**config))
		Kd = float("{Kd}".format(**config))
		self.pos_station_control.setKp(Kp)
		self.pos_station_control.setKi(Ki)
		self.pos_station_control.setKd(Kd)
		return config

	def ang_station_pid_cb(self, config, level):
		print("Angular: [Kp]: {Kp}   [Ki]: {Ki}   [Kd]: {Kd}\n".format(**config))
		Kp = float("{Kp}".format(**config))
		Ki = float("{Ki}".format(**config))
		Kd = float("{Kd}".format(**config))
		self.ang_station_control.setKp(Kp)
		self.ang_station_control.setKi(Ki)
		self.ang_station_control.setKd(Kd)
		return config

if __name__ == '__main__':
	rospy.init_node('PID_control')
	foo = Robot_PID()
	rospy.spin()
