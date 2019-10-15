;; Auto-generated. Do not edit!


(when (boundp 'duckiepond::SetValue)
  (if (not (find-package "DUCKIEPOND"))
    (make-package "DUCKIEPOND"))
  (shadow 'SetValue (find-package "DUCKIEPOND")))
(unless (find-package "DUCKIEPOND::SETVALUE")
  (make-package "DUCKIEPOND::SETVALUE"))
(unless (find-package "DUCKIEPOND::SETVALUEREQUEST")
  (make-package "DUCKIEPOND::SETVALUEREQUEST"))
(unless (find-package "DUCKIEPOND::SETVALUERESPONSE")
  (make-package "DUCKIEPOND::SETVALUERESPONSE"))

(in-package "ROS")





(defclass duckiepond::SetValueRequest
  :super ros::object
  :slots (_value ))

(defmethod duckiepond::SetValueRequest
  (:init
   (&key
    ((:value __value) 0.0)
    )
   (send-super :init)
   (setq _value (float __value))
   self)
  (:value
   (&optional __value)
   (if __value (setq _value __value)) _value)
  (:serialization-length
   ()
   (+
    ;; float32 _value
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _value
       (sys::poke _value (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _value
     (setq _value (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass duckiepond::SetValueResponse
  :super ros::object
  :slots ())

(defmethod duckiepond::SetValueResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass duckiepond::SetValue
  :super ros::object
  :slots ())

(setf (get duckiepond::SetValue :md5sum-) "0aca93dcf6d857f0e5a0dc6be1eaa9fb")
(setf (get duckiepond::SetValue :datatype-) "duckiepond/SetValue")
(setf (get duckiepond::SetValue :request) duckiepond::SetValueRequest)
(setf (get duckiepond::SetValue :response) duckiepond::SetValueResponse)

(defmethod duckiepond::SetValueRequest
  (:response () (instance duckiepond::SetValueResponse :init)))

(setf (get duckiepond::SetValueRequest :md5sum-) "0aca93dcf6d857f0e5a0dc6be1eaa9fb")
(setf (get duckiepond::SetValueRequest :datatype-) "duckiepond/SetValueRequest")
(setf (get duckiepond::SetValueRequest :definition-)
      "float32 value
---
")

(setf (get duckiepond::SetValueResponse :md5sum-) "0aca93dcf6d857f0e5a0dc6be1eaa9fb")
(setf (get duckiepond::SetValueResponse :datatype-) "duckiepond/SetValueResponse")
(setf (get duckiepond::SetValueResponse :definition-)
      "float32 value
---
")



(provide :duckiepond/SetValue "0aca93dcf6d857f0e5a0dc6be1eaa9fb")


