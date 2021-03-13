#!/usr/bin/env python
import rospy
import roslib
import tf
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
import numpy as np
def call_back(msg):
	# Global Frame: "/map"
	map_id = msg.header.frame_id
	br = tf.TransformBroadcaster()
	position = [msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.position.z]
	quat = [msg.pose.pose.orientation.x,\
			msg.pose.pose.orientation.y,\
			msg.pose.pose.orientation.z,\
			msg.pose.pose.orientation.w]
	r, p, y = tf.transformations.euler_from_quaternion(quat)
	tfros = tf.TransformerROS()
	M = tfros.fromTranslationRotation(position, quat)
	# M_inv =  np.linalg.inv(M)
	trans = tf.transformations.translation_from_matrix(M)
	rot = tf.transformations.quaternion_from_matrix(M)
	t = rospy.Time.from_sec(0)
	#t = rospy.Time.now()
	br.sendTransform(trans, rot, t, "/robot_base", map_id)

	#quat = tf.transformations.quaternion_from_euler (-r, -p, -y)
	br.sendTransform((0, 0, 0), \
					 (0, 0, 0, 1), rospy.Time.now(), "/laser", "/robot_base")

if __name__=="__main__":
	# Tell ROS that we're making a new node.
	rospy.init_node("pub_tf",anonymous=False)
	rospy.Subscriber("/ASV/odometry", Odometry, call_back, queue_size=1)
	rospy.spin()