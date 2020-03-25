#!/usr/bin/env python3
import rospy
import time
from brping import Ping1D
from asv_msgs.msg import SonarData, SonarDataList

class SONAR_SINGLE():
    def __init__(self):
        self.node_name = rospy.get_name()
        rospy.loginfo("[%s] Initializing " %(self.node_name))

        self.myPing = Ping1D()
        self.myPing.connect_serial("/dev/ttyUSB0", 115200)

        self.pub_sonar = rospy.Publisher("sonar", SonarDataList, queue_size=1)

        if self.myPing.initialize() is False:
            rospy.loginfo("Failed")
            exit(1)

        rospy.Timer(rospy.Duration(1.2), self.event_cb)

    def event_cb(self, event):
        data = self.myPing.get_distance()
        if data:
            sl = SonarDataList()
            s = SonarData()
            s.distance = int(data["distance"])
            sl.list.append(s)
            self.pub_sonar.publish(sl)
            # print("Distance: %s\tConfidence: %s%%" % (data["distance"], data["confidence"]))
        else:
            print("Failed to get distance data")
        time.sleep(0.1)

if __name__ == '__main__':
    rospy.init_node('SONAR_SINGLE')
    foo = SONAR_SINGLE()
    rospy.spin()