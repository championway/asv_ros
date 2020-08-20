#!/usr/bin/env python
import numpy as np
import roslib
import rospy
import math
import tf
import time
from nav_msgs.msg import Odometry
from asv_msgs.msg import RobotGoal
from asv_msgs.srv import SetRobotPath, SetRobotPathResponse, SonarData, SonarDataList
from std_srvs.srv import SetBool, SetBoolResponse
from geometry_msgs.msg import Pose

class OBS_AVOIDANCE():
	def __init__(self):
		self.node_name = rospy.get_name()
		self.dis_threshold = 2.0
		self.goal = None
		self.robot_position = None
		self.robot_pose = Pose()
		self.r_goal = None # relative goal position
		rospy.loginfo("[%s] Initializing " %(self.node_name))
		self.pub_robot_goal = rospy.Publisher("robot_goal/obs", RobotGoal, queue_size = 1)
		rospy.Subscriber("robot_goal", RobotGoal, self.goal_cb, queue_size = 1, buff_size = 2**24)
		rospy.Subscriber("sonar", SonarDataList, self.sonar_cb, queue_size = 1, buff_size = 2**24)

	def sonar_cb(self, msg):
		# 0 : down
		# 1 : left
		# 2 : front
		# 3 : right

		if len(msg.list) != 4:
			return

		new_goal = []
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
		self.pub_robot_goal.publish(rg)

	def goal_cb(self, msg):
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