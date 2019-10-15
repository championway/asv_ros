;; Auto-generated. Do not edit!


(when (boundp 'duckiepond::Heading)
  (if (not (find-package "DUCKIEPOND"))
    (make-package "DUCKIEPOND"))
  (shadow 'Heading (find-package "DUCKIEPOND")))
(unless (find-package "DUCKIEPOND::HEADING")
  (make-package "DUCKIEPOND::HEADING"))

(in-package "ROS")
;;//! \htmlinclude Heading.msg.html


(defclass duckiepond::Heading
  :super ros::object
  :slots (_phi _speed ))

(defmethod duckiepond::Heading
  (:init
   (&key
    ((:phi __phi) 0.0)
    ((:speed __speed) 0.0)
    )
   (send-super :init)
   (setq _phi (float __phi))
   (setq _speed (float __speed))
   self)
  (:phi
   (&optional __phi)
   (if __phi (setq _phi __phi)) _phi)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:serialization-length
   ()
   (+
    ;; float32 _phi
    4
    ;; float32 _speed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _phi
       (sys::poke _phi (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _phi
     (setq _phi (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get duckiepond::Heading :md5sum-) "8fe8a91eef3de9ae7860b3f07a1529db")
(setf (get duckiepond::Heading :datatype-) "duckiepond/Heading")
(setf (get duckiepond::Heading :definition-)
      "float32 phi
float32 speed
")



(provide :duckiepond/Heading "8fe8a91eef3de9ae7860b3f07a1529db")


