; Auto-generated. Do not edit!


(cl:in-package duckiepond-msg)


;//! \htmlinclude Boxlist.msg.html

(cl:defclass <Boxlist> (roslisp-msg-protocol:ros-message)
  ((list
    :reader list
    :initarg :list
    :type (cl:vector duckiepond-msg:Box)
   :initform (cl:make-array 0 :element-type 'duckiepond-msg:Box :initial-element (cl:make-instance 'duckiepond-msg:Box)))
   (image_width
    :reader image_width
    :initarg :image_width
    :type cl:integer
    :initform 0)
   (image_height
    :reader image_height
    :initarg :image_height
    :type cl:integer
    :initform 0)
   (image
    :reader image
    :initarg :image
    :type sensor_msgs-msg:CompressedImage
    :initform (cl:make-instance 'sensor_msgs-msg:CompressedImage)))
)

(cl:defclass Boxlist (<Boxlist>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Boxlist>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Boxlist)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name duckiepond-msg:<Boxlist> is deprecated: use duckiepond-msg:Boxlist instead.")))

(cl:ensure-generic-function 'list-val :lambda-list '(m))
(cl:defmethod list-val ((m <Boxlist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:list-val is deprecated.  Use duckiepond-msg:list instead.")
  (list m))

(cl:ensure-generic-function 'image_width-val :lambda-list '(m))
(cl:defmethod image_width-val ((m <Boxlist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:image_width-val is deprecated.  Use duckiepond-msg:image_width instead.")
  (image_width m))

(cl:ensure-generic-function 'image_height-val :lambda-list '(m))
(cl:defmethod image_height-val ((m <Boxlist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:image_height-val is deprecated.  Use duckiepond-msg:image_height instead.")
  (image_height m))

(cl:ensure-generic-function 'image-val :lambda-list '(m))
(cl:defmethod image-val ((m <Boxlist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader duckiepond-msg:image-val is deprecated.  Use duckiepond-msg:image instead.")
  (image m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Boxlist>) ostream)
  "Serializes a message object of type '<Boxlist>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'list))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'list))
  (cl:let* ((signed (cl:slot-value msg 'image_width)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'image_height)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Boxlist>) istream)
  "Deserializes a message object of type '<Boxlist>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'list) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'list)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'duckiepond-msg:Box))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'image_width) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'image_height) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Boxlist>)))
  "Returns string type for a message object of type '<Boxlist>"
  "duckiepond/Boxlist")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Boxlist)))
  "Returns string type for a message object of type 'Boxlist"
  "duckiepond/Boxlist")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Boxlist>)))
  "Returns md5sum for a message object of type '<Boxlist>"
  "64ed701dbabc3b78cf16142116cf4f2f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Boxlist)))
  "Returns md5sum for a message object of type 'Boxlist"
  "64ed701dbabc3b78cf16142116cf4f2f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Boxlist>)))
  "Returns full string definition for message of type '<Boxlist>"
  (cl:format cl:nil "Box[] list~%int32 image_width~%int32 image_height~%sensor_msgs/CompressedImage image~%================================================================================~%MSG: duckiepond/Box~%int32 x~%int32 y~%int32 w~%int32 h~%float32 confidence~%int32 id~%================================================================================~%MSG: sensor_msgs/CompressedImage~%# This message contains a compressed image~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%~%string format        # Specifies the format of the data~%                     #   Acceptable values:~%                     #     jpeg, png~%uint8[] data         # Compressed image buffer~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Boxlist)))
  "Returns full string definition for message of type 'Boxlist"
  (cl:format cl:nil "Box[] list~%int32 image_width~%int32 image_height~%sensor_msgs/CompressedImage image~%================================================================================~%MSG: duckiepond/Box~%int32 x~%int32 y~%int32 w~%int32 h~%float32 confidence~%int32 id~%================================================================================~%MSG: sensor_msgs/CompressedImage~%# This message contains a compressed image~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%~%string format        # Specifies the format of the data~%                     #   Acceptable values:~%                     #     jpeg, png~%uint8[] data         # Compressed image buffer~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Boxlist>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'list) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4
     4
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Boxlist>))
  "Converts a ROS message object to a list"
  (cl:list 'Boxlist
    (cl:cons ':list (list msg))
    (cl:cons ':image_width (image_width msg))
    (cl:cons ':image_height (image_height msg))
    (cl:cons ':image (image msg))
))
