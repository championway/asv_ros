; Auto-generated. Do not edit!


(cl:in-package asv_msgs-srv)


;//! \htmlinclude SetRobotPath-request.msg.html

(cl:defclass <SetRobotPath-request> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type asv_msgs-msg:RobotPath
    :initform (cl:make-instance 'asv_msgs-msg:RobotPath)))
)

(cl:defclass SetRobotPath-request (<SetRobotPath-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetRobotPath-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetRobotPath-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asv_msgs-srv:<SetRobotPath-request> is deprecated: use asv_msgs-srv:SetRobotPath-request instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <SetRobotPath-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asv_msgs-srv:data-val is deprecated.  Use asv_msgs-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetRobotPath-request>) ostream)
  "Serializes a message object of type '<SetRobotPath-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'data) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetRobotPath-request>) istream)
  "Deserializes a message object of type '<SetRobotPath-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'data) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetRobotPath-request>)))
  "Returns string type for a service object of type '<SetRobotPath-request>"
  "asv_msgs/SetRobotPathRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetRobotPath-request)))
  "Returns string type for a service object of type 'SetRobotPath-request"
  "asv_msgs/SetRobotPathRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetRobotPath-request>)))
  "Returns md5sum for a message object of type '<SetRobotPath-request>"
  "c7fd2b40589889fc45f9427101ed3a2a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetRobotPath-request)))
  "Returns md5sum for a message object of type 'SetRobotPath-request"
  "c7fd2b40589889fc45f9427101ed3a2a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetRobotPath-request>)))
  "Returns full string definition for message of type '<SetRobotPath-request>"
  (cl:format cl:nil "asv_msgs/RobotPath data~%~%================================================================================~%MSG: asv_msgs/RobotPath~%geometry_msgs/Pose[] list~%geometry_msgs/Pose robot~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetRobotPath-request)))
  "Returns full string definition for message of type 'SetRobotPath-request"
  (cl:format cl:nil "asv_msgs/RobotPath data~%~%================================================================================~%MSG: asv_msgs/RobotPath~%geometry_msgs/Pose[] list~%geometry_msgs/Pose robot~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetRobotPath-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetRobotPath-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetRobotPath-request
    (cl:cons ':data (data msg))
))
;//! \htmlinclude SetRobotPath-response.msg.html

(cl:defclass <SetRobotPath-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SetRobotPath-response (<SetRobotPath-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetRobotPath-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetRobotPath-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name asv_msgs-srv:<SetRobotPath-response> is deprecated: use asv_msgs-srv:SetRobotPath-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetRobotPath-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader asv_msgs-srv:success-val is deprecated.  Use asv_msgs-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetRobotPath-response>) ostream)
  "Serializes a message object of type '<SetRobotPath-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetRobotPath-response>) istream)
  "Deserializes a message object of type '<SetRobotPath-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetRobotPath-response>)))
  "Returns string type for a service object of type '<SetRobotPath-response>"
  "asv_msgs/SetRobotPathResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetRobotPath-response)))
  "Returns string type for a service object of type 'SetRobotPath-response"
  "asv_msgs/SetRobotPathResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetRobotPath-response>)))
  "Returns md5sum for a message object of type '<SetRobotPath-response>"
  "c7fd2b40589889fc45f9427101ed3a2a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetRobotPath-response)))
  "Returns md5sum for a message object of type 'SetRobotPath-response"
  "c7fd2b40589889fc45f9427101ed3a2a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetRobotPath-response>)))
  "Returns full string definition for message of type '<SetRobotPath-response>"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetRobotPath-response)))
  "Returns full string definition for message of type 'SetRobotPath-response"
  (cl:format cl:nil "bool success~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetRobotPath-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetRobotPath-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetRobotPath-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetRobotPath)))
  'SetRobotPath-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetRobotPath)))
  'SetRobotPath-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetRobotPath)))
  "Returns string type for a service object of type '<SetRobotPath>"
  "asv_msgs/SetRobotPath")