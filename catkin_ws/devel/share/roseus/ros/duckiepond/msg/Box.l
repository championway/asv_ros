;; Auto-generated. Do not edit!


(when (boundp 'duckiepond::Box)
  (if (not (find-package "DUCKIEPOND"))
    (make-package "DUCKIEPOND"))
  (shadow 'Box (find-package "DUCKIEPOND")))
(unless (find-package "DUCKIEPOND::BOX")
  (make-package "DUCKIEPOND::BOX"))

(in-package "ROS")
;;//! \htmlinclude Box.msg.html


(defclass duckiepond::Box
  :super ros::object
  :slots (_x _y _w _h _confidence _id ))

(defmethod duckiepond::Box
  (:init
   (&key
    ((:x __x) 0)
    ((:y __y) 0)
    ((:w __w) 0)
    ((:h __h) 0)
    ((:confidence __confidence) 0.0)
    ((:id __id) 0)
    )
   (send-super :init)
   (setq _x (round __x))
   (setq _y (round __y))
   (setq _w (round __w))
   (setq _h (round __h))
   (setq _confidence (float __confidence))
   (setq _id (round __id))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:w
   (&optional __w)
   (if __w (setq _w __w)) _w)
  (:h
   (&optional __h)
   (if __h (setq _h __h)) _h)
  (:confidence
   (&optional __confidence)
   (if __confidence (setq _confidence __confidence)) _confidence)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:serialization-length
   ()
   (+
    ;; int32 _x
    4
    ;; int32 _y
    4
    ;; int32 _w
    4
    ;; int32 _h
    4
    ;; float32 _confidence
    4
    ;; int32 _id
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _x
       (write-long _x s)
     ;; int32 _y
       (write-long _y s)
     ;; int32 _w
       (write-long _w s)
     ;; int32 _h
       (write-long _h s)
     ;; float32 _confidence
       (sys::poke _confidence (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int32 _id
       (write-long _id s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _x
     (setq _x (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _y
     (setq _y (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _w
     (setq _w (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _h
     (setq _h (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _confidence
     (setq _confidence (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get duckiepond::Box :md5sum-) "49a6b261b655b7a5a235174ffa9e8810")
(setf (get duckiepond::Box :datatype-) "duckiepond/Box")
(setf (get duckiepond::Box :definition-)
      "int32 x
int32 y
int32 w
int32 h
float32 confidence
int32 id
")



(provide :duckiepond/Box "49a6b261b655b7a5a235174ffa9e8810")


