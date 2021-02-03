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
from std_msgs.msg import UInt32, String
from dynamic_reconfigure.server import Server
from control.cfg import lookaheadConfig
from asv_msgs.msg import WayPoint, RobotGoal
from asv_msgs.srv import SetRobotPath, SetRobotPathResponse
from std_srvs.srv import SetBool, SetBoolResponse
import rospkg
from cv_bridge import CvBridge, CvBridgeError
from pure_pursuit import PurePursuit

class NAVIGATION():
	def __init__(self):
		self.node_name = rospy.get_name()

		self.state = "normal"

		self.station_keeping_dis = 1
		self.is_station_keeping = False
		self.start_navigation = False
		self.over_bridge_count = 4
		self.stop_pos = []
		self.goals = []
		self.full_goals = []
		self.get_path = False
		self.final_goal = None # The final goal that you want to arrive
		self.goal = self.final_goal
		self.robot_position = None
		self.cycle = rospy.get_param("~cycle", True)
		self.gazebo = rospy.get_param("~gazebo", False)

		self.over_bridge_counter = 0
		self.satellite_list = []
		self.satellite_thres = 15
		self.imu_angle = 0
		self.angle_thres = 0.85
		self.pre_pose = []
		self.bridge_mode = False

		self.stop_list = []
		self.stop_start_timer = rospy.get_time()
		self.stop_end_timer = rospy.get_time()

		self.satellite_avg = 0
		self.satellite_curr = 0

		self.log_string = ""

		rospy.loginfo("[%s] Initializing " %(self.node_name))
		
		# self.pub_lookahead = rospy.Publisher("lookahead_point", Marker, queue_size = 1)
		self.pub_robot_goal = rospy.Publisher("robot_goal", RobotGoal, queue_size = 1)
		self.pub_fake_goal = rospy.Publisher("fake_goal",Marker, queue_size=1)
		self.pub_log_str = rospy.Publisher("log_str",String, queue_size=1)
		self.path_srv = rospy.Service("set_path", SetRobotPath, self.path_cb)
		self.reset_srv = rospy.Service("reset_goals", SetBool, self.reset_cb)
		# self.lookahead_srv = Server(lookaheadConfig, self.lookahead_cb, "LookAhead")

		self.purepursuit = PurePursuit()
		self.purepursuit.set_lookahead(2.2)

		rospy.Subscriber("odometry", Odometry, self.odom_cb, queue_size = 1, buff_size = 2**24)
		rospy.Subscriber("/mavros/global_position/raw/satellites", UInt32, self.satellite_cb, queue_size = 1, buff_size = 2**24)
		# rospy.Subscriber("imu/data", Imu, self.imu_cb, queue_size = 1, buff_size = 2**24)
		
	def stop_state(self, time_threshold):
		if (rospy.get_time() - self.stop_start_timer) > time_threshold:
			self.state = "normal"
			return
		rg = RobotGoal()
		rg.goal.position.x, rg.goal.position.y = pursuit_point[0], pursuit_point[1]
		rg.robot = msg.pose.pose

	def imu_cb(self, msg):
		quat = (msg.orientation.x,\
				msg.orientation.y,\
				msg.orientation.z,\
				msg.orientation.w)
		_, _, angle = tf.transformations.euler_from_quaternion(quat)
		while angle >= np.pi:
			angle = angle - 2*np.pi
		while angle < -np.pi:
			angle = angle + 2*np.pi
		self.imu_angle = angle

	def satellite_cb(self, msg):
		self.satellite_curr = msg.data
		

	def publish_fake_goal(self, x, y):
		marker = Marker()
		marker.header.frame_id = "map"
		marker.header.stamp = rospy.Time.now()
		marker.ns = "fake_goal"
		marker.type = marker.CUBE
		marker.action = marker.ADD
		marker.pose.position.x = x
		marker.pose.position.y = y
		marker.pose.orientation.x = 0
		marker.pose.orientation.y = 0
		marker.pose.orientation.z = 0
		marker.pose.orientation.w = 1
		marker.scale.x = 0.7
		marker.scale.y = 0.7
		marker.scale.z = 0.7
		marker.color.a = 1.0
		marker.color.b = 1.0
		marker.color.g = 1.0
		marker.color.r = 1.0
		self.pub_fake_goal.publish(marker)

	def odom_cb(self, msg):
		self.robot_position = [msg.pose.pose.position.x, msg.pose.pose.position.y]

		if not self.is_station_keeping:
			self.stop_pos = [[msg.pose.pose.position.x, msg.pose.pose.position.y]]
		quat = (msg.pose.pose.orientation.x,\
				msg.pose.pose.orientation.y,\
				msg.pose.pose.orientation.z,\
				msg.pose.pose.orientation.w)
		_, _, yaw = tf.transformations.euler_from_quaternion(quat)

		while yaw >= np.pi:
			yaw = yaw - 2*np.pi
		while yaw < -np.pi:
			yaw = yaw + 2*np.pi
		self.imu_angle = yaw

		if len(self.goals) == 0 or not self.get_path: # if the robot haven't recieve any goal
			return

		reach_goal = self.purepursuit.set_robot_pose(self.robot_position, yaw)
		pursuit_point = self.purepursuit.get_pursuit_point()
		is_last_idx = self.purepursuit.is_last_idx()
		
		if reach_goal or pursuit_point is None or is_last_idx:
			if self.cycle:
				# The start point is the last point of the list
				self.stop_list = []
				start_point = [self.goals[-1].waypoint.position.x, self.goals[-1].waypoint.position.y]
				self.full_goals[0] = self.full_goals[-1]
				self.purepursuit.set_goal(start_point, self.goals)
			else:
				rg = RobotGoal()
				rg.goal.position.x, rg.goal.position.y = self.goals[-1].waypoint.position.x, self.goals[-1].waypoint.position.y
				rg.robot = msg.pose.pose
				rg.only_angle.data = False
				rg.mode.data = "normal"
				self.pub_robot_goal.publish(rg)
			return

		rg = RobotGoal()

		# if AUV is under the bridge
		if self.full_goals[self.purepursuit.current_waypoint_index - 1].bridge_start.data:
			self.bridge_mode = True
			rg.mode.data = "bridge"
			fake_goal, is_robot_over_goal = self.purepursuit.get_parallel_fake_goal()
			if fake_goal is None:
				return
			self.publish_fake_goal(fake_goal[0], fake_goal[1])
			rg.goal.position.x, rg.goal.position.y = fake_goal[0], fake_goal[1]
			

			if is_robot_over_goal:
				if self.legal_angle():
					if self.satellite_curr >= int(self.satellite_avg) or self.gazebo:
						self.over_bridge_counter = self.over_bridge_counter + 1
						self.log_string = "over bridge, leagal angle, satellite"
					else:
						self.over_bridge_counter = 0
						self.log_string = "over bridge, leagal angle, " + str(self.satellite_curr) + "," + str(self.satellite_avg)
				else:
					self.over_bridge_counter = 0
					self.log_string = "over bridge, illeagal angle"
			else:
				self.over_bridge_counter = 0
				self.log_string = "not over the bridge"

			if self.over_bridge_counter > self.over_bridge_count:
				if not (not self.cycle and self.purepursuit.current_waypoint_index == len(self.purepursuit.waypoints) - 1):
					rospy.loginfo("[%s]Arrived waypoint: %d"%("Over Bridge", self.purepursuit.current_waypoint_index))
					if self.purepursuit.status != -1:
						self.purepursuit.status = self.purepursuit.status + 1
				self.purepursuit.current_waypoint_index = self.purepursuit.current_waypoint_index + 1

		else:
			rg.mode.data = "normal"
			self.log_string = "not under bridge"
			self.bridge_mode = False
			rg.goal.position.x, rg.goal.position.y = pursuit_point[0], pursuit_point[1]
			
			if self.satellite_avg == 0:
				self.satellite_avg = self.satellite_curr
			else:
				self.satellite_avg = (self.satellite_avg*3. + self.satellite_curr)/4.

		if self.full_goals[self.purepursuit.current_waypoint_index - 1].stop_time.data != 0:
			if self.purepursuit.current_waypoint_index not in self.stop_list: 
				self.stop_list.append(self.purepursuit.current_waypoint_index)
				self.state = "stop"
				self.stop_start_timer = rospy.get_time()

			if self.state == "stop":
				time_threshold = self.full_goals[self.purepursuit.current_waypoint_index - 1].stop_time.data
				if (rospy.get_time() - self.stop_start_timer) > time_threshold:
					self.state = "normal"
				else:
					rg.goal.position.x, rg.goal.position.y = self.robot_position[0], self.robot_position[1]
			
		rg.robot = msg.pose.pose
		self.purepursuit.bridge_mode = self.bridge_mode
		self.pub_robot_goal.publish(rg)

		self.pre_pose = [msg.pose.pose.position.x, msg.pose.pose.position.y]

		#yaw = yaw + np.pi/2.
		# if reach_goal or reach_goal is None:
		# 	self.publish_lookahead(self.robot_position, self.final_goal[-1])
		# else:
		# 	self.publish_lookahead(self.robot_position, pursuit_point)
		ss = String()
		ss.data = self.log_string
		self.pub_log_str.publish(ss)

	def legal_angle(self):
		if self.pre_pose != []:
			angle = self.getAngle()
			if angle < self.angle_thres:
				return True
		return False

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

	def reset_cb(self, req):
		if req.data == True:
			self.full_goals = []
			self.goals = []
			self.get_path = False
		res = SetBoolResponse()
		res.success = True
		res.message = "recieved"
		return res

	def path_cb(self, req):
		rospy.loginfo("Get Path")
		res = SetRobotPathResponse()
		wp = WayPoint()
		wp.bridge_start.data = False
		wp.bridge_end.data = False
		self.full_goals.append(wp)
		if len(req.data.list) > 0:
			self.goals = req.data.list
			self.full_goals = self.full_goals + req.data.list
			self.get_path = True
			self.purepursuit.set_goal(self.robot_position, self.goals)
		res.success = True
		return res

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

	def publish_lookahead(self, robot, lookahead):
		marker = Marker()
		marker.header.frame_id = "map"
		marker.header.stamp = rospy.Time.now()
		marker.ns = "pure_pursuit"
		marker.type = marker.LINE_STRIP
		marker.action = marker.ADD
		wp = Point()
		wp.x, wp.y = robot[:2]
		wp.z = 0
		marker.points.append(wp)
		wp = Point()
		wp.x, wp.y = lookahead[0], lookahead[1]
		wp.z = 0
		marker.points.append(wp)
		marker.id = 0
		marker.scale.x = 0.5
		marker.scale.y = 0.5
		marker.scale.z = 0.5
		marker.color.a = 1.0
		marker.color.b = 1.0
		marker.color.g = 1.0
		marker.color.r = 0.0
		#self.pub_lookahead.publish(marker)

	def lookahead_cb(self, config, level):
		print("Look Ahead Distance: {Look_Ahead}\n".format(**config))
		lh = float("{Look_Ahead}".format(**config))
		self.purepursuit.set_lookahead(lh)
		return config

if __name__ == '__main__':
	rospy.init_node('NAVIGATION')
	foo = NAVIGATION()
	rospy.spin()
