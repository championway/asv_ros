
(cl:in-package :asdf)

(defsystem "asv_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :asv_msgs-msg
)
  :components ((:file "_package")
    (:file "SetRobotPath" :depends-on ("_package_SetRobotPath"))
    (:file "_package_SetRobotPath" :depends-on ("_package"))
    (:file "SetValue" :depends-on ("_package_SetValue"))
    (:file "_package_SetValue" :depends-on ("_package"))
  ))