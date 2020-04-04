#!/usr/bin/env python
import numpy as np
import roslib
import rospy
import math
import time
from nav_msgs.msg import Odometry
from asv_msgs.msg import RobotGoal
from asv_msgs.srv import SetRobotPath, SetRobotPathResponse, SonarData, SonarDataList
from std_srvs.srv import SetBool, SetBoolResponse

class OBS_AVOIDANCE():
	def __init__(self):
		self.node_name = rospy.get_name()
		rospy.loginfo("[%s] Initializing " %(self.node_name))
		self.pub_robot_goal = rospy.Publisher("robot_goal/obs", RobotGoal, queue_size = 1)
		rospy.Subscriber("robot_goal", RobotGoal, self.goal_cb, queue_size = 1, buff_size = 2**24)
		rospy.Subscriber("sonar", RobotGoal, self.goal_cb, queue_size = 1, buff_size = 2**24)

	def sonar_cb(self, msg):
		# 0 : down
		# 1 : left
		# 2 : front
		# 3 : right

		if len(msg.list) != 4:
			return

		


	def goal_cb(self, msg):
		

	def get_distance(self, p1, p2):
		return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

if __name__ == '__main__':
	rospy.init_node('OBS_AVOIDANCE')
	foo = OBS_AVOIDANCE()
	rospy.spin()