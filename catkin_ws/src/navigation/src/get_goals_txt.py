#!/usr/bin/env python
import numpy as np
import roslib
import rospy
import tf
import struct
import math
import time
from geometry_msgs.msg import PoseArray, Pose, PoseStamped, Point
from asv_msgs.msg import RobotPath, WayPoint
from asv_msgs.srv import SetRobotPath, SetRobotPathResponse, SetString, SetStringResponse
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from visualization_msgs.msg import Marker, MarkerArray
from nav_msgs.msg import Odometry
from geodesy.utm import UTMPoint, fromLatLong
import rospkg
import os

class ROBOT_GOAL():
	def __init__(self):
		self.node_name = rospy.get_name()
		self.frame_id = "map"
		self.path_list = []
		self.waypoint_list = []
		self.robot_orig = []
		self.get_orig = False
		self.rcv_goals = []
		self.goals = []
		self.clear = False
		self.get_path = False
		self.start_navigation = False
		self.set_path_succ = False	# If set path got wrong, we need to resend again
		self.path_srv = rospy.Service("path_txt", SetString, self.path_cb)
		self.cycle = rospy.get_param("~cycle", True)
		self.gui = rospy.get_param("~gui", True)
		
		if not self.gui:
			rospack = rospkg.RosPack()
			txt_name = rospy.get_param("~txt_name", "test1.txt")
			self.txt_path = os.path.join(rospack.get_path('asv_config'), "path", txt_name)
			if not os.path.isfile(self.txt_path):
				rospy.signal_shutdown("Quit")
				print("[%s] ERROR!!! No path txt file detected" %self.node_name)
				return
			read_succ = self.read_txt(self.txt_path)
			if not read_succ:
				rospy.signal_shutdown("Quit")
				print("[%s] ERROR!!! Path txt reading error" %self.node_name)
				return
			self.get_path = True


		rospy.loginfo("[%s] Initializing " %(self.node_name))
		
		self.navigation_srv = rospy.Service("start_navigation", SetBool, self.navigation_cb)
		self.clear_srv = rospy.Service("clear_goals", SetBool, self.clear_cb)
		self.pub_marker = rospy.Publisher('goals_marker', MarkerArray, queue_size=1)
		self.pub_waypoint = rospy.Publisher("path_marker",Marker, queue_size=1)
		self.sub_orig = rospy.Subscriber("robot_origin", Point, self.orig_cb, queue_size=1)
		rospy.Subscriber('odometry', Odometry, self.odom_cb, queue_size = 1, buff_size = 2**24)
		
	def odom_cb(self, msg):
		if self.clear:
			self.reset()
		if not self.get_orig:
			rospy.loginfo("Haven't recieve robot origin position")
			return
		robot_position = [msg.pose.pose.position.x, msg.pose.pose.position.y]
		quat = (msg.pose.pose.orientation.x,\
				msg.pose.pose.orientation.y,\
				msg.pose.pose.orientation.z,\
				msg.pose.pose.orientation.w)
		_, _, yaw = tf.transformations.euler_from_quaternion(quat)

		self.robot_position = robot_position
		if self.get_path:
			self.goals = self.rcv_goals[:]
			self.drawPoints()
			self.drawWaypoint()
			if self.start_navigation and not self.set_path_succ:
				self.set_path()

	def read_txt(self, txt_path):
		print("Read file: %s" %txt_path)
		file = open(txt_path, "r")
		self.path_list = []
		for f in file:
			try:
				#line = f.split('\n')
				line = f.strip()
				if line[0] == '#':
					continue
				data = line.split(',')
				self.path_list.append([float(data[0]), float(data[1])])
			except:
				return False
		file.close()
		self.utm_transform()
		return True

	def read_str(self, s):
		self.path_list = []
		self.waypoint_list = []
		if len(s) == 0:
			return False
		bridge_has_start = False
		for f in s.splitlines():
			try:
				wp = WayPoint()
				wp.bridge_start.data = False
				wp.bridge_end.data = False

				line = f.strip()
				if line[0] == '#':
					continue
				data = line.split(',')
				bridge_start = False
				bridge_end = False
				for i in range(2, len(data)):
					try:
						key, value = data[i].strip().split(':')
						if key == "bridge":
							if value == "start":
								bridge_start = True
								wp.bridge_start.data = True
							elif value == "end":
								bridge_end = True
								wp.bridge_end.data = True
						elif key == "stop":
							wp.stop_time.data = float(value)
					except:
						return False
					# value = data[i].strip()
					# if (value == "bridge_start"):
					# 	bridge_start = True
					# 	wp.bridge_start.data = True
					# elif (value == "bridge_end"):
					# 	bridge_end = True
					# 	wp.bridge_end.data = True
				if bridge_has_start:
					if bridge_end:
						bridge_has_start = False
					else:
						rospy.loginfo("Wrong Bridge Info")
						return False
				if bridge_start:
					bridge_has_start = True
				self.waypoint_list.append(wp)
				self.path_list.append([float(data[0]), float(data[1])])
			except:
				return False
		self.utm_transform()
		return True


	def path_cb(self, req):
		res = SetStringResponse()
		if self.read_str(req.str):
			rospy.loginfo("Get Path")
			self.get_path = True
			res.success = True
		else:
			rospy.loginfo("Wrong Path Data")
			res.success = False
		return res

	def orig_cb(self, msg):
		rospy.loginfo("get orig")
		self.robot_orig = [msg.x, msg.y]
		self.get_orig = True
		self.sub_orig.unregister()

	def utm_transform(self):
		self.rcv_goals = []
		for data in self.path_list:
			p = Pose()
			utm_data = fromLatLong(data[0], data[1])
			x = utm_data.easting - self.robot_orig[0]
			y = utm_data.northing - self.robot_orig[1]
			p.position.x, p.position.y = x, y
			self.rcv_goals.append(p)

	def reset(self):
		self.set_path_succ = False
		del self.rcv_goals[:]
		del self.waypoint_list[:]
		del self.goals[:]
		self.clear = False

	def resetNavigation(self):
		self.start_navigation = False
		self.set_path_succ = False
		set_bool = SetBoolRequest()
		set_bool.data = True
		try:
			srv = rospy.ServiceProxy('reset_goals', SetBool)
			resp = srv(set_bool)
			return resp
		except rospy.ServiceException, e:
			print "Service call failed: %s"%e

	def navigation_cb(self, req):
		if req.data == True:
			rospy.loginfo("Start Navigation")
			if not self.start_navigation:
				self.start_navigation = True
				self.set_path_succ = False
		else:
			rospy.loginfo("Reset Navigation")
			self.resetNavigation()
		res = SetBoolResponse()
		res.success = True
		res.message = "recieved"
		return res

	def clear_cb(self, req):
		if req.data == True:
			self.clear = True
		else:			
			self.clear = False
		res = SetBoolResponse()
		res.success = True
		res.message = "recieved"
		return res

	def set_path(self):
		#rospy.wait_for_service('/set_path')
		rospy.loginfo("Set path to robot")
		robot_path = RobotPath()
		for i in range(len(self.goals)):
			wp = WayPoint()
			wp = self.waypoint_list[i]
			wp.waypoint = self.goals[i]
			robot_path.list.append(wp)
		try:
			srv = rospy.ServiceProxy('set_path', SetRobotPath)
			resp = srv(robot_path)
			self.set_path_succ = True
			return resp
		except rospy.ServiceException, e:
			self.set_path_succ = False
			print "Service call failed: %s"%e

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

	def drawPoints(self):
		marker_array = MarkerArray()
		for i in range(len(self.goals)):
			#print obj_list.list[i].varianceX, obj_list.list[i].varianceY
			marker = Marker()
			marker.header.frame_id = self.frame_id
			marker.id = i
			marker.header.stamp = rospy.Time.now()
			marker.type = Marker.CUBE
			marker.action = Marker.ADD
			marker.lifetime = rospy.Duration(0.5)
			marker.pose.position = self.goals[i].position
			marker.pose.orientation.x = 0.0
			marker.pose.orientation.y = 0.0
			marker.pose.orientation.z = 0.0
			marker.pose.orientation.w = 1.0
			marker.scale.x = 1.5
			marker.scale.y = 1.5
			marker.scale.z = 1.5
			marker.color.r = 0
			marker.color.g = 1
			marker.color.b = 0
			marker.color.a = 1
			if self.waypoint_list[i].bridge_start.data == True or self.waypoint_list[i].bridge_end.data == True:
				marker.color.r = 1
				marker.color.g = 0
				marker.color.b = 0

			marker_array.markers.append(marker)
		self.pub_marker.publish(marker_array)

	def drawWaypoint(self):
		marker = Marker()
		marker.header.frame_id = self.frame_id
		marker.header.stamp = rospy.Time.now()
		marker.ns = "points_for_waypoint"
		marker.action = Marker.ADD
		marker.pose.orientation.w = 1.0
		marker.id = 0
		marker.type = Marker.LINE_STRIP
		marker.scale.x = 0.7
		marker.scale.y = 0.7
		marker.scale.z = 0.7
		marker.color.g = 1.0
		marker.color.b = 1.0
		marker.color.a = 0.75
		for i in range(len(self.goals)):
			wp = Point()
			wp.x, wp.y = self.goals[i].position.x, self.goals[i].position.y
			wp.z = 0
			marker.points.append(wp)
		if self.cycle:
			wp = Point()
			wp.x, wp.y = self.goals[0].position.x, self.goals[0].position.y
			wp.z = 0
			marker.points.append(wp)
		self.pub_waypoint.publish(marker)

	'''def drawPath(self):
		marker = Marker()
		marker.header.frame_id = self.frame_id
		marker.header.stamp = rospy.Time.now()
		marker.ns = "points_for_waypoint"
		marker.action = Marker.ADD
		marker.pose.orientation.w = 1.0
		marker.id = 0
		marker.type = Marker.LINE_STRIP
		marker.scale.x = 0.5
		marker.scale.y = 0.5
		marker.scale.z = 0.5
		marker.color.g = 1.0
		marker.color.a = 1.0
		for goal in self.goals:
			wp = Point()
			wp.x, wp.y = goal.position.x, goal.position.y
			wp.z = 0
			marker.points.append(wp)
		wp = Point()
		wp.x, wp.y = self.goals[0].position.x, self.goals[0].position.y
		wp.z = 0
		marker.points.append(wp)
		self.pub_waypoint.publish(marker)'''

if __name__ == '__main__':
	rospy.init_node('ROBOT_GOAL_TXT')
	foo = ROBOT_GOAL()
	rospy.spin()