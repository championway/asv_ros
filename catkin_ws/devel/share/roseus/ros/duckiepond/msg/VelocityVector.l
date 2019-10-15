;; Auto-generated. Do not edit!


(when (boundp 'duckiepond::VelocityVector)
  (if (not (find-package "DUCKIEPOND"))
    (make-package "DUCKIEPOND"))
  (shadow 'VelocityVector (find-package "DUCKIEPOND")))
(unless (find-package "DUCKIEPOND::VELOCITYVECTOR")
  (make-package "DUCKIEPOND::VELOCITYVECTOR"))

(in-package "ROS")
;;//! \htmlinclude VelocityVector.msg.html


(defclass duckiepond::VelocityVector
  :super ros::object
  :slots (_x _y _angular ))

(defmethod duckiepond::VelocityVector
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:angular __angular) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _angular (float __angular))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:angular
   (&optional __angular)
   (if __angular (setq _angular __angular)) _angular)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ;; float32 _angular
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _angular
       (sys::poke _angular (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _angular
     (setq _angular (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get duckiepond::VelocityVector :md5sum-) "1b6108f70c66951a6da12942857785cf")
(setf (get duckiepond::VelocityVector :datatype-) "duckiepond/VelocityVector")
(setf (get duckiepond::VelocityVector :definition-)
      "#velocity command {1,-1}
float32 x
float32 y
float32 angular
")



(provide :duckiepond/VelocityVector "1b6108f70c66951a6da12942857785cf")


