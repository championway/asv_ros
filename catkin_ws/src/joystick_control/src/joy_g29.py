#!/usr/bin/env python
import rospy
import math

from sensor_msgs.msg import Joy

class JoyG29(object):
    def __init__(self):
        self.node_name = rospy.get_name()
        rospy.loginfo("[%s] Initializing " %(self.node_name))
        self.pub_joy = rospy.Publisher("mapping_joy", Joy, queue_size=1)
        self.sub_joy = rospy.Subscriber("g29_joy", Joy, self.cbJoy, queue_size=1)
            
    def cbJoy(self, joy_msg):
        out_msg = Joy()
        out_msg.header = joy_msg.header
        # 
        out_msg.axes = [0.] * 6

        # A, B, X, Y, LB, RB, back, start, power, btn_stick_left, btn stick right
        # 0, 1, 2, 3,  4,  5,    6,     7,     8,              9,              10
        out_msg.buttons = [0] * 10

        # X -> A
        out_msg.buttons[0] = joy_msg.buttons[0]
        # circle -> B
        out_msg.buttons[1] = joy_msg.buttons[2]
        # square -> X
        out_msg.buttons[2] = joy_msg.buttons[1]
        # triangle -> Y
        out_msg.buttons[3] = joy_msg.buttons[3]
        # share -> start
        out_msg.buttons[7] = joy_msg.buttons[8]
        # logo -> Power
        out_msg.buttons[8] = joy_msg.buttons[24]
        # accelerator
        out_msg.axes[1] = (joy_msg.axes[2] - joy_msg.axes[3]) / 2.
        # steering wheel -> Left/Right Stick
        out_msg.axes[3] = joy_msg.axes[0]
        # up_down
        out_msg.axes[2] = 1.
        out_msg.axes[5] = 1.
        if out_msg.buttons[4] == 1 and out_msg.buttons[5] == 0: # RT
            out_msg.axes[5] = -joy_msg.axes[1]
        elif out_msg.buttons[4] == 0 and out_msg.buttons[1] == 0: # LT
            out_msg.axes[2] = -joy_msg.axes[1]

        self.pub_joy.publish(out_msg)


    def on_shutdown(self):
        rospy.loginfo("shutting down [%s]" %(self.node_name))

if __name__ == "__main__":
    rospy.init_node("JoyG29",anonymous=False)
    joy_g29 = JoyG29()
    rospy.on_shutdown(joy_g29.on_shutdown)
    rospy.spin()
