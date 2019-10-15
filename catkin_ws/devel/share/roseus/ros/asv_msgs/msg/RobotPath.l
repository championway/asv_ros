;; Auto-generated. Do not edit!


(when (boundp 'asv_msgs::RobotPath)
  (if (not (find-package "ASV_MSGS"))
    (make-package "ASV_MSGS"))
  (shadow 'RobotPath (find-package "ASV_MSGS")))
(unless (find-package "ASV_MSGS::ROBOTPATH")
  (make-package "ASV_MSGS::ROBOTPATH"))

(in-package "ROS")
;;//! \htmlinclude RobotPath.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass asv_msgs::RobotPath
  :super ros::object
  :slots (_list _robot ))

(defmethod asv_msgs::RobotPath
  (:init
   (&key
    ((:list __list) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Pose :init) r)) r))
    ((:robot __robot) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _list __list)
   (setq _robot __robot)
   self)
  (:list
   (&rest __list)
   (if (keywordp (car __list))
       (send* _list __list)
     (progn
       (if __list (setq _list (car __list)))
       _list)))
  (:robot
   (&rest __robot)
   (if (keywordp (car __robot))
       (send* _robot __robot)
     (progn
       (if __robot (setq _robot (car __robot)))
       _robot)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose[] _list
    (apply #'+ (send-all _list :serialization-length)) 4
    ;; geometry_msgs/Pose _robot
    (send _robot :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose[] _list
     (write-long (length _list) s)
     (dolist (elem _list)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Pose _robot
       (send _robot :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose[] _list
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _list (let (r) (dotimes (i n) (push (instance geometry_msgs::Pose :init) r)) r))
     (dolist (elem- _list)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Pose _robot
     (send _robot :deserialize buf ptr-) (incf ptr- (send _robot :serialization-length))
   ;;
   self)
  )

(setf (get asv_msgs::RobotPath :md5sum-) "26644de2debc53d8bba799cb1ae600b6")
(setf (get asv_msgs::RobotPath :datatype-) "asv_msgs/RobotPath")
(setf (get asv_msgs::RobotPath :definition-)
      "geometry_msgs/Pose[] list
geometry_msgs/Pose robot
================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :asv_msgs/RobotPath "26644de2debc53d8bba799cb1ae600b6")


