;; Auto-generated. Do not edit!


(when (boundp 'asv_msgs::RobotGoal)
  (if (not (find-package "ASV_MSGS"))
    (make-package "ASV_MSGS"))
  (shadow 'RobotGoal (find-package "ASV_MSGS")))
(unless (find-package "ASV_MSGS::ROBOTGOAL")
  (make-package "ASV_MSGS::ROBOTGOAL"))

(in-package "ROS")
;;//! \htmlinclude RobotGoal.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass asv_msgs::RobotGoal
  :super ros::object
  :slots (_goal _robot ))

(defmethod asv_msgs::RobotGoal
  (:init
   (&key
    ((:goal __goal) (instance geometry_msgs::Pose :init))
    ((:robot __robot) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _goal __goal)
   (setq _robot __robot)
   self)
  (:goal
   (&rest __goal)
   (if (keywordp (car __goal))
       (send* _goal __goal)
     (progn
       (if __goal (setq _goal (car __goal)))
       _goal)))
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
    ;; geometry_msgs/Pose _goal
    (send _goal :serialization-length)
    ;; geometry_msgs/Pose _robot
    (send _robot :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose _goal
       (send _goal :serialize s)
     ;; geometry_msgs/Pose _robot
       (send _robot :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose _goal
     (send _goal :deserialize buf ptr-) (incf ptr- (send _goal :serialization-length))
   ;; geometry_msgs/Pose _robot
     (send _robot :deserialize buf ptr-) (incf ptr- (send _robot :serialization-length))
   ;;
   self)
  )

(setf (get asv_msgs::RobotGoal :md5sum-) "98c7ffdb4ffaa1a7d09b7aef3442e3f1")
(setf (get asv_msgs::RobotGoal :datatype-) "asv_msgs/RobotGoal")
(setf (get asv_msgs::RobotGoal :definition-)
      "geometry_msgs/Pose goal
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



(provide :asv_msgs/RobotGoal "98c7ffdb4ffaa1a7d09b7aef3442e3f1")


