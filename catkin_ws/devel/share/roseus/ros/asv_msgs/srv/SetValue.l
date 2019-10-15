;; Auto-generated. Do not edit!


(when (boundp 'asv_msgs::SetValue)
  (if (not (find-package "ASV_MSGS"))
    (make-package "ASV_MSGS"))
  (shadow 'SetValue (find-package "ASV_MSGS")))
(unless (find-package "ASV_MSGS::SETVALUE")
  (make-package "ASV_MSGS::SETVALUE"))
(unless (find-package "ASV_MSGS::SETVALUEREQUEST")
  (make-package "ASV_MSGS::SETVALUEREQUEST"))
(unless (find-package "ASV_MSGS::SETVALUERESPONSE")
  (make-package "ASV_MSGS::SETVALUERESPONSE"))

(in-package "ROS")





(defclass asv_msgs::SetValueRequest
  :super ros::object
  :slots (_value ))

(defmethod asv_msgs::SetValueRequest
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

(defclass asv_msgs::SetValueResponse
  :super ros::object
  :slots ())

(defmethod asv_msgs::SetValueResponse
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

(defclass asv_msgs::SetValue
  :super ros::object
  :slots ())

(setf (get asv_msgs::SetValue :md5sum-) "0aca93dcf6d857f0e5a0dc6be1eaa9fb")
(setf (get asv_msgs::SetValue :datatype-) "asv_msgs/SetValue")
(setf (get asv_msgs::SetValue :request) asv_msgs::SetValueRequest)
(setf (get asv_msgs::SetValue :response) asv_msgs::SetValueResponse)

(defmethod asv_msgs::SetValueRequest
  (:response () (instance asv_msgs::SetValueResponse :init)))

(setf (get asv_msgs::SetValueRequest :md5sum-) "0aca93dcf6d857f0e5a0dc6be1eaa9fb")
(setf (get asv_msgs::SetValueRequest :datatype-) "asv_msgs/SetValueRequest")
(setf (get asv_msgs::SetValueRequest :definition-)
      "float32 value
---
")

(setf (get asv_msgs::SetValueResponse :md5sum-) "0aca93dcf6d857f0e5a0dc6be1eaa9fb")
(setf (get asv_msgs::SetValueResponse :datatype-) "asv_msgs/SetValueResponse")
(setf (get asv_msgs::SetValueResponse :definition-)
      "float32 value
---
")



(provide :asv_msgs/SetValue "0aca93dcf6d857f0e5a0dc6be1eaa9fb")


