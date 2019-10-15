# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "duckiepond: 8 messages, 1 services")

set(MSG_I_FLAGS "-Iduckiepond:/home/arg/asv_ros/catkin_ws/src/duckiepond/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg;-Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(duckiepond_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg" NAME_WE)
add_custom_target(_duckiepond_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "duckiepond" "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg" NAME_WE)
add_custom_target(_duckiepond_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "duckiepond" "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg" NAME_WE)
add_custom_target(_duckiepond_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "duckiepond" "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg" "duckiepond/Box:sensor_msgs/CompressedImage:std_msgs/Header"
)

get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg" NAME_WE)
add_custom_target(_duckiepond_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "duckiepond" "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg" ""
)

get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg" NAME_WE)
add_custom_target(_duckiepond_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "duckiepond" "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg" ""
)

get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv" NAME_WE)
add_custom_target(_duckiepond_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "duckiepond" "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv" ""
)

get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg" NAME_WE)
add_custom_target(_duckiepond_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "duckiepond" "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg" NAME_WE)
add_custom_target(_duckiepond_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "duckiepond" "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg" ""
)

get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg" NAME_WE)
add_custom_target(_duckiepond_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "duckiepond" "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
)
_generate_msg_cpp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
)
_generate_msg_cpp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg"
  "${MSG_I_FLAGS}"
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg;/opt/ros/melodic/share/sensor_msgs/cmake/../msg/CompressedImage.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
)
_generate_msg_cpp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
)
_generate_msg_cpp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
)
_generate_msg_cpp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
)
_generate_msg_cpp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
)
_generate_msg_cpp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
)

### Generating Services
_generate_srv_cpp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
)

### Generating Module File
_generate_module_cpp(duckiepond
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(duckiepond_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(duckiepond_generate_messages duckiepond_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_cpp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_cpp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_cpp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_cpp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_cpp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv" NAME_WE)
add_dependencies(duckiepond_generate_messages_cpp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_cpp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_cpp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_cpp _duckiepond_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(duckiepond_gencpp)
add_dependencies(duckiepond_gencpp duckiepond_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS duckiepond_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
)
_generate_msg_eus(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
)
_generate_msg_eus(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg"
  "${MSG_I_FLAGS}"
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg;/opt/ros/melodic/share/sensor_msgs/cmake/../msg/CompressedImage.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
)
_generate_msg_eus(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
)
_generate_msg_eus(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
)
_generate_msg_eus(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
)
_generate_msg_eus(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
)
_generate_msg_eus(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
)

### Generating Services
_generate_srv_eus(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
)

### Generating Module File
_generate_module_eus(duckiepond
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(duckiepond_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(duckiepond_generate_messages duckiepond_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_eus _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_eus _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_eus _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_eus _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_eus _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv" NAME_WE)
add_dependencies(duckiepond_generate_messages_eus _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_eus _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_eus _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_eus _duckiepond_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(duckiepond_geneus)
add_dependencies(duckiepond_geneus duckiepond_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS duckiepond_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
)
_generate_msg_lisp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
)
_generate_msg_lisp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg"
  "${MSG_I_FLAGS}"
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg;/opt/ros/melodic/share/sensor_msgs/cmake/../msg/CompressedImage.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
)
_generate_msg_lisp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
)
_generate_msg_lisp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
)
_generate_msg_lisp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
)
_generate_msg_lisp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
)
_generate_msg_lisp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
)

### Generating Services
_generate_srv_lisp(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
)

### Generating Module File
_generate_module_lisp(duckiepond
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(duckiepond_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(duckiepond_generate_messages duckiepond_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_lisp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_lisp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_lisp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_lisp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_lisp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv" NAME_WE)
add_dependencies(duckiepond_generate_messages_lisp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_lisp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_lisp _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_lisp _duckiepond_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(duckiepond_genlisp)
add_dependencies(duckiepond_genlisp duckiepond_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS duckiepond_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
)
_generate_msg_nodejs(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
)
_generate_msg_nodejs(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg"
  "${MSG_I_FLAGS}"
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg;/opt/ros/melodic/share/sensor_msgs/cmake/../msg/CompressedImage.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
)
_generate_msg_nodejs(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
)
_generate_msg_nodejs(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
)
_generate_msg_nodejs(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
)
_generate_msg_nodejs(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
)
_generate_msg_nodejs(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
)

### Generating Services
_generate_srv_nodejs(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
)

### Generating Module File
_generate_module_nodejs(duckiepond
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(duckiepond_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(duckiepond_generate_messages duckiepond_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_nodejs _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_nodejs _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_nodejs _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_nodejs _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_nodejs _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv" NAME_WE)
add_dependencies(duckiepond_generate_messages_nodejs _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_nodejs _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_nodejs _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_nodejs _duckiepond_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(duckiepond_gennodejs)
add_dependencies(duckiepond_gennodejs duckiepond_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS duckiepond_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
)
_generate_msg_py(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
)
_generate_msg_py(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg"
  "${MSG_I_FLAGS}"
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg;/opt/ros/melodic/share/sensor_msgs/cmake/../msg/CompressedImage.msg;/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
)
_generate_msg_py(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
)
_generate_msg_py(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
)
_generate_msg_py(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
)
_generate_msg_py(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
)
_generate_msg_py(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/melodic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
)

### Generating Services
_generate_srv_py(duckiepond
  "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
)

### Generating Module File
_generate_module_py(duckiepond
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(duckiepond_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(duckiepond_generate_messages duckiepond_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_py _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_py _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_py _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_py _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_py _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv" NAME_WE)
add_dependencies(duckiepond_generate_messages_py _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_py _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_py _duckiepond_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg" NAME_WE)
add_dependencies(duckiepond_generate_messages_py _duckiepond_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(duckiepond_genpy)
add_dependencies(duckiepond_genpy duckiepond_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS duckiepond_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/duckiepond
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(duckiepond_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET sensor_msgs_generate_messages_cpp)
  add_dependencies(duckiepond_generate_messages_cpp sensor_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/duckiepond
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(duckiepond_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET sensor_msgs_generate_messages_eus)
  add_dependencies(duckiepond_generate_messages_eus sensor_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/duckiepond
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(duckiepond_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET sensor_msgs_generate_messages_lisp)
  add_dependencies(duckiepond_generate_messages_lisp sensor_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/duckiepond
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(duckiepond_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET sensor_msgs_generate_messages_nodejs)
  add_dependencies(duckiepond_generate_messages_nodejs sensor_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/duckiepond
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(duckiepond_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET sensor_msgs_generate_messages_py)
  add_dependencies(duckiepond_generate_messages_py sensor_msgs_generate_messages_py)
endif()
