#!/usr/bin/env python
import numpy as np
import roslib
import rospy
import tf
import struct
import math
import time
from geometry_msgs.msg import PoseArray, Pose, PoseStamped, Point
from asv_msgs.msg import RobotPath
from asv_msgs.srv import SetRobotPath, SetRobotPathResponse
from std_srvs.srv import SetBool, SetBoolResponse
from visualization_msgs.msg import Marker, MarkerArray
from nav_msgs.msg import Odometry
import rospkg

class ROBOT_GOAL():
	def __init__(self):
		self.node_name = rospy.get_name()
		self.frame_id = "map"
		self.rcv_goals = []
		self.goals = []
		self.clear = False
		self.start_navigation = False
		self.set_path_succ = False	# If set path got wrong, we need to resend again

		rospy.loginfo("[%s] Initializing " %(self.node_name))
		
		self.navigation_srv = rospy.Service("/start_navigation", SetBool, self.navigation_cb)
		self.clear_srv = rospy.Service("/clear_goals", SetBool, self.clear_cb)
		self.pub_marker = rospy.Publisher('~goals_marker', MarkerArray, queue_size=1)
		rospy.Subscriber("/move_base_simple/goal", PoseStamped, self.goal_cb, queue_size=1)
		rospy.Subscriber('~odometry', Odometry, self.odom_cb, queue_size = 1, buff_size = 2**24)


	def odom_cb(self, msg):
		if self.clear:
			self.reset()
		robot_position = [msg.pose.pose.position.x, msg.pose.pose.position.y]
		quat = (msg.pose.pose.orientation.x,\
				msg.pose.pose.orientation.y,\
				msg.pose.pose.orientation.z,\
				msg.pose.pose.orientation.w)
		_, _, yaw = tf.transformations.euler_from_quaternion(quat)

		self.robot_position = robot_position
		self.goals = self.rcv_goals[:]
		self.drawPoints()
		if self.start_navigation and not self.set_path_succ:
			self.set_path()

	def reset(self):
		self.set_path_succ = False
		del self.rcv_goals[:]
		del self.goals[:]
		self.clear = False

	def goal_cb(self, p):
		self.rcv_goals.append(p.pose)

	def navigation_cb(self, req):
		if req.data == True:
			rospy.loginfo("Start Navigation")
			self.start_navigation = True
			self.set_path_succ = False
		else:
			rospy.loginfo("Stop Navigation")
			self.start_navigation = False
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
		for goal in self.goals:
			robot_path.list.append(goal)
		try:
			srv = rospy.ServiceProxy('/set_path', SetRobotPath)
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
			marker.scale.x = 0.7
			marker.scale.y = 0.7
			marker.scale.z = 0.7
			marker.color.r = 1
			marker.color.g = 0
			marker.color.b = 0
			marker.color.a = 1
			marker_array.markers.append(marker)
		self.pub_marker.publish(marker_array)

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
	rospy.init_node('ROBOT_GOAL')
	foo = ROBOT_GOAL()
	rospy.spin()