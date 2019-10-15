; Auto-generated. Do not edit!


(cl:in-package duckiepond-msg)


;//! \htmlinclude Heading.msg.html

(cl:defclass <Heading> (roslisp-msg-protocol:ros-message)
  ((phi
    :reader phi
    :initarg :phi
    :type cl:float
    :initform 0.0)
   (speed
    :reader speed
    :initarg :speed
    :type cl:float
    :initform 0.0))
)

(cl:defclass Heading (<Heading>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Heading>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Heading)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name duckiepond-msg:<Heading> is deprecated: use duckiepond-msg:Heading instead.")))

(cl:ensure-generic-function 'phi-val :lambda-list '(m))
(cl:defmethod phi-val ((m <Heading>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:phi-val is deprecated.  Use duckiepond-msg:phi instead.")
  (phi m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <Heading>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:speed-val is deprecated.  Use duckiepond-msg:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Heading>) ostream)
  "Serializes a message object of type '<Heading>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'phi))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Heading>) istream)
  "Deserializes a message object of type '<Heading>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'phi) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'speed) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Heading>)))
  "Returns string type for a message object of type '<Heading>"
  "duckiepond/Heading")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Heading)))
  "Returns string type for a message object of type 'Heading"
  "duckiepond/Heading")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Heading>)))
  "Returns md5sum for a message object of type '<Heading>"
  "8fe8a91eef3de9ae7860b3f07a1529db")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Heading)))
  "Returns md5sum for a message object of type 'Heading"
  "8fe8a91eef3de9ae7860b3f07a1529db")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Heading>)))
  "Returns full string definition for message of type '<Heading>"
  (cl:format cl:nil "float32 phi~%float32 speed~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Heading)))
  "Returns full string definition for message of type 'Heading"
  (cl:format cl:nil "float32 phi~%float32 speed~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Heading>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Heading>))
  "Converts a ROS message object to a list"
  (cl:list 'Heading
    (cl:cons ':phi (phi msg))
    (cl:cons ':speed (speed msg))
))
