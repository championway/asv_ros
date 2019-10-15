;; Auto-generated. Do not edit!


(when (boundp 'duckiepond::Boxlist)
  (if (not (find-package "DUCKIEPOND"))
    (make-package "DUCKIEPOND"))
  (shadow 'Boxlist (find-package "DUCKIEPOND")))
(unless (find-package "DUCKIEPOND::BOXLIST")
  (make-package "DUCKIEPOND::BOXLIST"))

(in-package "ROS")
;;//! \htmlinclude Boxlist.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass duckiepond::Boxlist
  :super ros::object
  :slots (_list _image_width _image_height _image ))

(defmethod duckiepond::Boxlist
  (:init
   (&key
    ((:list __list) (let (r) (dotimes (i 0) (push (instance duckiepond::Box :init) r)) r))
    ((:image_width __image_width) 0)
    ((:image_height __image_height) 0)
    ((:image __image) (instance sensor_msgs::CompressedImage :init))
    )
   (send-super :init)
   (setq _list __list)
   (setq _image_width (round __image_width))
   (setq _image_height (round __image_height))
   (setq _image __image)
   self)
  (:list
   (&rest __list)
   (if (keywordp (car __list))
       (send* _list __list)
     (progn
       (if __list (setq _list (car __list)))
       _list)))
  (:image_width
   (&optional __image_width)
   (if __image_width (setq _image_width __image_width)) _image_width)
  (:image_height
   (&optional __image_height)
   (if __image_height (setq _image_height __image_height)) _image_height)
  (:image
   (&rest __image)
   (if (keywordp (car __image))
       (send* _image __image)
     (progn
       (if __image (setq _image (car __image)))
       _image)))
  (:serialization-length
   ()
   (+
    ;; duckiepond/Box[] _list
    (apply #'+ (send-all _list :serialization-length)) 4
    ;; int32 _image_width
    4
    ;; int32 _image_height
    4
    ;; sensor_msgs/CompressedImage _image
    (send _image :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; duckiepond/Box[] _list
     (write-long (length _list) s)
     (dolist (elem _list)
       (send elem :serialize s)
       )
     ;; int32 _image_width
       (write-long _image_width s)
     ;; int32 _image_height
       (write-long _image_height s)
     ;; sensor_msgs/CompressedImage _image
       (send _image :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; duckiepond/Box[] _list
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _list (let (r) (dotimes (i n) (push (instance duckiepond::Box :init) r)) r))
     (dolist (elem- _list)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; int32 _image_width
     (setq _image_width (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _image_height
     (setq _image_height (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; sensor_msgs/CompressedImage _image
     (send _image :deserialize buf ptr-) (incf ptr- (send _image :serialization-length))
   ;;
   self)
  )

(setf (get duckiepond::Boxlist :md5sum-) "64ed701dbabc3b78cf16142116cf4f2f")
(setf (get duckiepond::Boxlist :datatype-) "duckiepond/Boxlist")
(setf (get duckiepond::Boxlist :definition-)
      "Box[] list
int32 image_width
int32 image_height
sensor_msgs/CompressedImage image
================================================================================
MSG: duckiepond/Box
int32 x
int32 y
int32 w
int32 h
float32 confidence
int32 id
================================================================================
MSG: sensor_msgs/CompressedImage
# This message contains a compressed image

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image

string format        # Specifies the format of the data
                     #   Acceptable values:
                     #     jpeg, png
uint8[] data         # Compressed image buffer

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :duckiepond/Boxlist "64ed701dbabc3b78cf16142116cf4f2f")


