;; Auto-generated. Do not edit!


(when (boundp 'asv_msgs::SetRobotPath)
  (if (not (find-package "ASV_MSGS"))
    (make-package "ASV_MSGS"))
  (shadow 'SetRobotPath (find-package "ASV_MSGS")))
(unless (find-package "ASV_MSGS::SETROBOTPATH")
  (make-package "ASV_MSGS::SETROBOTPATH"))
(unless (find-package "ASV_MSGS::SETROBOTPATHREQUEST")
  (make-package "ASV_MSGS::SETROBOTPATHREQUEST"))
(unless (find-package "ASV_MSGS::SETROBOTPATHRESPONSE")
  (make-package "ASV_MSGS::SETROBOTPATHRESPONSE"))

(in-package "ROS")





(defclass asv_msgs::SetRobotPathRequest
  :super ros::object
  :slots (_data ))

(defmethod asv_msgs::SetRobotPathRequest
  (:init
   (&key
    ((:data __data) (instance asv_msgs::RobotPath :init))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&rest __data)
   (if (keywordp (car __data))
       (send* _data __data)
     (progn
       (if __data (setq _data (car __data)))
       _data)))
  (:serialization-length
   ()
   (+
    ;; asv_msgs/RobotPath _data
    (send _data :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; asv_msgs/RobotPath _data
       (send _data :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; asv_msgs/RobotPath _data
     (send _data :deserialize buf ptr-) (incf ptr- (send _data :serialization-length))
   ;;
   self)
  )

(defclass asv_msgs::SetRobotPathResponse
  :super ros::object
  :slots (_success ))

(defmethod asv_msgs::SetRobotPathResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional __success)
   (if __success (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass asv_msgs::SetRobotPath
  :super ros::object
  :slots ())

(setf (get asv_msgs::SetRobotPath :md5sum-) "c7fd2b40589889fc45f9427101ed3a2a")
(setf (get asv_msgs::SetRobotPath :datatype-) "asv_msgs/SetRobotPath")
(setf (get asv_msgs::SetRobotPath :request) asv_msgs::SetRobotPathRequest)
(setf (get asv_msgs::SetRobotPath :response) asv_msgs::SetRobotPathResponse)

(defmethod asv_msgs::SetRobotPathRequest
  (:response () (instance asv_msgs::SetRobotPathResponse :init)))

(setf (get asv_msgs::SetRobotPathRequest :md5sum-) "c7fd2b40589889fc45f9427101ed3a2a")
(setf (get asv_msgs::SetRobotPathRequest :datatype-) "asv_msgs/SetRobotPathRequest")
(setf (get asv_msgs::SetRobotPathRequest :definition-)
      "asv_msgs/RobotPath data

================================================================================
MSG: asv_msgs/RobotPath
geometry_msgs/Pose[] list
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
---
bool success
")

(setf (get asv_msgs::SetRobotPathResponse :md5sum-) "c7fd2b40589889fc45f9427101ed3a2a")
(setf (get asv_msgs::SetRobotPathResponse :datatype-) "asv_msgs/SetRobotPathResponse")
(setf (get asv_msgs::SetRobotPathResponse :definition-)
      "asv_msgs/RobotPath data

================================================================================
MSG: asv_msgs/RobotPath
geometry_msgs/Pose[] list
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
---
bool success
")



(provide :asv_msgs/SetRobotPath "c7fd2b40589889fc45f9427101ed3a2a")


