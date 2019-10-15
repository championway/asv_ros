; Auto-generated. Do not edit!


(cl:in-package duckiepond-msg)


;//! \htmlinclude VelocityVector.msg.html

(cl:defclass <VelocityVector> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (angular
    :reader angular
    :initarg :angular
    :type cl:float
    :initform 0.0))
)

(cl:defclass VelocityVector (<VelocityVector>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <VelocityVector>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'VelocityVector)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name duckiepond-msg:<VelocityVector> is deprecated: use duckiepond-msg:VelocityVector instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <VelocityVector>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:x-val is deprecated.  Use duckiepond-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <VelocityVector>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:y-val is deprecated.  Use duckiepond-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'angular-val :lambda-list '(m))
(cl:defmethod angular-val ((m <VelocityVector>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:angular-val is deprecated.  Use duckiepond-msg:angular instead.")
  (angular m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <VelocityVector>) ostream)
  "Serializes a message object of type '<VelocityVector>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angular))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <VelocityVector>) istream)
  "Deserializes a message object of type '<VelocityVector>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angular) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<VelocityVector>)))
  "Returns string type for a message object of type '<VelocityVector>"
  "duckiepond/VelocityVector")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'VelocityVector)))
  "Returns string type for a message object of type 'VelocityVector"
  "duckiepond/VelocityVector")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<VelocityVector>)))
  "Returns md5sum for a message object of type '<VelocityVector>"
  "1b6108f70c66951a6da12942857785cf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'VelocityVector)))
  "Returns md5sum for a message object of type 'VelocityVector"
  "1b6108f70c66951a6da12942857785cf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<VelocityVector>)))
  "Returns full string definition for message of type '<VelocityVector>"
  (cl:format cl:nil "#velocity command {1,-1}~%float32 x~%float32 y~%float32 angular~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'VelocityVector)))
  "Returns full string definition for message of type 'VelocityVector"
  (cl:format cl:nil "#velocity command {1,-1}~%float32 x~%float32 y~%float32 angular~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <VelocityVector>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <VelocityVector>))
  "Converts a ROS message object to a list"
  (cl:list 'VelocityVector
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':angular (angular msg))
))
