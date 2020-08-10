#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auv.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import rospy
from PyQt4 import QtCore, QtGui
from asv_msgs.msg import ControlCmd, Status
from std_msgs.msg import Int32
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest
from asv_msgs.srv import SetString, SetStringResponse, SetCmd, SetCmdRequest, SetCmdResponse, SetValue, SetValueResponse
from sensor_msgs.msg import Image, CompressedImage, NavSatFix, BatteryState
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import cv2
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def run_(self, message):
        self.trigger.emit(message)

class ImgThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(ImgThread, self).__init__(parent)
    def run_(self, qt_image):
       self.trigger.emit(qt_image)

class Ui_Form(object):

    def __init__(self):
        self.alphaCmd = 0
        self.leftrightCmd = 0
        self.updownCmd = 0
        self.forbackCmd = 0
        self.dead_zone = 10
        self.battery = 0.
        self.battery_full = 16.8
        self.useVJoyStick = False
        self.pre_status = Status()
        self.cv_bridge = CvBridge()
        self.is_compressed = False
        self.estop = False
        self.manual = True
        self.navigate = False
        self.lat = 0
        self.lng = 0
        self.navStatus = 0
        self.has_ImgSub = False
        self.master = rospy.get_master()
        self.cmd_publiser = rospy.Publisher("/ASV/cmd_control", ControlCmd, queue_size = 1)
        self.timer = rospy.Timer(rospy.Duration(0.1),self.cb_publish)

    def cb_publish(self, event):
        try:
            self.master.getSystemState()
            self.internet_thread.run_('1')
        except:
            self.internet_thread.run_('0')
        cmd = ControlCmd()
        cmd.forward = float(self.forbackCmd)
        cmd.right = float(self.leftrightCmd)
        cmd.up = float(self.updownCmd)
        # cmd.useVJoystick = self.useVJoyStick
        # cmd.estop = self.estop
        # cmd.manual = self.manual
        # cmd.navigate = self.navigate
        self.cmd_publiser.publish(cmd)

    def cbNavStatus(self, msg):
        self.navStatus = msg.data

    def cbBattery(self, msg):
        self.battery = msg.voltage

    def cbStatus(self, msg):
        # if self.pre_status.manual != msg.manual:
        #     self.manual = msg.manual
        # if self.pre_status.estop != msg.estop:
        #     self.estop = msg.estop
        # if self.pre_status.navigate != msg.navigate:
        #     self.navigate = msg.navigate
        self.check_Navigate(msg.navigate)
        text = ""
        battery_percentage = (self.battery/self.battery_full)*100.
        text = "{:<18}".format("[Battery]") + "%.3f V  (%.2f" %(self.battery, battery_percentage) + "%)\n"
        text += "{:<18}".format("[Left Motor]") + str(msg.left) + "\n"
        text += "{:<18}".format("[Right Motor]") + str(msg.right) + "\n"
        text += "{:<18}".format("[Up/Down Motor]") + str(msg.horizontal) + "\n"
        if msg.estop:
            text += "{:<18}".format("[E-Stop]") + "True\n"
        else:
            text += "{:<18}".format("[E-Stop]") + "False\n"
        if msg.manual:
            text += "{:<18}".format("[Manual]") + "True\n"
        else:
            text += "{:<18}".format("[Manual]") + "False\n"
        if msg.navigate:
            text += "{:<18}".format("[Navigation]") + "True\n"
        else:
            text += "{:<18}".format("[Navigation]") + "False\n"
        if (self.navStatus!=-1):
            text += "{:<18}".format("[Waypoint]") + str(self.navStatus) + "\n"
        else:
            text += "{:<18}".format("[Waypoint]") + "Destination\n"

        # self.update_status_text(text)
        self.pre_status = msg
        self.thread.run_(text)

    def cbImage(self, msg):
        try:
            if self.is_compressed:
                np_arr = np.fromstring(msg.data, np.uint8)
                cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            else:
                cv_image = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            print(e)
        self.img1_thread.run_(cv_image)
        # else:
        #     self.img2_thread.run_(cv_image)

    def update_status_text(self, msg):
        # self.statusOutput.clear()
        self.statusOutput.setText(msg)

    def update_internet_status(self, is_connect):
        if is_connect == '1':
            self.status_internet.setText(_translate("Form", "Connected 連線", None))
            self.status_internet.setStyleSheet("color: rgb(0, 0, 255);")
        else:
            self.status_internet.setText(_translate("Form", "Disconnected 斷線", None))
            self.status_internet.setStyleSheet("color: rgb(255, 0, 0);")

    def update_LatLng(self, msg):
        self.LatLngOutput.setText(msg)

    def update_image_1(self, cv_image):
        w = self.imageView_1.width()
        h = self.imageView_1.height()
        ratio_w = w/float(cv_image.shape[1])
        ratio_h = h/float(cv_image.shape[0])
        if ratio_w < ratio_h:
            h = int(float(cv_image.shape[0])*ratio_w)
        else:
            w = int(float(cv_image.shape[1])*ratio_h)
        cv_image = cv2.resize(cv_image, (w, h), interpolation=cv2.INTER_CUBIC)
        qt_image = QtGui.QImage(cv_image.data, w, h, cv_image.strides[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.imageView_1.setPixmap(QtGui.QPixmap.fromImage(qt_image))

    # def update_image_2(self, cv_image):
    #     w = self.imageView_2.width()
    #     h = self.imageView_2.height()
    #     ratio_w = w/float(cv_image.shape[1])
    #     ratio_h = h/float(cv_image.shape[0])
    #     if ratio_w < ratio_h:
    #         h = int(float(cv_image.shape[0])*ratio_w)
    #     else:
    #         w = int(float(cv_image.shape[1])*ratio_h)
    #     cv_image = cv2.resize(cv_image, (w, h), interpolation=cv2.INTER_CUBIC)
    #     qt_image = QtGui.QImage(cv_image.data, w, h, cv_image.strides[0], QtGui.QImage.Format_RGB888).rgbSwapped()
    #     self.imageView_2.setPixmap(QtGui.QPixmap.fromImage(qt_image))

    def cb_VJoyStick(self):
        self.check_VJoystick()

    def check_VJoystick(self):
        if self.useVJoyStickBtn.isChecked():
            self.send_cmd("usevjoystick", True)
            # self.useVJoyStick = True
            self.updownScroll.setEnabled(True)
            self.leftrightScroll.setEnabled(True)
            self.forbackScroll.setEnabled(True)
            self.updownValue.setEnabled(True)
            self.leftrightValue.setEnabled(True)
            self.forbackValue.setEnabled(True)
        else:
            self.send_cmd("usevjoystick", False)
            # self.useVJoyStick = False
            self.updownScroll.setEnabled(False)
            self.leftrightScroll.setEnabled(False)
            self.forbackScroll.setEnabled(False)
            self.updownValue.setEnabled(False)
            self.leftrightValue.setEnabled(False)
            self.forbackValue.setEnabled(False)

    def check_Navigate(self, isNav):
        if isNav:
            self.navigateBtn.setEnabled(False)
            self.resetNavigateBtn.setEnabled(True)
        else:
            self.navigateBtn.setEnabled(True)
            self.resetNavigateBtn.setEnabled(False)
        
    def cb_navigate(self):
        text = str(self.textEditPath.toPlainText())
        self.send_path(text)
        # self.navigate = True

    def cbGPS(self, msg):
        self.lat = msg.latitude
        self.lng = msg.longitude

    def cb_LatLngBtn(self):
        self.latlngThread.run_(str(self.lat) + ", " + str(self.lng))

    def cb_FileBtn(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self.window, 'OpenFile')
        # self.myTextBox.setText(fileName)
        text=open(fileName).read()
        # text_edit.setPlainText(text)
        rospy.loginfo("Load file: " + fileName)
        # self.textEditPath.append(text)
        self.textEditPath.setPlainText(text)

    def cb_resetNavigate(self):
        self.send_cmd("navigate", False)
        # self.navigate = False

    def cb_manual(self):
        self.send_cmd("manual", True)
        # self.manual = True

    def cb_auto(self):
        self.send_cmd("manual", False)
        # self.manual = False

    def cb_estop(self):
        self.send_cmd("estop", True)
        # self.estop = True

    def cb_estop_release(self):
        self.send_cmd("estop", False)
        # self.estop = False

    def cb_imgBtn(self):
        null_img = np.zeros((300, 450, 3), np.uint8)
        null_img[:,:] = (200, 200, 200)
        self.img1_thread.run_(null_img)
        topic = str(self.ImgTopicInput.toPlainText())
        if topic != "":
            if self.has_ImgSub:
                self.sub_image.unregister()
            self.has_ImgSub = True
            self.sub_image = rospy.Subscriber(topic, Image , self.cbImage, queue_size=1)
        # self.img2_thread.run_(null_img)

    def cb_recordPathBtn(self):
        fname = str(self.RecordPathInput.toPlainText())
        if fname != "":
            self.record_path(fname)

    def cb_savePathBtn(self):
        self.save_path()

    def send_alpha(self, alpha):
        try:
            srv = rospy.ServiceProxy('/ASV/alphaV', SetValue)
            resp = srv(alpha)
            # if resp.success:
            #     rospy.loginfo("Send Alpha Success")
            return resp
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def send_path(self, txt):
        try:
            srv = rospy.ServiceProxy('/ASV/path_txt', SetString)
            resp = srv(txt)
            if resp.success:
                self.send_cmd("navigate", True)
                # self.navigate = True
                rospy.loginfo("Send Path Success")
            return resp
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def record_path(self, txt):
        try:
            srv = rospy.ServiceProxy('/ASV/record_path', SetString)
            resp = srv(txt)
            if resp.success:
                self.RecordPathBtn.setEnabled(False)
                self.SavePathBtn.setEnabled(True)
                rospy.loginfo("Record Path Success")
            return resp
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def save_path(self):
        set_bool = SetBoolRequest()
        set_bool.data = True
        try:
            srv = rospy.ServiceProxy('/ASV/save_path', SetBool)
            resp = srv(set_bool)
            self.RecordPathBtn.setEnabled(True)
            self.SavePathBtn.setEnabled(False)
            rospy.loginfo("Save Path Success")            
            return resp
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e

    def send_cmd(self, title, data):
        try:
            srv = rospy.ServiceProxy('/ASV/gui_cmd', SetCmd)
            set_cmd = SetCmdRequest()
            set_cmd.title = title
            set_cmd.data = data
            resp = srv(set_cmd)
            if resp.success:
                rospy.loginfo("Send command successfully")
            return resp
        except rospy.ServiceException, e:
            return False

    def updownScrollMoved(self):
        self.updownCmd = self.updownScroll.value()-100
        if (abs(self.updownCmd) < self.dead_zone):
            self.updownCmd = 0
        self.updownValue.setText("Value: " + str(self.updownCmd))

    def leftrightScrollMoved(self):
        self.leftrightCmd = self.leftrightScroll.value()-100
        if (abs(self.leftrightCmd) < self.dead_zone):
            self.leftrightCmd = 0
        self.leftrightValue.setText("Value: " + str(self.leftrightCmd))

    def forbackScrollMoved(self):
        self.forbackCmd = -(self.forbackScroll.value()-100)
        if (abs(self.forbackCmd) < self.dead_zone):
            self.forbackCmd = 0
        self.forbackValue.setText("Value: " + str(self.forbackCmd))

    def alphaVScrollMoved(self):
        self.alphaCmd = (float(self.alphaVScroll.value())/100.)**2
        self.alphaVValue.setText("Alpha: " + "%.2f" % self.alphaCmd)
        self.send_alpha(self.alphaCmd)

    def setupUi(self, Form):
        self.window = Form
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1038, 689)
        self.navigateBtn = QtGui.QPushButton(Form)
        self.navigateBtn.setGeometry(QtCore.QRect(620, 50, 181, 51))
        self.navigateBtn.setObjectName(_fromUtf8("navigateBtn"))
        self.manualBtn = QtGui.QPushButton(Form)
        self.manualBtn.setGeometry(QtCore.QRect(660, 130, 141, 51))
        self.manualBtn.setObjectName(_fromUtf8("manualBtn"))
        self.autoBtn = QtGui.QPushButton(Form)
        self.autoBtn.setGeometry(QtCore.QRect(810, 130, 141, 51))
        self.autoBtn.setObjectName(_fromUtf8("autoBtn"))
        self.estopBtn = QtGui.QPushButton(Form)
        self.estopBtn.setGeometry(QtCore.QRect(610, 220, 191, 61))
        self.estopBtn.setObjectName(_fromUtf8("estopBtn"))
        self.imageView_1 = QtGui.QLabel(Form)
        self.imageView_1.setGeometry(QtCore.QRect(10, 10, 571, 331))
        self.imageView_1.setObjectName(_fromUtf8("imageView_1"))
        self.leftrightScroll = QtGui.QScrollBar(Form)
        self.leftrightScroll.setGeometry(QtCore.QRect(700, 530, 191, 16))
        self.leftrightScroll.setOrientation(QtCore.Qt.Horizontal)
        self.leftrightScroll.setObjectName(_fromUtf8("leftrightScroll"))
        self.updownName = QtGui.QTextBrowser(Form)
        self.updownName.setGeometry(QtCore.QRect(600, 390, 101, 31))
        self.updownName.setObjectName(_fromUtf8("updownName"))
        self.forbackName = QtGui.QTextBrowser(Form)
        self.forbackName.setGeometry(QtCore.QRect(880, 390, 151, 31))
        self.forbackName.setObjectName(_fromUtf8("forbackName"))
        self.leftrightName = QtGui.QTextBrowser(Form)
        self.leftrightName.setGeometry(QtCore.QRect(740, 390, 101, 31))
        self.leftrightName.setObjectName(_fromUtf8("leftrightName"))
        self.updownScroll = QtGui.QScrollBar(Form)
        self.updownScroll.setGeometry(QtCore.QRect(640, 430, 16, 201))
        self.updownScroll.setOrientation(QtCore.Qt.Vertical)
        self.updownScroll.setObjectName(_fromUtf8("updownScroll"))
        self.statusOutput = QtGui.QTextBrowser(Form)
        self.statusOutput.setGeometry(QtCore.QRect(300, 510, 291, 161))
        self.statusOutput.setObjectName(_fromUtf8("statusOutput"))
        self.updownValue = QtGui.QTextBrowser(Form)
        self.updownValue.setGeometry(QtCore.QRect(600, 640, 101, 31))
        self.updownValue.setObjectName(_fromUtf8("updownValue"))
        self.forbackScroll = QtGui.QScrollBar(Form)
        self.forbackScroll.setGeometry(QtCore.QRect(940, 430, 16, 201))
        self.forbackScroll.setOrientation(QtCore.Qt.Vertical)
        self.forbackScroll.setObjectName(_fromUtf8("forbackScroll"))
        self.leftrightValue = QtGui.QTextBrowser(Form)
        self.leftrightValue.setGeometry(QtCore.QRect(750, 640, 101, 31))
        self.leftrightValue.setObjectName(_fromUtf8("leftrightValue"))
        self.forbackValue = QtGui.QTextBrowser(Form)
        self.forbackValue.setGeometry(QtCore.QRect(890, 640, 101, 31))
        self.forbackValue.setObjectName(_fromUtf8("forbackValue"))
        self.alphaVValue = QtGui.QTextBrowser(Form)
        self.alphaVValue.setGeometry(QtCore.QRect(630, 295, 101, 31))
        self.alphaVValue.setObjectName(_fromUtf8("alphaVValue"))
        self.alphaVScroll = QtGui.QScrollBar(Form)
        self.alphaVScroll.setGeometry(QtCore.QRect(750, 300, 260, 22))
        self.alphaVScroll.setOrientation(QtCore.Qt.Horizontal)
        self.alphaVScroll.setObjectName(_fromUtf8("alphaVScroll"))
        self.useVJoyStickBtn = QtGui.QRadioButton(Form)
        self.useVJoyStickBtn.setGeometry(QtCore.QRect(680, 340, 271, 22))
        self.useVJoyStickBtn.setObjectName(_fromUtf8("useVJoyStickBtn"))
        self.estopReleaseBtn = QtGui.QPushButton(Form)
        self.estopReleaseBtn.setGeometry(QtCore.QRect(810, 220, 221, 61))
        self.estopReleaseBtn.setObjectName(_fromUtf8("estopReleaseBtn"))
        self.resetNavigateBtn = QtGui.QPushButton(Form)
        self.resetNavigateBtn.setGeometry(QtCore.QRect(810, 50, 181, 51))
        self.resetNavigateBtn.setObjectName(_fromUtf8("resetNavigateBtn"))
        self.ImgTopicBtn = QtGui.QPushButton(Form)
        self.ImgTopicBtn.setGeometry(QtCore.QRect(510, 350, 71, 27))
        self.ImgTopicBtn.setObjectName(_fromUtf8("ImgTopicBtn"))
        self.RecordPathBtn = QtGui.QPushButton(Form)
        self.RecordPathBtn.setGeometry(QtCore.QRect(430, 390, 71, 27))
        self.RecordPathBtn.setObjectName(_fromUtf8("RecordPathBtn"))
        self.SavePathBtn = QtGui.QPushButton(Form)
        self.SavePathBtn.setGeometry(QtCore.QRect(510, 390, 71, 27))
        self.SavePathBtn.setObjectName(_fromUtf8("SavePathBtn"))
        self.path_text = QtGui.QLabel(Form)
        self.path_text.setGeometry(QtCore.QRect(110, 480, 68, 27))
        self.path_text.setObjectName(_fromUtf8("path_text"))
        self.FileBtn = QtGui.QPushButton(Form)
        self.FileBtn.setGeometry(QtCore.QRect(200, 480, 50, 27))
        self.FileBtn.setObjectName(_fromUtf8("FileBtn"))
        self.status_text = QtGui.QLabel(Form)
        self.status_text.setGeometry(QtCore.QRect(410, 480, 81, 27))
        self.status_text.setObjectName(_fromUtf8("status_text"))
        self.status_internet = QtGui.QLabel(Form)
        self.status_internet.setGeometry(QtCore.QRect(760, 20, 161, 17))
        self.status_internet.setObjectName(_fromUtf8("status_internet"))
        self.textEditPath = QtGui.QTextEdit(Form)
        self.textEditPath.setGeometry(QtCore.QRect(10, 510, 281, 161))
        self.textEditPath.setObjectName(_fromUtf8("textEditPath"))
        self.ImgTopicInput = QtGui.QTextEdit(Form)
        self.ImgTopicInput.setGeometry(QtCore.QRect(100, 350, 401, 31))
        self.ImgTopicInput.setObjectName(_fromUtf8("ImgTopicInput"))
        self.RecordPathInput = QtGui.QTextEdit(Form)
        self.RecordPathInput.setGeometry(QtCore.QRect(100, 390, 321, 31))
        self.RecordPathInput.setObjectName(_fromUtf8("RecordPathInput"))
        self.LatLngOutput = QtGui.QTextBrowser(Form)
        self.LatLngOutput.setGeometry(QtCore.QRect(100, 430, 301, 31))
        self.LatLngOutput.setObjectName(_fromUtf8("LatLngOutput"))
        self.path_text_2 = QtGui.QLabel(Form)
        self.path_text_2.setGeometry(QtCore.QRect(10, 350, 91, 31))
        self.path_text_2.setObjectName(_fromUtf8("path_text_2"))
        self.record_path_text = QtGui.QLabel(Form)
        self.record_path_text.setGeometry(QtCore.QRect(10, 390, 91, 31))
        self.record_path_text.setObjectName(_fromUtf8("record_path_text"))
        self.path_text_3 = QtGui.QLabel(Form)
        self.path_text_3.setGeometry(QtCore.QRect(10, 430, 91, 31))
        self.path_text_3.setObjectName(_fromUtf8("path_text_3"))
        self.LatLngBtn = QtGui.QPushButton(Form)
        self.LatLngBtn.setGeometry(QtCore.QRect(410, 430, 171, 27))
        self.LatLngBtn.setObjectName(_fromUtf8("LatLngBtn"))
        self.retranslateUi(Form)
        
        QtCore.QObject.connect(self.navigateBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_navigate)
        QtCore.QObject.connect(self.resetNavigateBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_resetNavigate)
        QtCore.QObject.connect(self.manualBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_manual)
        QtCore.QObject.connect(self.autoBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_auto)
        QtCore.QObject.connect(self.estopBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_estop)
        QtCore.QObject.connect(self.estopReleaseBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_estop_release)
        QtCore.QObject.connect(self.ImgTopicBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_imgBtn)
        QtCore.QObject.connect(self.RecordPathBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_recordPathBtn)
        QtCore.QObject.connect(self.SavePathBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_savePathBtn)
        QtCore.QObject.connect(self.LatLngBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_LatLngBtn)
        QtCore.QObject.connect(self.FileBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_FileBtn)

        self.updownScroll.valueChanged.connect(self.updownScrollMoved)
        self.leftrightScroll.valueChanged.connect(self.leftrightScrollMoved)
        self.forbackScroll.valueChanged.connect(self.forbackScrollMoved)
        self.alphaVScroll.valueChanged.connect(self.alphaVScrollMoved)
        self.useVJoyStickBtn.toggled.connect(self.cb_VJoyStick)
        # self.thread = QtCore.QThread()
        self.thread = MyThread(Form)
        self.thread.trigger.connect(self.update_status_text)
        self.internet_thread = MyThread(Form)
        self.internet_thread.trigger.connect(self.update_internet_status)
        self.latlngThread = MyThread(Form)
        self.latlngThread.trigger.connect(self.update_LatLng)
        self.imageView_1.setAlignment(QtCore.Qt.AlignCenter)
        self.img1_thread = ImgThread(Form)
        self.img1_thread.trigger.connect(self.update_image_1)
        # self.imageView_2.setAlignment(QtCore.Qt.AlignCenter)
        # self.img2_thread = ImgThread(Form)
        # self.img2_thread.trigger.connect(self.update_image_2)

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.init()

    def init(self):
        self.updownScroll.setMaximum(200)
        self.updownScroll.setValue(100)
        self.updownValue.setText("Value: " + str(0))
        self.leftrightScroll.setMaximum(200)
        self.leftrightScroll.setValue(100)
        self.leftrightValue.setText("Value: " + str(0))
        self.alphaVValue.setText("Alpha: " + str(1))
        self.forbackScroll.setMaximum(200)
        self.forbackScroll.setValue(100)
        self.forbackValue.setText("Value: " + str(0))
        self.useVJoyStickBtn.setChecked(False)
        self.alphaVScroll.setMaximum(200)
        self.alphaVScroll.setValue(100)
        self.check_VJoystick()
        self.cb_imgBtn()
        self.SavePathBtn.setEnabled(False)
        # self.sub_image = rospy.Subscriber("/usb_cam/image_raw/compressed",CompressedImage , self.cbImage, queue_size=1)
        self.sub_gps = rospy.Subscriber("/mavros/global_position/raw/fix", NavSatFix , self.cbGPS, queue_size=1)
        self.sub_status = rospy.Subscriber("/ASV/status",Status , self.cbStatus, queue_size=1)
        self.sub_nav_status = rospy.Subscriber("/ASV/pure_pursuit/status",Int32 , self.cbNavStatus, queue_size=1)
        self.sub_battery = rospy.Subscriber("/mavros/battery", BatteryState, self.cbBattery, queue_size=1)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.navigateBtn.setText(_translate("Form", "Start Navigate 開始導航", None))
        self.manualBtn.setText(_translate("Form", "Manual 手動", None))
        self.autoBtn.setText(_translate("Form", "Autonomous 自動", None))
        self.estopBtn.setText(_translate("Form", "Emergency Stop 緊急停止", None))
        self.updownName.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">up/down</p></body></html>", None))
        self.forbackName.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">forward/backward</p></body></html>", None))
        self.leftrightName.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">left/right</p></body></html>", None))
        self.statusOutput.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Status</p></body></html>", None))
        self.updownValue.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">value: </p></body></html>", None))
        self.leftrightValue.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">value: </p></body></html>", None))
        self.alphaVValue.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">value: </p></body></html>", None))
        self.forbackValue.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">value: </p></body></html>", None))
        self.useVJoyStickBtn.setText(_translate("Form", "Use Virtual Joystick 使用虛擬遙控器", None))
        self.estopReleaseBtn.setText(_translate("Form", "E-Stop Release 解除緊急停止", None))
        self.resetNavigateBtn.setText(_translate("Form", "Reset Navigate 重設導航", None))
        self.ImgTopicBtn.setText(_translate("Form", "OK 確定", None))
        self.RecordPathBtn.setText(_translate("Form", "開始", None))
        self.SavePathBtn.setText(_translate("Form", "存檔", None))
        self.path_text.setText(_translate("Form", "Path 路徑", None))
        self.status_text.setText(_translate("Form", "Status 狀態", None))
        self.status_internet.setText(_translate("Form", "Connected 連線", None))
        self.LatLngOutput.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.path_text_2.setText(_translate("Form", "Image topic:", None))
        self.record_path_text.setText(_translate("Form", "Saved file:", None))
        self.path_text_3.setText(_translate("Form", "Lat, Lng", None))
        self.LatLngBtn.setText(_translate("Form", "Get Lat, Lng 取得經緯度", None))
        self.FileBtn.setText(_translate("Form", "File", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()

    rospy.init_node("auv_gui",anonymous=False)

    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

