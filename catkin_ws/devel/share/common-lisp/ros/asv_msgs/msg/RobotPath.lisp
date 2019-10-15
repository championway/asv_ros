; Auto-generated. Do not edit!


(cl:in-package asv_msgs-msg)


;//! \htmlinclude RobotPath.msg.html

(cl:defclass <RobotPath> (roslisp-msg-protocol:ros-message)
  ((list
    :reader list
    :initarg :list
    :type (cl:vector geometry_msgs-msg:Pose)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Pose :initial-element (cl:make-instance 'geometry_msgs-msg:Pose)))
   (robot
    :reader robot
    :initarg :robot
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass RobotPath (<RobotPath>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RobotPath>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RobotPath)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asv_msgs-msg:<RobotPath> is deprecated: use asv_msgs-msg:RobotPath instead.")))

(cl:ensure-generic-function 'list-val :lambda-list '(m))
(cl:defmethod list-val ((m <RobotPath>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asv_msgs-msg:list-val is deprecated.  Use asv_msgs-msg:list instead.")
  (list m))

(cl:ensure-generic-function 'robot-val :lambda-list '(m))
(cl:defmethod robot-val ((m <RobotPath>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asv_msgs-msg:robot-val is deprecated.  Use asv_msgs-msg:robot instead.")
  (robot m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RobotPath>) ostream)
  "Serializes a message object of type '<RobotPath>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'list))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'list))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'robot) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RobotPath>) istream)
  "Deserializes a message object of type '<RobotPath>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'list) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'list)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Pose))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'robot) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RobotPath>)))
  "Returns string type for a message object of type '<RobotPath>"
  "asv_msgs/RobotPath")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RobotPath)))
  "Returns string type for a message object of type 'RobotPath"
  "asv_msgs/RobotPath")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RobotPath>)))
  "Returns md5sum for a message object of type '<RobotPath>"
  "26644de2debc53d8bba799cb1ae600b6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RobotPath)))
  "Returns md5sum for a message object of type 'RobotPath"
  "26644de2debc53d8bba799cb1ae600b6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RobotPath>)))
  "Returns full string definition for message of type '<RobotPath>"
  (cl:format cl:nil "geometry_msgs/Pose[] list~%geometry_msgs/Pose robot~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RobotPath)))
  "Returns full string definition for message of type 'RobotPath"
  (cl:format cl:nil "geometry_msgs/Pose[] list~%geometry_msgs/Pose robot~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RobotPath>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'list) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'robot))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RobotPath>))
  "Converts a ROS message object to a list"
  (cl:list 'RobotPath
    (cl:cons ':list (list msg))
    (cl:cons ':robot (robot msg))
))
