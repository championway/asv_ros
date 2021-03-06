#!/usr/bin/env python3
import rospy
import time
from brping import Ping1D
from asv_msgs.msg import SonarData, SonarDataList

class P30_MULTI():
    def __init__(self):
        self.node_name = rospy.get_name()
        rospy.loginfo("[%s] Initializing " %(self.node_name))

        self.p30Front = Ping1D()
        self.p30Left = Ping1D()
        self.p30Right = Ping1D()
        self.p30Down = Ping1D()

        self.check_port()

        self.sonar_front = SonarData()
        self.sonar_left = SonarData()
        self.sonar_right = SonarData()
        self.sonar_down = SonarData()

        self.pub_sonar = rospy.Publisher("sonar", SonarDataList, queue_size=1)

        if (self.p30Front.initialize() and self.p30Left and self.p30Right and self.p30Down) is False:
            rospy.loginfo("Failed  open the P30 sensors")
            exit(1)

        rospy.Timer(rospy.Duration(0.1), self.event_cb)

    def event_cb(self, event):
        data_front = self.p30Front.get_distance()
        data_left = self.p30Left.get_distance()
        data_right = self.p30Right.get_distance()
        data_down = self.p30Down.get_distance()

        if data_front:
            self.sonar_front.distance = float(data_front["distance"])
            self.sonar_front.confidence = float(data_front["confidence"])

        if data_left:
            self.sonar_left.distance = float(data_left["distance"])
            self.sonar_left.confidence = float(data_left["confidence"])

        if data_right:
            self.sonar_right.distance = float(data_right["distance"])
            self.sonar_right.confidence = float(data_right["confidence"])

        if data_down:
            self.sonar_down.distance = float(data_down["distance"])
            self.sonar_down.confidence = float(data_down["confidence"])

        data_list = SonarDataList()
        data_list.list.append(self.sonar_front)
        data_list.list.append(self.sonar_left)
        data_list.list.append(self.sonar_right)
        data_list.list.append(self.sonar_down)
        self.pub_sonar.publish(data_list)
        print(str(data_list.list[0].distance) + ", " + str(data_list.list[1].distance) + ", " + str(data_list.list[2].distance) + ", " + str(data_list.list[3].distance))
        # print("Distance: %s\tConfidence: %s%%" % (data["distance"], data["confidence"]))

    def check_port(self):
        port_succ = True
        try:
            self.p30Front.connect_serial("/dev/sonar_front", 115200)
        except:
            rospy.loginfo("sonar_front not exist")
            port_succ = False

        try:
            self.p30Left.connect_serial("/dev/sonar_left", 115200)
        except:
            rospy.loginfo("sonar_left not exist")
            port_succ = False

        try:
            self.p30Right.connect_serial("/dev/sonar_right", 115200)
        except:
            rospy.loginfo("sonar_right not exist")
            port_succ = False

        try:
            self.p30Down.connect_serial("/dev/sonar_down", 115200)
        except:
            rospy.loginfo("sonar_down not exist")
            port_succ = False

        if not port_succ:
            exit()

if __name__ == '__main__':
    rospy.init_node('P30_MULTI')
    foo = P30_MULTI()
    rospy.spin()
