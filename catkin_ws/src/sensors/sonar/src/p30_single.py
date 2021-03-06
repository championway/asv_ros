#!/usr/bin/env python3
import rospy
import time
from brping import Ping1D
from asv_msgs.msg import SonarData, SonarDataList

class P30_SINGLE():
    def __init__(self):
        self.node_name = rospy.get_name()
        rospy.loginfo("[%s] Initializing " %(self.node_name))
        self.p30_port = rospy.get_param("~p30_port", "/dev/sonar_front")

        self.myPing = Ping1D()
        self.myPing.connect_serial(self.p30_port, 115200)

        self.pub_sonar = rospy.Publisher("sonar", SonarDataList, queue_size=1)

        if self.myPing.initialize() is False:
            rospy.loginfo("Failed")
            exit(1)

        rospy.Timer(rospy.Duration(0.1), self.event_cb)

    def event_cb(self, event):
        data = self.myPing.get_distance()
        if data:
            sl = SonarDataList()
            s = SonarData()
            s.distance = float(data["distance"])
            s.confidence = float(data["confidence"])
            sl.list.append(s)
            self.pub_sonar.publish(sl)
            print("Distance: %s\tConfidence: %s%%" % (data["distance"], data["confidence"]))
        else:
            print("Failed to get distance data")

if __name__ == '__main__':
    rospy.init_node('P30_SINGLE')
    foo = P30_SINGLE()
    rospy.spin()
