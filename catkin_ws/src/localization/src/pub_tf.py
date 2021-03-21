#!/usr/bin/env python
import rospy
import roslib
import tf
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
import numpy as np

class PUB_TF():
	def __init__(self):
		self.node_name = rospy.get_name()
		rospy.loginfo("[%s] Initializing " %(self.node_name))

		self.br = tf.TransformBroadcaster()

		self.laser_frame = "/laser"
		self.robot_frame = "/robot_base"
		self.map_frame = "/map"

		self.get_odom = False

		self.odom_trans = None
		self.odom_rot = None

		rospy.Subscriber("/ASV/odometry", Odometry, self.cbOdom, queue_size=1)
		rospy.Timer(rospy.Duration(0.1), self.cbTimer)


	def cbTimer(self, event):
		if self.get_odom:
			t = rospy.Time.now()
			self.br.sendTransform(self.odom_trans, self.odom_rot, t, self.robot_frame, self.map_frame)

		#quat = tf.transformations.quaternion_from_euler (-r, -p, -y)
		self.br.sendTransform((0, 0, 0), \
						 (0, 0, 0, 1), rospy.Time.now(), self.laser_frame, self.robot_frame)

	def cbOdom(self, msg):
		# Global Frame: "/map"
		# map_id = msg.header.frame_id
		# br = tf.TransformBroadcaster()
		position = [msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z]
		quat = [msg.pose.pose.orientation.x,\
				msg.pose.pose.orientation.y,\
				msg.pose.pose.orientation.z,\
				msg.pose.pose.orientation.w]
		r, p, y = tf.transformations.euler_from_quaternion(quat)
		tfros = tf.TransformerROS()
		M = tfros.fromTranslationRotation(position, quat)
		# M_inv =  np.linalg.inv(M)
		self.odom_trans = tf.transformations.translation_from_matrix(M)
		self.odom_rot = tf.transformations.quaternion_from_matrix(M)
		# t = rospy.Time.from_sec(0)
		# t = rospy.Time.now()
		# br.sendTransform(trans, rot, t, "/robot_base", map_id)

		#quat = tf.transformations.quaternion_from_euler (-r, -p, -y)
		# br.sendTransform((0, 0, 0), \
		# 				 (0, 0, 0, 1), rospy.Time.now(), "/laser", "/robot_base")
		self.get_odom = True

if __name__=="__main__":
	# Tell ROS that we're making a new node.
	rospy.init_node("pub_tf",anonymous=False)
	foo = PUB_TF()
	rospy.spin()