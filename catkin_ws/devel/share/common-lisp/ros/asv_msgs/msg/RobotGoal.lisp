; Auto-generated. Do not edit!


(cl:in-package asv_msgs-msg)


;//! \htmlinclude RobotGoal.msg.html

(cl:defclass <RobotGoal> (roslisp-msg-protocol:ros-message)
  ((goal
    :reader goal
    :initarg :goal
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (robot
    :reader robot
    :initarg :robot
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass RobotGoal (<RobotGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RobotGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RobotGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asv_msgs-msg:<RobotGoal> is deprecated: use asv_msgs-msg:RobotGoal instead.")))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <RobotGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asv_msgs-msg:goal-val is deprecated.  Use asv_msgs-msg:goal instead.")
  (goal m))

(cl:ensure-generic-function 'robot-val :lambda-list '(m))
(cl:defmethod robot-val ((m <RobotGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asv_msgs-msg:robot-val is deprecated.  Use asv_msgs-msg:robot instead.")
  (robot m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RobotGoal>) ostream)
  "Serializes a message object of type '<RobotGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'robot) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RobotGoal>) istream)
  "Deserializes a message object of type '<RobotGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'robot) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RobotGoal>)))
  "Returns string type for a message object of type '<RobotGoal>"
  "asv_msgs/RobotGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RobotGoal)))
  "Returns string type for a message object of type 'RobotGoal"
  "asv_msgs/RobotGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RobotGoal>)))
  "Returns md5sum for a message object of type '<RobotGoal>"
  "98c7ffdb4ffaa1a7d09b7aef3442e3f1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RobotGoal)))
  "Returns md5sum for a message object of type 'RobotGoal"
  "98c7ffdb4ffaa1a7d09b7aef3442e3f1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RobotGoal>)))
  "Returns full string definition for message of type '<RobotGoal>"
  (cl:format cl:nil "geometry_msgs/Pose goal~%geometry_msgs/Pose robot~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RobotGoal)))
  "Returns full string definition for message of type 'RobotGoal"
  (cl:format cl:nil "geometry_msgs/Pose goal~%geometry_msgs/Pose robot~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RobotGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'robot))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RobotGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'RobotGoal
    (cl:cons ':goal (goal msg))
    (cl:cons ':robot (robot msg))
))
