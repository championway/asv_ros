
(cl:in-package :asdf)

(defsystem "asv_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SetValue" :depends-on ("_package_SetValue"))
    (:file "_package_SetValue" :depends-on ("_package"))
  ))