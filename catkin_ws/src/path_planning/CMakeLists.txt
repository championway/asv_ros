cmake_minimum_required(VERSION 2.8.3)
project(path_planning)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  gazebo_ros
  geometry_msgs
  nav_msgs
  pcl_ros
  pcl_conversions
  roscpp
  rospy
  sensor_msgs
  std_msgs
  asv_msgs
  tf
  tf_conversions
  dynamic_reconfigure
  nav_msgs
  message_generation
)

#add_service_files(
#  FILES
#)

#generate_dynamic_reconfigure_options(
#)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
  nav_msgs
)

catkin_package(
)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

SET(CMAKE_CXX_FLAGS "-std=c++0x")
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)
find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIRS})

add_executable(obstacle_avoidance src/obstacle_avoidance.cpp)
add_dependencies(obstacle_avoidance ${catkin_EXPORTED_TARGETS} ${PROJECT_NAME}_gencpp)
target_link_libraries(obstacle_avoidance ${catkin_LIBRARIES} ${EIGEN3_LIBRARIES})