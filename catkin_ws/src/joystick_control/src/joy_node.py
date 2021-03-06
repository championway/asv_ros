#!/usr/bin/env python
import rospy
import math

import yaml
from sensor_msgs.msg import Joy
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from asv_msgs.msg import MotorCmd, Heading, ControlCmd, Status
from asv_msgs.srv import SetCmd, SetCmdRequest, SetCmdResponse, SetValue, SetValueResponse, SetString, SetStringResponse
import rospkg
import os
from robotx_gazebo.msg import UsvDrive

class JoyMapper(object):
    def __init__(self):
        self.node_name = rospy.get_name()
        rospy.loginfo("[%s] Initializing " %(self.node_name))

        self.gazebo = rospy.get_param("~gazebo", False)
        self.motor_mode = rospy.get_param("~motor_mode", 0)
        if self.gazebo:
            rospy.loginfo("Using gazebo")
        else:
            rospy.loginfo("Not using gazebo")

        # Publications
        self.pub_motor_cmd = rospy.Publisher("motor_cmd", MotorCmd, queue_size=1)
        if self.gazebo:
            self.pub_motor_cmd = rospy.Publisher("/cmd_drive",UsvDrive,queue_size=1)
        self.pub_status = rospy.Publisher("status", Status, queue_size=1)

        #varibles
        self.emergencyStop = False
        self.autoMode = False
        self.motor_msg = MotorCmd()
        self.motor_msg.right = 0
        self.motor_msg.left = 0
        self.motor_msg.vertical = 0
        self.motor_msg.horizontal = 0
        self.MAX = 0.6
        self.MIN = -0.6
        self.dive_MAX = 0.8
        self.dive_MIN = -0.8
        self.check_no_signal = False
        self.navigate = False
        self.useVJoystick = False
        self.pre_ControlMsg = ControlCmd()
        self.alpha_v = 1.0
        self.trim_left_v = 1.0
        self.trim_right_v = 1.0

        self.trim_parent = ["right", "left"]
        self.param_srv = rospy.Service("trim_config", SetString, self.trim_cb)
        rospack = rospkg.RosPack()
        self.trim_param_path = os.path.join(rospack.get_path('asv_config'), "calibration/motor_trim.yaml")
        self.trim_param = None

        with open (self.trim_param_path, 'r') as file:
            self.trim_param = yaml.safe_load(file)

        self.set_trim_param()

        self.no_signal = rospy.Service("no_signal", SetBool, self.no_signal_cb)
        self.estop_srv = rospy.Service("estop", SetBool, self.estop_cb)
        self.gui_cmd_srv = rospy.Service("gui_cmd", SetCmd, self.gui_cmd_cb)
        
        self.alpha_srv = rospy.Service("alphaV", SetValue, self.alpha_cb)
        
        # Subscriptions
        self.sub_cmd_drive = rospy.Subscriber("cmd_drive",MotorCmd, self.cbCmd, queue_size=1)
        self.sub_joy = rospy.Subscriber("joy", Joy, self.cbJoy, queue_size=1)
        self.sub_control_cmd = rospy.Subscriber("cmd_control", ControlCmd, self.cbControlCmd, queue_size = 1)

        #timer
        self.timer = rospy.Timer(rospy.Duration(0.2),self.cb_publish)

    def cb_publish(self, event):
        motor_out = MotorCmd()
        motor_out.right = self.motor_msg.right
        motor_out.left = self.motor_msg.left
        motor_out.vertical = self.motor_msg.vertical
        motor_out.horizontal = self.motor_msg.horizontal
        if self.emergencyStop:
            motor_out.right = 0
            motor_out.left = 0
            motor_out.horizontal = 0

        if self.check_no_signal and self.autoMode:
            # let ASV float up when no GPS signal receive
            motor_out.right = 0
            motor_out.left = 0
            motor_out.horizontal = 0
            motor_out.vertical = -0.5

        # Calibration trimming left/right motor
        motor_out.right = max(min(motor_out.right * self.alpha_v  * self.trim_left_v, self.MAX), self.MIN)
        motor_out.left = max(min(motor_out.left * self.alpha_v  * self.trim_right_v, self.MAX), self.MIN)
        

        status = Status()
        status.right = motor_out.right
        status.left = motor_out.left
        status.vertical = motor_out.vertical
        status.horizontal = motor_out.horizontal
        status.manual = not self.autoMode
        status.estop = self.emergencyStop
        status.navigate = self.navigate
        # print(self.trim_right_v, self.trim_left_v)
        
        self.pub_status.publish(status)
        if self.gazebo:
            motor_usv_msg = UsvDrive()
            motor_usv_msg.right = -status.left
            motor_usv_msg.left = status.right
            self.pub_motor_cmd.publish(motor_usv_msg)
        else:
            self.pub_motor_cmd.publish(motor_out)

    def alpha_cb(self, req):
        res = SetValueResponse()
        self.alpha_v = req.value
        res.success = True
        return res
            
    def set_trim_param(self):
        self.trim_left_v = float(self.trim_param['left'])
        self.trim_right_v = float(self.trim_param['right'])

    def trim_cb(self, req):
        s = req.str
        ss = s.split('/')
        string_valid = False
        if len(ss) == 2:
            if ss[0] in self.trim_parent:
                try:
                    string_valid = True
                    self.trim_param[ss[0]] = float(ss[1])
                    with open(self.trim_param_path, "w") as file:
                        yaml.dump(self.trim_param, file)
                    self.set_trim_param()
                except:
                    pass
        res = SetStringResponse()
        if string_valid:
            res.success = True
        else:
            res.success = False
        return res

    def cbCmd(self, cmd_msg):
        # From auto mode PID result
        if not self.emergencyStop and self.autoMode:
            self.motor_msg.left = -max(min(cmd_msg.right, self.MAX), self.MIN)
            self.motor_msg.right = max(min(cmd_msg.left, self.MAX), self.MIN)
            self.motor_msg.vertical = max(min(cmd_msg.vertical, self.MAX), self.MIN)
            self.motor_msg.horizontal = max(min(cmd_msg.horizontal, self.MAX), self.MIN)
            
    def cbJoy(self, joy_msg):
        # From joystick message
        self.processButtons(joy_msg)
        if not self.emergencyStop and not self.autoMode:
            self.joy = joy_msg
            boat_heading_msg = Heading()
            boat_heading_msg.speed = math.sqrt((math.pow(self.joy.axes[1],2)+math.pow(self.joy.axes[3],2))/2)
            boat_heading_msg.phi = math.atan2(self.joy.axes[1],self.joy.axes[3])
            speed = boat_heading_msg.speed*math.sin(boat_heading_msg.phi)
            difference = boat_heading_msg.speed*math.cos(boat_heading_msg.phi)
            if self.motor_mode == 0:
                self.motor_msg.left = -max(min(speed + difference, self.MAX), self.MIN)
                self.motor_msg.right = max(min(speed - difference, self.MAX), self.MIN)
            elif self.motor_mode == 1:
                self.motor_msg.left = -max(min(speed, self.MAX), self.MIN)
                self.motor_msg.right = max(min(speed, self.MAX), self.MIN)
                self.motor_msg.horizontal = max(min(difference , self.MAX), self.MIN)
            go_down = -(self.joy.axes[2] - 1.)/2.
            go_up = -(self.joy.axes[5] - 1.)/2.
            self.motor_msg.vertical = max(min((go_down - go_up)*self.dive_MAX, self.dive_MAX), self.dive_MIN)

    def processButtons(self, joy_msg):
        # Button B
        if (joy_msg.buttons[1] == 1):
            self.navigate = True
            self.start_navigation(True)

        # Button A
        if (joy_msg.buttons[0] == 1):
            self.navigate = False
            self.start_navigation(False)
        
        # Start button
        elif (joy_msg.buttons[7] == 1):
            self.autoMode = not self.autoMode
            if self.autoMode:
                rospy.loginfo('going auto')
            else:
                rospy.loginfo('going manual')

        # Power/middle button
        elif (joy_msg.buttons[8] == 1):
            self.emergencyStop = not self.emergencyStop
            if self.emergencyStop:
                rospy.loginfo('emergency stop activate')
                self.motor_msg.right = 0
                self.motor_msg.left = 0
                self.motor_msg.horizontal = 0
                self.motor_msg.vertical = 0
            else:
                rospy.loginfo('emergency stop release')

        else:
            some_active = sum(joy_msg.buttons) > 0
            if some_active:
                pass
                #rospy.loginfo('No binding for joy_msg.buttons = %s' % str(joy_msg.buttons))

    def gui_cmd_cb(self, req):
        if (req.title == 'usevjoystick'):
            self.useVJoystick = req.data
        elif (req.title == 'navigate'):
            self.navigate = req.data
            if req.data:
                self.start_navigation(True)
                rospy.loginfo("Start Navigation!")
            else:
                self.start_navigation(False)
                rospy.loginfo("Reset Navigation!")
        elif (req.title == 'manual'):
            self.autoMode = not req.data
        elif (req.title == 'estop'):
            self.emergencyStop = req.data
            if req.data:
                self.motor_msg.right = 0
                self.motor_msg.left = 0
                self.motor_msg.horizontal = 0
                self.motor_msg.vertical = 0
        res = SetCmdResponse()
        res.success = True
        return res

    def cbControlCmd(self, msg):
        # if self.pre_ControlMsg.manual != msg.manual:
        #     self.autoMode = not msg.manual

        # if self.pre_ControlMsg.navigate != msg.navigate:
        #     self.navigate = msg.navigate
        #     if msg.navigate:
        #         self.start_navigation(True)
        #         rospy.loginfo("Start Navigation!")
        #     else:
        #         self.start_navigation(False)
        #         rospy.loginfo("Reset Navigation!")

        # if self.pre_ControlMsg.estop != msg.estop:
        #     self.emergencyStop = msg.estop
            
        # if self.emergencyStop:
        #     self.motor_msg.right = 0
        #     self.motor_msg.left = 0

        # From GUI virtual joystick
        if not self.emergencyStop and not self.autoMode and self.useVJoystick:
            boat_heading_msg = Heading()
            forward = -msg.forward/100.
            right = -msg.right/100.
            boat_heading_msg.speed = math.sqrt((math.pow(forward,2)+math.pow(right,2))/2)
            boat_heading_msg.phi = math.atan2(forward, right)
            speed = boat_heading_msg.speed*math.sin(boat_heading_msg.phi)
            difference = boat_heading_msg.speed*math.cos(boat_heading_msg.phi)
            if self.motor_mode == 0:
                self.motor_msg.right = -max(min(speed + difference , self.MAX), self.MIN)
                self.motor_msg.left = max(min(speed - difference , self.MAX), self.MIN)
            elif self.motor_mode == 1:
                self.motor_msg.right = -max(min(speed, self.MAX), self.MIN)
                self.motor_msg.left = max(min(speed, self.MAX), self.MIN)
                self.motor_msg.horizontal = max(min(difference, self.MAX), self.MIN)
            go_up = -msg.up/100.
            self.motor_msg.vertical = max(min((go_up)*self.dive_MAX, self.dive_MAX), self.dive_MIN)

        # self.pre_ControlMsg = msg


    def start_navigation(self, isTrue):
        set_bool = SetBoolRequest()
        if isTrue:
            set_bool.data = True
        else:
            set_bool.data = False
        try:
            srv = rospy.ServiceProxy('start_navigation', SetBool)
            resp = srv(set_bool)
            return resp
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def no_signal_cb(self, req):
        if req.data == True:
            self.check_no_signal = True
            rospy.loginfo("No Signal")
        else:
            self.check_no_signal = False
            self.motor_msg.vertical = 0
            rospy.loginfo("Got Signal")
        res = SetBoolResponse()
        res.success = True
        res.message = "recieved"
        return res

    def estop_cb(self, req):
        if req.data == True:
            self.emergencyStop = True
            rospy.loginfo("EStop")
        else:
            self.emergencyStop = False
            rospy.loginfo("Release EStop")
        res = SetBoolResponse()
        res.success = True
        res.message = "recieved"
        return res

    def on_shutdown(self):
        self.motor_msg.right = 0
        self.motor_msg.left = 0
        self.motor_msg.vertical = 0
        self.motor_msg.horizontal = 0
        self.pub_motor_cmd.publish(self.motor_msg)
        rospy.loginfo("shutting down [%s]" %(self.node_name))

if __name__ == "__main__":
    rospy.init_node("joy_mapper",anonymous=False)
    joy_mapper = JoyMapper()
    rospy.on_shutdown(joy_mapper.on_shutdown)
    rospy.spin()
