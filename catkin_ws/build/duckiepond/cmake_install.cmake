# Install script for directory: /home/arg/asv_ros/catkin_ws/src/duckiepond

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/arg/asv_ros/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/duckiepond/msg" TYPE FILE FILES
    "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Heading.msg"
    "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/MotorCmd.msg"
    "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Motor4Cmd.msg"
    "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/VelocityVector.msg"
    "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Box.msg"
    "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/Boxlist.msg"
    "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/BoolStamped.msg"
    "/home/arg/asv_ros/catkin_ws/src/duckiepond/msg/UsvDrive.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/duckiepond/srv" TYPE FILE FILES "/home/arg/asv_ros/catkin_ws/src/duckiepond/srv/SetValue.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/duckiepond/cmake" TYPE FILE FILES "/home/arg/asv_ros/catkin_ws/build/duckiepond/catkin_generated/installspace/duckiepond-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/arg/asv_ros/catkin_ws/devel/include/duckiepond")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/arg/asv_ros/catkin_ws/devel/share/roseus/ros/duckiepond")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/arg/asv_ros/catkin_ws/devel/share/common-lisp/ros/duckiepond")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/arg/asv_ros/catkin_ws/devel/share/gennodejs/ros/duckiepond")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/arg/asv_ros/catkin_ws/devel/lib/python2.7/dist-packages/duckiepond")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/arg/asv_ros/catkin_ws/devel/lib/python2.7/dist-packages/duckiepond")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/arg/asv_ros/catkin_ws/build/duckiepond/catkin_generated/installspace/duckiepond.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/duckiepond/cmake" TYPE FILE FILES "/home/arg/asv_ros/catkin_ws/build/duckiepond/catkin_generated/installspace/duckiepond-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/duckiepond/cmake" TYPE FILE FILES
    "/home/arg/asv_ros/catkin_ws/build/duckiepond/catkin_generated/installspace/duckiepondConfig.cmake"
    "/home/arg/asv_ros/catkin_ws/build/duckiepond/catkin_generated/installspace/duckiepondConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/duckiepond" TYPE FILE FILES "/home/arg/asv_ros/catkin_ws/src/duckiepond/package.xml")
endif()

