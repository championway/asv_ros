#!/usr/bin/env python

import numpy as np
import roslib
import rospy
import math
import tf
import time
from nav_msgs.msg import Odometry
from asv_msgs.msg import RobotGoal, SonarData, SonarDataList
from asv_msgs.srv import SetRobotPath, SetRobotPathResponse
from std_srvs.srv import SetBool, SetBoolResponse
from geometry_msgs.msg import Pose
from visualization_msgs.msg import Marker, MarkerArray

class OBS_AVOIDANCE():
	def __init__(self):
		self.node_name = rospy.get_name()
		self.dis_threshold = 2.0
		self.goal = None
		self.robot_pose = Pose()
		self.robot_orig = []
		self.r_goal = None # relative goal position
		self.get_goal = False
		self.get_odom = False
		rospy.loginfo("[%s] Initializing " %(self.node_name))

		self.pub_sonar_marker = rospy.Publisher('sonar_marker', MarkerArray, queue_size=1)
		self.pub_new_goal_marker = rospy.Publisher("new_goal_marker",Marker, queue_size=1)

		self.pub_robot_goal = rospy.Publisher("robot_goal/obs", RobotGoal, queue_size = 1)
		rospy.Subscriber("robot_goal", RobotGoal, self.goal_cb, queue_size = 1, buff_size = 2**24)
		rospy.Subscriber("sonar", SonarDataList, self.sonar_cb, queue_size = 1, buff_size = 2**24)
		rospy.Subscriber('odometry', Odometry, self.odom_cb, queue_size = 1, buff_size = 2**24)
	
	def odom_cb(self, msg):
		self.get_odom = True
		robot_pose = Pose()
		robot_pose.position.x = msg.pose.pose.position.x
		robot_pose.position.y = msg.pose.pose.position.y
		quat = (msg.pose.pose.orientation.x,\
				msg.pose.pose.orientation.y,\
				msg.pose.pose.orientation.z,\
				msg.pose.pose.orientation.w)

		self.robot_pose = robot_pose

	def sonar_cb(self, msg):
		# 0 : down
		# 1 : left
		# 2 : front
		# 3 : right

		if len(msg.list) != 4 or self.get_odom == False:
			return

		marker_array = MarkerArray()
		for i in range(1, 4):
			marker = Marker()
			marker.header.frame_id = "map"
			marker.id = i
			marker.header.stamp = rospy.Time.now()
			marker.type = Marker.CUBE
			marker.action = Marker.ADD
			marker.lifetime = rospy.Duration(0.5)
			marker.pose.position.x = self.robot_pose.position.x
			marker.pose.position.y = self.robot_pose.position.y
			marker.pose.position.z = self.robot_pose.position.z
			if i == 1:
				marker.pose.position.y = self.robot_pose.position.y + msg.list[i].distance/1000.
				marker.color.r = 1
				marker.color.g = 0
				marker.color.b = 0
			elif i == 2:
				marker.pose.position.x = self.robot_pose.position.x + msg.list[i].distance/1000.
				marker.color.r = 0
				marker.color.g = 1
				marker.color.b = 0
			elif i == 3:
				marker.pose.position.y = self.robot_pose.position.y - msg.list[i].distance/1000.
				marker.color.r = 0
				marker.color.g = 0
				marker.color.b = 1
			marker.pose.orientation.x = 0.0
			marker.pose.orientation.y = 0.0
			marker.pose.orientation.z = 0.0
			marker.pose.orientation.w = 1.0
			marker.scale.x = 0.3
			marker.scale.y = 0.3
			marker.scale.z = 0.3
			marker.color.a = 1
			marker_array.markers.append(marker)
		self.pub_sonar_marker.publish(marker_array)

		'''new_goal = []
		new_goal = self.r_goal[:]

		left_safe_dis = msg.list[1].distance - self.dis_threshold
		front_safe_dis = msg.list[2].distance - self.dis_threshold
		right_safe_dis = msg.list[3].distance - self.dis_threshold

		if front_safe_dis < new_goal[0]:
			new_goal[0] = front_safe_dis

		if right_safe_dis < new_goal[1]:
			if left_safe_dis < - new_goal[1]:
				new_goal[1] = (right_safe_dis - left_safe_dis)/2.
			else:
				new_goal[1] = right_safe_dis
		elif left_safe_dis < - new_goal[1]:
			new_goal[1] = left_safe_dis

		rg = RobotGoal()
		rg.goal.position.x = new_goal[0] + self.robot_pose.position.x
		rg.goal.position.y = new_goal[1] + self.robot_pose.position.y
		rg.robot = self.robot_pose
		self.pub_robot_goal.publish(rg)'''

	def goal_cb(self, msg):
		self.get_goal = True
		self.goal = [msg.goal.position.x, msg.goal.position.y]
		self.robot_position = [msg.robot.position.x, msg.robot.position.y]
		self.robot_pose = msg.robot
		quat = (msg.robot.orientation.x,\
				msg.robot.orientation.y,\
				msg.robot.orientation.z,\
				msg.robot.orientation.w)
		_, _, yaw = tf.transformations.euler_from_quaternion(quat)

		if len(self.goal) == 0 or len(self.robot_position) == 0: # if the robot hasn't recieve any goal
			return

		self.r_goal = [self.goal[0] - self.robot_position[0], self.goal[1] - self.robot_position[1]]

	def get_distance(self, p1, p2):
		return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

if __name__ == '__main__':
	rospy.init_node('OBS_AVOIDANCE')
	foo = OBS_AVOIDANCE()
	rospy.spin()