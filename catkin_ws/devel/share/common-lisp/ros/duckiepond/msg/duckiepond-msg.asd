
(cl:in-package :asdf)

(defsystem "duckiepond-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "BoolStamped" :depends-on ("_package_BoolStamped"))
    (:file "_package_BoolStamped" :depends-on ("_package"))
    (:file "Box" :depends-on ("_package_Box"))
    (:file "_package_Box" :depends-on ("_package"))
    (:file "Boxlist" :depends-on ("_package_Boxlist"))
    (:file "_package_Boxlist" :depends-on ("_package"))
    (:file "Heading" :depends-on ("_package_Heading"))
    (:file "_package_Heading" :depends-on ("_package"))
    (:file "Motor4Cmd" :depends-on ("_package_Motor4Cmd"))
    (:file "_package_Motor4Cmd" :depends-on ("_package"))
    (:file "MotorCmd" :depends-on ("_package_MotorCmd"))
    (:file "_package_MotorCmd" :depends-on ("_package"))
    (:file "UsvDrive" :depends-on ("_package_UsvDrive"))
    (:file "_package_UsvDrive" :depends-on ("_package"))
    (:file "VelocityVector" :depends-on ("_package_VelocityVector"))
    (:file "_package_VelocityVector" :depends-on ("_package"))
  ))