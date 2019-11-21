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
from dynamic_reconfigure.server import Server
from control.cfg import lookaheadConfig
from asv_msgs.msg import RobotGoal
from asv_msgs.srv import SetRobotPath, SetRobotPathResponse
from std_srvs.srv import SetBool, SetBoolResponse
import rospkg
from cv_bridge import CvBridge, CvBridgeError
from pure_pursuit import PurePursuit

class NAVIGATION():
	def __init__(self):
		self.node_name = rospy.get_name()
		self.station_keeping_dis = 1
		self.is_station_keeping = False
		self.start_navigation = False
		self.stop_pos = []
		self.goals = []
		self.get_path = False
		self.final_goal = None # The final goal that you want to arrive
		self.goal = self.final_goal
		self.robot_position = None
		self.cycle = rospy.get_param("~cycle", True)

		rospy.loginfo("[%s] Initializing " %(self.node_name))
		
		# self.pub_lookahead = rospy.Publisher("lookahead_point", Marker, queue_size = 1)
		self.pub_robot_goal = rospy.Publisher("robot_goal", RobotGoal, queue_size = 1)
		self.path_srv = rospy.Service("set_path", SetRobotPath, self.path_cb)
		# self.lookahead_srv = Server(lookaheadConfig, self.lookahead_cb, "LookAhead")

		self.purepursuit = PurePursuit()
		self.purepursuit.set_lookahead(2.75)

		rospy.Subscriber("odometry", Odometry, self.odom_cb, queue_size = 1, buff_size = 2**24)


	def odom_cb(self, msg):
		self.robot_position = [msg.pose.pose.position.x, msg.pose.pose.position.y]
		if not self.is_station_keeping:
			self.stop_pos = [[msg.pose.pose.position.x, msg.pose.pose.position.y]]
		quat = (msg.pose.pose.orientation.x,\
				msg.pose.pose.orientation.y,\
				msg.pose.pose.orientation.z,\
				msg.pose.pose.orientation.w)
		_, _, yaw = tf.transformations.euler_from_quaternion(quat)

		if len(self.goals) == 0 or not self.get_path: # if the robot haven't recieve any goal
			return

		reach_goal = self.purepursuit.set_robot_pose(self.robot_position, yaw)
		pursuit_point = self.purepursuit.get_pursuit_point()
		is_last_idx = self.purepursuit.is_last_idx()
		
		if reach_goal or pursuit_point is None or is_last_idx:
			if self.cycle:
				# The start point is the last point of the list
				start_point = [self.goals[-1].position.x, self.goals[-1].position.y]
				self.purepursuit.set_goal(start_point, self.goals)
			else:
				rg = RobotGoal()
				rg.goal.position.x, rg.goal.position.y = self.goals[-1].position.x, self.goals[-1].position.y
				rg.robot = msg.pose.pose
				rg.only_angle.data = False
				self.pub_robot_goal.publish(rg)
			return

		rg = RobotGoal()
		rg.goal.position.x, rg.goal.position.y = pursuit_point[0], pursuit_point[1]
		rg.robot = msg.pose.pose
		self.pub_robot_goal.publish(rg)

		#yaw = yaw + np.pi/2.
		# if reach_goal or reach_goal is None:
		# 	self.publish_lookahead(self.robot_position, self.final_goal[-1])
		# else:
		# 	self.publish_lookahead(self.robot_position, pursuit_point)

	def path_cb(self, req):
		rospy.loginfo("Get Path")
		res = SetRobotPathResponse()
		if len(req.data.list) > 0:
			self.goals = req.data.list
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