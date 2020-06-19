#!/usr/bin/env python3
import rospy
import time
import sys
from brping import Ping1D
from asv_msgs.msg import SonarData, SonarDataList

class SONAR_SINGLE():
    def __init__(self):
        self.node_name = rospy.get_name()
        rospy.loginfo("[%s] Initializing " %(self.node_name))

        self.p30Front = Ping1D()
        self.p30Left = Ping1D()
        self.p30Right = Ping1D()
        self.p30Down = Ping1D()

        self.sonar_front = SonarData()
        self.sonar_left = SonarData()
        self.sonar_right = SonarData()
        self.sonar_down = SonarData()

        if not self.check_port():
            rospy.loginfo("Failed  open the P30 sensors")
            exit(1)

        self.p30Front.connect_serial("/dev/sonar_front", 115200)
        self.p30Left.connect_serial("/dev/sonar_left", 115200)
        self.p30Right.connect_serial("/dev/sonar_right", 115200)
        self.p30Down.connect_serial("/dev/sonar_down", 115200)

        self.pub_sonar = rospy.Publisher("sonar", SonarDataList, queue_size=1)

        if (self.p30Front.initialize() and self.p30Left and self.p30Right and self.p30Down) is False:
            rospy.loginfo("Failed  open the P30 sensors")
            exit(1)

        rospy.Timer(rospy.Duration(0.1), self.event_cb)

    def event_cb(self, event):
        data_list = SonarDataList()

        data_front = self.p30Front.get_distance()
        data_left = self.p30Left.get_distance()
        data_right = self.p30Right.get_distance()
        data_down = self.p30Down.get_distance()

        if data_front:
            self.sonar_front.distance = float(data["distance"])
            self.sonar_front.confidence = float(data["confidence"])

        if data_left:
            self.sonar_left.distance = float(data["distance"])
            self.sonar_left.confidence = float(data["confidence"])

        if data_right:
            self.sonar_right.distance = float(data["distance"])
            self.sonar_right.confidence = float(data["confidence"])

        if data_down:
            self.sonar_down.distance = float(data["distance"])
            self.sonar_down.confidence = float(data["confidence"])

        data_list.append(self.sonar_front)
        data_list.append(self.sonar_left)
        data_list.append(self.sonar_right)
        data_list.append(self.sonar_down)
        self.pub_sonar.publish(sl)
        print(data_list[0].distance + ", " + data_list[1].distance + ", " + data_list[2].distance + ", " + data_list[3].distance)
        # print("Distance: %s\tConfidence: %s%%" % (data["distance"], data["confidence"]))

    def check_port(self):
        return os.path.exists("/dev/sonar_front") and os.path.exists("/dev/sonar_left") and os.path.exists("/dev/sonar_right") and os.path.exists("/dev/sonar_down")

if __name__ == '__main__':
    rospy.init_node('SONAR_SINGLE')
    foo = SONAR_SINGLE()
    rospy.spin()