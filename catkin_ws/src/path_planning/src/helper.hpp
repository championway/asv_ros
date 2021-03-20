#include <Eigen/Dense>
#include <tf/transform_listener.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/Point.h>
#include <nav_msgs/OccupancyGrid.h>
#include <nav_msgs/MapMetaData.h>

const float EPS = 1e-2;
// Convert int data[] to Eigen::MatrixXd
void grid_to_matrix(const nav_msgs::OccupancyGrid msg, Eigen::MatrixXd &map){
  for(int i=0; i<msg.data.size(); ++i){
    map(i/msg.info.width,i%msg.info.height) = msg.data[i];
  }
}
// Get indices of grid from position
// Return false if out of range
bool pose_to_idx(nav_msgs::MapMetaData info, double target_x, double target_y, int& idx_x, int& idx_y){
  geometry_msgs::Pose origin = info.origin;
  float resolution = info.resolution;
  int map_width = info.width, map_height = info.height;
  idx_x = floor((target_x - origin.position.x + EPS)/resolution);
  idx_y = floor((target_y - origin.position.y + EPS)/resolution);
  if(idx_x<0 or idx_x>=map_height or idx_y<0 or idx_y>=map_height) return false;
  return true;
}
// Convert indices of grid to position with type PoseStamped
geometry_msgs::PoseStamped indice_to_pose(nav_msgs::MapMetaData info, int x, int y){
  geometry_msgs::Pose origin = info.origin;
  float resolution = info.resolution;
  geometry_msgs::PoseStamped res;
  res.pose.position.x = origin.position.x+resolution*y;
  res.pose.position.y = origin.position.y+resolution*x; // Have to change xy order
  res.pose.orientation.w = 1.0;
  return res;
}
// Convert indices of grid to position with type Point
geometry_msgs::Point indice_to_point(nav_msgs::MapMetaData info, int x, int y){
  geometry_msgs::Pose origin = info.origin;
  float resolution = info.resolution;
  geometry_msgs::Point res;
  res.x = origin.position.x+resolution*y;
  res.y = origin.position.y+resolution*x; // Have to change xy order
  return res;
}
// Convert frame of pose with given transform
void convertFrame(tf::Transform mat, geometry_msgs::PoseStamped &ps){
  tf::Vector3 pos(ps.pose.position.x, ps.pose.position.y, 0), res = mat*pos;
  ps.pose.position.x = res.getX(); ps.pose.position.y = res.getY();
}
// Convert frame of pose with given transform
void convertFrame(tf::Transform mat, geometry_msgs::Pose &ps){
  tf::Vector3 pos(ps.position.x, ps.position.y, 0), res = mat*pos;
  ps.position.x = res.getX(); ps.position.y = res.getY();
}
// Overloading for input point
void convertFrame(tf::Transform mat, geometry_msgs::Point &p){
  tf::Vector3 pos(p.x, p.y, 0), res = mat*pos;
  p.x = res.getX(); p.y = res.getY();
}
