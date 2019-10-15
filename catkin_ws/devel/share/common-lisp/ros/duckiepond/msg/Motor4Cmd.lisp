; Auto-generated. Do not edit!


(cl:in-package duckiepond-msg)


;//! \htmlinclude Motor4Cmd.msg.html

(cl:defclass <Motor4Cmd> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (lf
    :reader lf
    :initarg :lf
    :type cl:float
    :initform 0.0)
   (rf
    :reader rf
    :initarg :rf
    :type cl:float
    :initform 0.0)
   (lr
    :reader lr
    :initarg :lr
    :type cl:float
    :initform 0.0)
   (rr
    :reader rr
    :initarg :rr
    :type cl:float
    :initform 0.0))
)

(cl:defclass Motor4Cmd (<Motor4Cmd>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Motor4Cmd>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Motor4Cmd)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name duckiepond-msg:<Motor4Cmd> is deprecated: use duckiepond-msg:Motor4Cmd instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Motor4Cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:header-val is deprecated.  Use duckiepond-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'lf-val :lambda-list '(m))
(cl:defmethod lf-val ((m <Motor4Cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:lf-val is deprecated.  Use duckiepond-msg:lf instead.")
  (lf m))

(cl:ensure-generic-function 'rf-val :lambda-list '(m))
(cl:defmethod rf-val ((m <Motor4Cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:rf-val is deprecated.  Use duckiepond-msg:rf instead.")
  (rf m))

(cl:ensure-generic-function 'lr-val :lambda-list '(m))
(cl:defmethod lr-val ((m <Motor4Cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:lr-val is deprecated.  Use duckiepond-msg:lr instead.")
  (lr m))

(cl:ensure-generic-function 'rr-val :lambda-list '(m))
(cl:defmethod rr-val ((m <Motor4Cmd>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:rr-val is deprecated.  Use duckiepond-msg:rr instead.")
  (rr m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Motor4Cmd>) ostream)
  "Serializes a message object of type '<Motor4Cmd>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'lf))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rf))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'lr))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rr))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Motor4Cmd>) istream)
  "Deserializes a message object of type '<Motor4Cmd>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lf) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rf) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'lr) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rr) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Motor4Cmd>)))
  "Returns string type for a message object of type '<Motor4Cmd>"
  "duckiepond/Motor4Cmd")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Motor4Cmd)))
  "Returns string type for a message object of type 'Motor4Cmd"
  "duckiepond/Motor4Cmd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Motor4Cmd>)))
  "Returns md5sum for a message object of type '<Motor4Cmd>"
  "77d80b96b13055bc97b62acface81cb7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Motor4Cmd)))
  "Returns md5sum for a message object of type 'Motor4Cmd"
  "77d80b96b13055bc97b62acface81cb7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Motor4Cmd>)))
  "Returns full string definition for message of type '<Motor4Cmd>"
  (cl:format cl:nil "# Thrust command - typically ranges from {-1.0 - 1.0}~%Header header~%float32 lf~%float32 rf~%float32 lr~%float32 rr~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Motor4Cmd)))
  "Returns full string definition for message of type 'Motor4Cmd"
  (cl:format cl:nil "# Thrust command - typically ranges from {-1.0 - 1.0}~%Header header~%float32 lf~%float32 rf~%float32 lr~%float32 rr~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Motor4Cmd>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Motor4Cmd>))
  "Converts a ROS message object to a list"
  (cl:list 'Motor4Cmd
    (cl:cons ':header (header msg))
    (cl:cons ':lf (lf msg))
    (cl:cons ':rf (rf msg))
    (cl:cons ':lr (lr msg))
    (cl:cons ':rr (rr msg))
))
