;; Auto-generated. Do not edit!


(when (boundp 'duckiepond::Motor4Cmd)
  (if (not (find-package "DUCKIEPOND"))
    (make-package "DUCKIEPOND"))
  (shadow 'Motor4Cmd (find-package "DUCKIEPOND")))
(unless (find-package "DUCKIEPOND::MOTOR4CMD")
  (make-package "DUCKIEPOND::MOTOR4CMD"))

(in-package "ROS")
;;//! \htmlinclude Motor4Cmd.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass duckiepond::Motor4Cmd
  :super ros::object
  :slots (_header _lf _rf _lr _rr ))

(defmethod duckiepond::Motor4Cmd
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:lf __lf) 0.0)
    ((:rf __rf) 0.0)
    ((:lr __lr) 0.0)
    ((:rr __rr) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _lf (float __lf))
   (setq _rf (float __rf))
   (setq _lr (float __lr))
   (setq _rr (float __rr))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:lf
   (&optional __lf)
   (if __lf (setq _lf __lf)) _lf)
  (:rf
   (&optional __rf)
   (if __rf (setq _rf __rf)) _rf)
  (:lr
   (&optional __lr)
   (if __lr (setq _lr __lr)) _lr)
  (:rr
   (&optional __rr)
   (if __rr (setq _rr __rr)) _rr)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float32 _lf
    4
    ;; float32 _rf
    4
    ;; float32 _lr
    4
    ;; float32 _rr
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float32 _lf
       (sys::poke _lf (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _rf
       (sys::poke _rf (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _lr
       (sys::poke _lr (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _rr
       (sys::poke _rr (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float32 _lf
     (setq _lf (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _rf
     (setq _rf (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _lr
     (setq _lr (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _rr
     (setq _rr (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get duckiepond::Motor4Cmd :md5sum-) "77d80b96b13055bc97b62acface81cb7")
(setf (get duckiepond::Motor4Cmd :datatype-) "duckiepond/Motor4Cmd")
(setf (get duckiepond::Motor4Cmd :definition-)
      "# Thrust command - typically ranges from {-1.0 - 1.0}
Header header
float32 lf
float32 rf
float32 lr
float32 rr
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



(provide :duckiepond/Motor4Cmd "77d80b96b13055bc97b62acface81cb7")


