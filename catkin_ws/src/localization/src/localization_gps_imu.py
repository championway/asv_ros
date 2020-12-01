#!/usr/bin/env python
'''
Author: David Chen
Date:2019/10/15                                                                
Last update: 2020/11/30                                                         
Locailization by gps and imu
'''
import rospy
from sensor_msgs.msg import NavSatFix, Imu
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Point
from std_msgs.msg import Float64
from message_filters import ApproximateTimeSynchronizer, TimeSynchronizer
from std_srvs.srv import EmptyRequest, EmptyResponse, Empty
from asv_msgs.srv import SetValue, SetValueRequest, SetValueResponse
import message_filters

from geodesy.utm import UTMPoint, fromLatLong
import tf
import math
from scipy.stats import norm
import numpy as np

import rospkg
import yaml
import os

class LocailizationGPSImu(object):
    def __init__(self):
        self.node_name = rospy.get_name()
        self.debug = False
        self.pose = Pose()
        self.prior_pose = Pose()
        self.prior_roll = 0
        self.prior_pitch = 0
        self.prior_yaw = 0
        self.flush_count = 0
        self.start = False
        self.robot_origin = Point()
        self.covariance = np.zeros((36,), dtype=float)
        self.odometry = Odometry()
        self.br = tf.TransformBroadcaster()

        self.IMU_MSG = None
        self.GPS_MSG = None
        
        # param
        self.imu_offset = 0
        self.lat_orig = rospy.get_param('~latitude', 0.0)
        self.long_orig = rospy.get_param('~longitude', 0.0)
        self.utm_orig = fromLatLong(self.lat_orig, self.long_orig)
        self.imu_rotate = rospy.get_param('~imu_rotate',np.pi/2)

        rospack = rospkg.RosPack()
        self.imu_param_path = os.path.join(rospack.get_path('asv_config'), "calibration/imu.yaml")
        self.imu_param = None

        with open (self.imu_param_path, 'r') as file:
            self.imu_param = yaml.safe_load(file)

        # Service
        self.srv_imu_offset = rospy.Service('~imu_offset', SetValue, self.cb_srv_imu_offest)

        # Publisher
        self.pub_odm = rospy.Publisher("odometry", Odometry, queue_size=1)
        self.pub_orig = rospy.Publisher("robot_origin", Point, queue_size=1)

        # Subscriber
        sub_imu_only = rospy.Subscriber("imu/data", Imu, self.cb_imu, queue_size = 1)
        sub_gps_only = rospy.Subscriber("fix", NavSatFix, self.cb_gps, queue_size = 1)
        
        # sub_imu = message_filters.Subscriber("imu/data", Imu)
        # sub_gps = message_filters.Subscriber("fix", NavSatFix)
        # ats = ApproximateTimeSynchronizer((sub_imu, sub_gps), queue_size = 1, slop = 0.1)
        # ats.registerCallback(self.cb_gps_imu)

        self.timer = rospy.Timer(rospy.Duration(0.2),self.cb_timer)

    def cb_timer(self, event):
        if self.flush_count < 10 and self.GPS_MSG is not None and self.IMU_MSG is not None:
            # rospy.loginfo("[%s] Flush Data" %self.node_name)
            self.flush_count = self.flush_count + 1
            self.utm_orig = fromLatLong(self.GPS_MSG.latitude, self.GPS_MSG.longitude)
            self.robot_origin.x = self.utm_orig.easting
            self.robot_origin.y = self.utm_orig.northing
            return        
        self.pub_orig.publish(self.robot_origin)
        self.process_gps(self.GPS_MSG)
        self.process_imu(self.IMU_MSG)
        self.kalman_filter()

    def cb_gps(self, msg):
        self.GPS_MSG = msg

    def cb_imu(self, msg):
        self.IMU_MSG = msg

    def process_gps(self, msg_gps):
        if msg_gps is None:
            return
        utm_point = fromLatLong(msg_gps.latitude, msg_gps.longitude)
        self.pose.position.x = utm_point.easting - self.utm_orig.easting
        self.pose.position.y = utm_point.northing - self.utm_orig.northing
        self.pose.position.z = 0


    def process_imu(self, msg_imu):
        self.pose.orientation = msg_imu.orientation

    # def cb_gps_imu(self, msg_imu, msg_gps):
    #     if self.flush_count < 10:
    #         # rospy.loginfo("[%s] Flush Data" %self.node_name)
    #         self.flush_count = self.flush_count + 1
    #         self.utm_orig = fromLatLong(msg_gps.latitude, msg_gps.longitude)
    #         self.robot_origin.x = self.utm_orig.easting
    #         self.robot_origin.y = self.utm_orig.northing
    #         return        
    #     self.pub_orig.publish(self.robot_origin)
    #     self.process_gps(msg_gps)
    #     self.process_imu(msg_imu)
    #     self.kalman_filter()

    def kalman_filter(self):

        q = (self.pose.orientation.x, self.pose.orientation.y, self.pose.orientation.z, self.pose.orientation.w)
        roll = tf.transformations.euler_from_quaternion(q)[0]
        pitch = tf.transformations.euler_from_quaternion(q)[1]
        yaw = tf.transformations.euler_from_quaternion(q)[2]
        yaw = yaw + self.imu_rotate - float(self.imu_param["imu"])
        # yaw = yaw + self.imu_rotate - 0.7

        if self.start == False:
            self.start = True
            self.prior_pose.position.x = norm(loc = self.pose.position.x, scale = 100)
            self.prior_pose.position.y = norm(loc = self.pose.position.y, scale = 100)
            self.prior_pose.position.z = norm(loc = self.pose.position.z, scale = 100)
            self.prior_roll = norm(loc = roll, scale = 10)
            self.prior_pitch = norm(loc = pitch, scale = 10)
            self.prior_yaw = norm(loc = yaw, scale = 10)
            return

        covariance = self.covariance

        #p rediction step
        kernel = norm(loc = 0, scale = 2)
        kernel_euler = norm(loc = 0, scale = 0.5)
        x = self.pose.position.x
        y = self.pose.position.y
        z = self.pose.position.z
        
        predicted_x = norm(loc = self.prior_pose.position.x.mean()+kernel.mean(), scale = np.sqrt(self.prior_pose.position.x.var()+kernel.var()))
        predicted_y = norm(loc = self.prior_pose.position.y.mean()+kernel.mean(), scale = np.sqrt(self.prior_pose.position.y.var()+kernel.var()))
        predicted_z = norm(loc = self.prior_pose.position.z.mean()+kernel.mean(), scale = np.sqrt(self.prior_pose.position.z.var()+kernel.var()))
        predicted_roll = norm(loc = self.prior_roll.mean()+kernel_euler.mean(), scale = np.sqrt(self.prior_roll.var()+kernel_euler.var()))
        predicted_pitch = norm(loc = self.prior_pitch.mean()+kernel_euler.mean(), scale = np.sqrt(self.prior_pitch.var()+kernel_euler.var()))
        predicted_yaw = norm(loc = self.prior_yaw.mean()+kernel_euler.mean(), scale = np.sqrt(self.prior_yaw.var()+kernel_euler.var()))

        # update step
        posterior_x = self.update_con(predicted_x, x, 0.05)
        posterior_y = self.update_con(predicted_y, y, 0.05)
        posterior_z = self.update_con(predicted_z, z, 0.05)
        posterior_roll = self.update_con(predicted_roll, roll, 0.05)
        posterior_pitch = self.update_con(predicted_pitch, pitch, 0.05)
        posterior_yaw = self.update_con(predicted_yaw, yaw, 0.05)

        self.prior_roll = posterior_roll
        self.prior_pitch = posterior_pitch
        self.prior_yaw = posterior_yaw

        self.prior_pose.position.x = posterior_x
        self.prior_pose.position.y = posterior_y
        self.prior_pose.position.z = posterior_z   

        self.odometry.pose.pose.position.x = posterior_x.mean()
        self.odometry.pose.pose.position.y = posterior_y.mean()
        self.odometry.pose.pose.position.z = posterior_z.mean()
        kf_euler = posterior_yaw.mean()
        qu = tf.transformations.quaternion_from_euler(0, 0, kf_euler+self.imu_offset)
        pose = Pose()
        pose.orientation.x = qu[0]
        pose.orientation.y = qu[1]
        pose.orientation.z = qu[2]
        pose.orientation.w = qu[3]
        self.odometry.pose.pose.orientation = pose.orientation
        
        # publish
        self.odometry.header.stamp = rospy.Time.now()
        self.odometry.header.frame_id = "map"
        self.pub_odm.publish(self.odometry)

        # tf transform
        self.br.sendTransform((self.odometry.pose.pose.position.x, \
                         self.odometry.pose.pose.position.y, self.odometry.pose.pose.position.z), \
                        (self.odometry.pose.pose.orientation.x, self.odometry.pose.pose.orientation.y, \
                        self.odometry.pose.pose.orientation.z, self.odometry.pose.pose.orientation.w), \
                        rospy.Time.now(),"/base_link","/odom")

        q = tf.transformations.quaternion_from_euler(0, 0, 0)
        self.br.sendTransform((self.utm_orig.easting, self.utm_orig .northing, 0), \
            (q[0], q[1], q[2], q[3]), \
            rospy.Time.now(),"/map","/utm")

        rad_2_deg = 180/math.pi
        if self.debug:
            print("X = ", self.pose.position.x, ", Y = ", self.pose.position.y)
            print(", RPY = ", posterior_roll.mean()*rad_2_deg, posterior_pitch.mean()*rad_2_deg, posterior_yaw.mean()*rad_2_deg+self.imu_offset*rad_2_deg)
            print("========================================================")

    def cb_srv_imu_offest(self, request): 
        self.imu_offset = request.data
        print ("Set imu offset = " + str(self.imu_offset))
        return SetFloatResponse()

    def measurement(self, measurementx, variance):
        likelihood = norm(loc = measurementx, scale = np.sqrt(variance))
        return likelihood

    def gaussian_multiply(self, g1, g2):
        g1_mean, g1_var = g1.stats(moments='mv')
        g2_mean, g2_var = g2.stats(moments='mv')
        mean = (g1_var * g2_mean + g2_var * g1_mean) / (g1_var + g2_var)
        variance = (g1_var * g2_var) / (g1_var + g2_var)
        #print mean, variance
        return norm(loc = mean, scale = np.sqrt(variance))

    def update_con(self, prior, measurementz, covariance):
        likelihood = self.measurement(measurementz, covariance)
        posterior = self.gaussian_multiply(likelihood, prior)
        return posterior

    def on_shutdown(self):
        rospy.loginfo("[%s] Shutdown." %(self.node_name))

if __name__ == '__main__':
    rospy.init_node('localization_gps_imu_node',anonymous=False)
    localization_gps_imu_node = LocailizationGPSImu()
    rospy.on_shutdown(localization_gps_imu_node.on_shutdown)
    rospy.spin()

