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
from std_srvs.srv import SetBool, SetBoolResponse, SetBoolRequest

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
        #time.sleep(random.random() * 5)
        self.trigger.emit(message)

class Ui_Form(object):

    def __init__(self):
        self.leftrightCmd = 0
        self.updownCmd = 0
        self.forbackCmd = 0
        self.dead_zone = 10
        self.useVJoyStick = True
        self.estop = False
        self.manual = True
        self.navigate = False
        self.cmd_publiser = rospy.Publisher("/ASV/cmd_control", ControlCmd, queue_size = 1)
        self.timer = rospy.Timer(rospy.Duration(0.1),self.cb_publish)

    def cb_publish(self, event):
        cmd = ControlCmd()
        cmd.useVJoystick = self.useVJoyStick
        cmd.forward = float(self.forbackCmd)
        cmd.right = float(self.leftrightCmd)
        cmd.up = float(self.updownCmd)
        cmd.estop = self.estop
        cmd.manual = self.manual
        cmd.navigate = self.navigate
        self.cmd_publiser.publish(cmd)

    def cbStatus(self, msg):
        if self.manual != msg.manual:
            self.manual = msg.manual
        if self.estop != msg.estop:
            self.estop = msg.estop
        if self.navigate != msg.navigate:
            self.navigate = msg.navigate
        text = ""
        text = "[Left Motor]  " + str(msg.left) + "\n"
        text += "[Right Motor]  " + str(msg.right) + "\n"
        text += "[Horizontal Motor]  " + str(msg.horizontal) + "\n"
        if msg.estop:
            text += "[Emergency Stop]  \tTrue\n"
        else:
            text += "[Emergency Stop]  \tFalse\n"
        if msg.manual:
            text += "[Manual]  \t\tTrue\n"
        else:
            text += "[Manual]  \t\tFalse\n"
        if msg.navigate:
            text += "[Navigation]  \tTrue\n"
        else:
            text += "[Navigation]  \tFalse\n"

        # self.update_status_text(text)
        self.thread.run_(text)

    def update_status_text(self, msg):
        # self.statusOutput.clear()
        self.statusOutput.setText(msg)


    def cb_VJoyStick(self):
        if self.useVJoyStickBtn.isChecked():
            self.useVJoyStick = True
            self.updownScroll.setEnabled(True)
            self.leftrightScroll.setEnabled(True)
            self.forbackScroll.setEnabled(True)
            self.updownValue.setEnabled(True)
            self.leftrightValue.setEnabled(True)
            self.forbackValue.setEnabled(True)
        else:
            self.useVJoyStick = False
            self.updownScroll.setEnabled(False)
            self.leftrightScroll.setEnabled(False)
            self.forbackScroll.setEnabled(False)
            self.updownValue.setEnabled(False)
            self.leftrightValue.setEnabled(False)
            self.forbackValue.setEnabled(False)

        
    def cb_navigate(self):
        self.navigate = True

    def cb_manual(self):
        self.manual = True

    def cb_auto(self):
        self.manual = False

    def cb_estop(self):
        self.estop = True

    def cb_estop_release(self):
        self.estop = False

    def updownScrollMoved(self):
        self.updownCmd = -(self.updownScroll.value()-100)
        if (abs(self.updownCmd) < self.dead_zone):
            self.updownCmd = 0
        self.updownValue.setText("Value: " + str(self.updownCmd))

    def leftrightScrollMoved(self):
        self.leftrightCmd = self.leftrightScroll.value()-100
        if (abs(self.leftrightCmd) < self.dead_zone):
            self.leftrightCmd = 0
        self.leftrightValue.setText("Value: " + str(self.leftrightCmd))

    def forbackScrollMoved(self):
        self.forbackCmd = self.forbackScroll.value()-100
        if (abs(self.forbackCmd) < self.dead_zone):
            self.forbackCmd = 0
        self.forbackValue.setText("Value: " + str(self.forbackCmd))

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(976, 553)
        self.navigatieBtn = QtGui.QPushButton(Form)
        self.navigatieBtn.setGeometry(QtCore.QRect(640, 10, 181, 51))
        self.navigatieBtn.setObjectName(_fromUtf8("navigatieBtn"))
        self.manualBtn = QtGui.QPushButton(Form)
        self.manualBtn.setGeometry(QtCore.QRect(590, 70, 141, 51))
        self.manualBtn.setObjectName(_fromUtf8("manualBtn"))
        self.autoBtn = QtGui.QPushButton(Form)
        self.autoBtn.setGeometry(QtCore.QRect(740, 70, 141, 51))
        self.autoBtn.setObjectName(_fromUtf8("autoBtn"))
        self.estopBtn = QtGui.QPushButton(Form)
        self.estopBtn.setGeometry(QtCore.QRect(520, 130, 211, 61))
        self.estopBtn.setObjectName(_fromUtf8("estopBtn"))
        self.imageView = QtGui.QGraphicsView(Form)
        self.imageView.setGeometry(QtCore.QRect(10, 10, 501, 361))
        self.imageView.setObjectName(_fromUtf8("imageView"))
        self.statusInput = QtGui.QTextEdit(Form)
        self.statusInput.setGeometry(QtCore.QRect(10, 390, 211, 151))
        self.statusInput.setObjectName(_fromUtf8("statusInput"))
        self.leftrightScroll = QtGui.QScrollBar(Form)
        self.leftrightScroll.setGeometry(QtCore.QRect(630, 400, 191, 16))
        self.leftrightScroll.setOrientation(QtCore.Qt.Horizontal)
        self.leftrightScroll.setObjectName(_fromUtf8("leftrightScroll"))
        self.updownName = QtGui.QTextBrowser(Form)
        self.updownName.setGeometry(QtCore.QRect(530, 260, 101, 31))
        self.updownName.setObjectName(_fromUtf8("updownName"))
        self.forbackName = QtGui.QTextBrowser(Form)
        self.forbackName.setGeometry(QtCore.QRect(810, 260, 151, 31))
        self.forbackName.setObjectName(_fromUtf8("forbackName"))
        self.leftrightName = QtGui.QTextBrowser(Form)
        self.leftrightName.setGeometry(QtCore.QRect(670, 260, 101, 31))
        self.leftrightName.setObjectName(_fromUtf8("leftrightName"))
        self.updownScroll = QtGui.QScrollBar(Form)
        self.updownScroll.setGeometry(QtCore.QRect(570, 300, 16, 201))
        self.updownScroll.setOrientation(QtCore.Qt.Vertical)
        self.updownScroll.setObjectName(_fromUtf8("updownScroll"))
        self.statusOutput = QtGui.QTextBrowser(Form)
        self.statusOutput.setGeometry(QtCore.QRect(240, 390, 271, 151))
        self.statusOutput.setObjectName(_fromUtf8("statusOutput"))
        self.updownValue = QtGui.QTextBrowser(Form)
        self.updownValue.setGeometry(QtCore.QRect(530, 510, 101, 31))
        self.updownValue.setObjectName(_fromUtf8("updownValue"))
        self.forbackScroll = QtGui.QScrollBar(Form)
        self.forbackScroll.setGeometry(QtCore.QRect(870, 300, 16, 201))
        self.forbackScroll.setOrientation(QtCore.Qt.Vertical)
        self.forbackScroll.setObjectName(_fromUtf8("forbackScroll"))
        self.leftrightValue = QtGui.QTextBrowser(Form)
        self.leftrightValue.setGeometry(QtCore.QRect(680, 510, 101, 31))
        self.leftrightValue.setObjectName(_fromUtf8("leftrightValue"))
        self.forbackValue = QtGui.QTextBrowser(Form)
        self.forbackValue.setGeometry(QtCore.QRect(820, 510, 101, 31))
        self.forbackValue.setObjectName(_fromUtf8("forbackValue"))
        self.useVJoyStickBtn = QtGui.QRadioButton(Form)
        self.useVJoyStickBtn.setGeometry(QtCore.QRect(610, 210, 271, 22))
        self.useVJoyStickBtn.setObjectName(_fromUtf8("useVJoyStickBtn"))
        self.estopReleaseBtn = QtGui.QPushButton(Form)
        self.estopReleaseBtn.setGeometry(QtCore.QRect(740, 130, 221, 61))
        self.estopReleaseBtn.setObjectName(_fromUtf8("estopReleaseBtn"))

        self.retranslateUi(Form)
        
        QtCore.QObject.connect(self.navigatieBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_navigate)
        QtCore.QObject.connect(self.manualBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_manual)
        QtCore.QObject.connect(self.autoBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_auto)
        QtCore.QObject.connect(self.estopBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_estop)
        QtCore.QObject.connect(self.estopReleaseBtn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cb_estop_release)

        self.updownScroll.valueChanged.connect(self.updownScrollMoved)
        self.leftrightScroll.valueChanged.connect(self.leftrightScrollMoved)
        self.forbackScroll.valueChanged.connect(self.forbackScrollMoved)
        self.useVJoyStickBtn.toggled.connect(self.cb_VJoyStick)
        # self.thread = QtCore.QThread()
        self.thread = MyThread(Form)
        self.thread.trigger.connect(self.update_status_text)

        
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.init()

    def init(self):
        self.updownScroll.setMaximum(200)
        self.updownScroll.setValue(100)
        self.updownValue.setText("Value: " + str(0))
        self.leftrightScroll.setMaximum(200)
        self.leftrightScroll.setValue(100)
        self.leftrightValue.setText("Value: " + str(0))
        self.forbackScroll.setMaximum(200)
        self.forbackScroll.setValue(100)
        self.forbackValue.setText("Value: " + str(0))
        self.useVJoyStickBtn.setChecked(True)
        self.sub_status = rospy.Subscriber("/ASV/status",Status, self.cbStatus, queue_size=1)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.navigatieBtn.setText(_translate("Form", "Start Navigate 開始導航", None))
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
        self.forbackValue.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">value: </p></body></html>", None))
        self.useVJoyStickBtn.setText(_translate("Form", "Use Virtual Joystick 使用虛擬遙控器", None))
        self.estopReleaseBtn.setText(_translate("Form", "E-Stop Releasesh 解除緊急停止", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()

    rospy.init_node("auv_gui",anonymous=False)

    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

