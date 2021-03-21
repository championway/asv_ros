/**********************************
Author: David Chen
Revised by Sean Lu
Date: 2019/03/30 
Last update: 2019/04/01
Point Cloud Obstacle Detection
Subscribe: 
  /velodyne_points      (sensor_msgs/PointCloud2)
Publish:
  /pcl_preprocess       (sensor_msgs/PointCloud2)
  /local_map            (nav_msgs/OccupancyGrid)
***********************************/ 
// C++ STL
#include <cassert>
//ROS Lib
#include <ros/ros.h>
#include <ros/console.h>
#include <sensor_msgs/PointCloud2.h>
#include <sensor_msgs/LaserScan.h>
#include <nav_msgs/OccupancyGrid.h>
#include <std_srvs/Empty.h>
#include <std_srvs/Trigger.h>
//PCL lib
#include <pcl/io/pcd_io.h>
#include <pcl_ros/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/common/transforms.h>
#include <pcl/filters/radius_outlier_removal.h>
#include <pcl/filters/conditional_removal.h>
#include <pcl/filters/passthrough.h>
#include <pcl/ModelCoefficients.h>
#include <pcl/filters/project_inliers.h>
#include <pcl/kdtree/kdtree_flann.h>
//TF lib
#include <tf/transform_listener.h>
#include <tf/transform_datatypes.h>
#include <tf_conversions/tf_eigen.h>
//Tool
#include <laser_geometry/laser_geometry.h>

using namespace std;
typedef pcl::PointCloud<pcl::PointXYZ> PointCloudXYZ;
typedef pcl::PointCloud<pcl::PointXYZRGB> PointCloudXYZRGB;

class Obstacle_Detection{
private:
  laser_geometry::LaserProjection projector_; // Convert Laser Scanner to PointCloud
  tf::TransformListener listener;

  string node_name;
  string robot_frame;
  string lidar_frame;

  // Only point cloud in these range will be take into account
  double range_min;
  double range_max;
  double angle_min;
  double angle_max;
  double height_max;
  double height_min;

  // Range of robot itself
  double robot_x_max;
  double robot_x_min;
  double robot_y_max;
  double robot_y_min;
  double robot_z_max;
  double robot_z_min;
  vector< vector<double> > kernel;
  vector<double> velodyne2husky;

  // Define map
  int map_size; // Square assumed
  int compute_size;
  float map_resolution;
  nav_msgs::OccupancyGrid occupancygrid;
  int obs_size;
  int dilating_size;

  ros::NodeHandle nh, pnh;
  ros::Subscriber sub_cloud;
  ros::Subscriber sub_point;
  ros::Publisher  pub_cloud;
  ros::Publisher  pub_points;
  ros::Publisher  pub_map;

  ros::ServiceServer service;
  vector<double> getStaticTf(void);

public:
  Obstacle_Detection(ros::NodeHandle&, ros::NodeHandle&);
  void cbLaser(const sensor_msgs::LaserScanConstPtr&);
  bool obstacle_srv(std_srvs::Trigger::Request&, std_srvs::Trigger::Response&);
  void pcl_preprocess(const PointCloudXYZRGB::Ptr, PointCloudXYZRGB::Ptr);
  void mapping(const PointCloudXYZ::Ptr);
  void map2occupancygrid(float&, float&);
};

Obstacle_Detection::Obstacle_Detection(ros::NodeHandle &n, ros::NodeHandle &pn):
                                       nh(n), pnh(pn){
  node_name = ros::this_node::getName();

  //Read yaml file and set costumes parameters
  if(!pnh.getParam("range_min", range_min)) range_min=0.0;
  if(!pnh.getParam("range_max", range_max)) range_max=30.0;
  if(!pnh.getParam("angle_min", angle_min)) angle_min = -180.0;
  if(!pnh.getParam("angle_max", angle_max)) angle_max = 180.0;
  if(!pnh.getParam("height_min", height_min)) height_min = -0.3;
  if(!pnh.getParam("height_max", height_max)) height_max = 0.5;
  if(!pnh.getParam("robot_x_max", robot_x_max)) robot_x_max=0.05;
  if(!pnh.getParam("robot_x_min", robot_x_min)) robot_x_min=-0.6;
  if(!pnh.getParam("robot_y_max", robot_y_max)) robot_y_max=0.1;
  if(!pnh.getParam("robot_y_min", robot_y_min)) robot_y_min=-0.1;
  if(!pnh.getParam("robot_z_max", robot_z_max)) robot_z_max=1.;
  if(!pnh.getParam("robot_z_min", robot_z_min)) robot_z_min=-1.5;
  if(!pnh.getParam("robot_frame", robot_frame)) robot_frame="/robot_base";
  if(!pnh.getParam("lidar_frame", lidar_frame)) lidar_frame="/laser";
  if(!pnh.getParam("map_resolution", map_resolution)) map_resolution=0.3;
  if(!pnh.getParam("obs_size", obs_size)) obs_size=2;
  if(!pnh.getParam("dilating_size", dilating_size)) dilating_size=4;
  if(!pnh.getParam("map_size", map_size)) map_size=200;
  if(!pnh.getParam("compute_size", compute_size)) compute_size=20;
  // Parameter information
  ROS_INFO("[%s] Initializing ", node_name.c_str());
  ROS_INFO("[%s] Param [range_max] = %f, [range_min] = %f", node_name.c_str(), range_max, range_min);
  ROS_INFO("[%s] Param [angle_max] = %f, [angle_min] = %f", node_name.c_str(), angle_max, angle_min);
  ROS_INFO("[%s] Param [height_max] = %f, [height_min] = %f", node_name.c_str(), height_max, height_min);
  ROS_INFO("[%s] Param [robot_x_max] = %f, [robot_x_min] = %f", node_name.c_str(), robot_x_max, robot_x_min);
  ROS_INFO("[%s] Param [robot_y_max] = %f, [robot_y_min] = %f", node_name.c_str(), robot_y_max, robot_y_min);
  ROS_INFO("[%s] Param [robot_z_max] = %f, [robot_z_min] = %f", node_name.c_str(), robot_z_max, robot_z_min);
  ROS_INFO("[%s] Param [robot_frame] = %s, [map_resolution] = %f", node_name.c_str(), robot_frame.c_str(), map_resolution);
  ROS_INFO("[%s] Param [lidar_frame] = %s", node_name.c_str(), lidar_frame.c_str());
  ROS_INFO("[%s] Param [obs_size] = %d, [dilating_size] = %d", node_name.c_str(), obs_size, dilating_size);
  ROS_INFO("[%s] Param [map_size] = %d", node_name.c_str(), map_size);
  
  //velodyne2husky = getStaticTf(); 
  //ROS_INFO("%f %f %f", velodyne2husky[0], velodyne2husky[1], velodyne2husky[2]);
  
  // Set map meta data
  occupancygrid.header.frame_id = lidar_frame;
  occupancygrid.info.resolution = map_resolution;
  occupancygrid.info.width = map_size;
  occupancygrid.info.height = map_size;
  occupancygrid.info.origin.position.x = -map_size*map_resolution/2.;
  occupancygrid.info.origin.position.y = -map_size*map_resolution/2.;

  // Define kernel
  /*kernel =  {
              {10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10},
              {10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 10},
              {10, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 20, 10},
              {10, 20, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 30, 20, 10},
              {10, 20, 30, 40, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 40, 30, 20, 10},
              {10, 20, 30, 40, 50, 60, 60, 60, 60, 60, 60, 60, 60, 60, 50, 40, 30, 20, 10},
              {10, 20, 30, 40, 50, 60, 70, 70, 70, 70, 70, 70, 70, 60, 50, 40, 30, 20, 10},
              {10, 20, 30, 40, 50, 60, 70, 80, 80, 80, 80, 80, 70, 60, 50, 40, 30, 20, 10},
              {10, 20, 30, 40, 50, 60, 70, 80, 90, 90, 90, 80, 70, 60, 50, 40, 30, 20, 10}, 
              {10, 20, 30, 40, 50, 60, 70, 80, 90,100, 90, 80, 70, 60, 50, 40, 30, 20, 10},
              {10, 20, 30, 40, 50, 60, 70, 80, 90, 90, 90, 80, 70, 60, 50, 40, 30, 20, 10},
              {10, 20, 30, 40, 50, 60, 70, 80, 80, 80, 80, 80, 70, 60, 50, 40, 30, 20, 10},
              {10, 20, 30, 40, 50, 60, 70, 70, 70, 70, 70, 70, 70, 60, 50, 40, 30, 20, 10},
              {10, 20, 30, 40, 50, 60, 60, 60, 60, 60, 60, 60, 60, 60, 50, 40, 30, 20, 10},
              {10, 20, 30, 40, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 40, 30, 20, 10},
              {10, 20, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 30, 20, 10},
              {10, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 20, 10},
              {10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 10},
              {10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10},
            };*/

  /*kernel =  {
              {20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20},
              {20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 20},
              {20, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 30, 20},
              {20, 30, 40, 50, 50, 50, 50, 50, 50, 50, 50, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 60, 60, 60, 60, 60, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 80, 80, 80, 80, 80, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 80, 90, 90, 90, 80, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 80, 90,100, 90, 80, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 80, 90, 90, 90, 80, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 80, 80, 80, 80, 80, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 60, 60, 60, 60, 60, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 50, 50, 50, 50, 50, 50, 50, 50, 40, 30, 20},
              {20, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 30, 20},
              {20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 20},
              {20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20},
            };*/

  /*kernel =  {
              {20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20},
              {20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 20},
              {20, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 30, 20},
              {20, 30, 40, 50, 50, 50, 50, 50, 50, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 60, 60, 60, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 80, 80, 80, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 80,100, 80, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 80, 80, 80, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 60, 60, 60, 60, 60, 50, 40, 30, 20},
              {20, 30, 40, 50, 50, 50, 50, 50, 50, 50, 40, 30, 20},
              {20, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 30, 20},
              {20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 20},
              {20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20},
            };*/

  /*kernel =  {
              {20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20},
              {20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 20},
              {20, 30, 40, 40, 40, 40, 40, 40, 40, 30, 20},
              {20, 30, 40, 50, 50, 50, 50, 50, 40, 30, 20},
              {20, 30, 40, 50, 80, 80, 80, 50, 40, 30, 20},
              {20, 30, 40, 50, 80,100, 80, 50, 40, 30, 20},
              {20, 30, 40, 50, 80, 80, 80, 50, 40, 30, 20},
              {20, 30, 40, 50, 50, 50, 50, 50, 40, 30, 20},
              {20, 30, 40, 40, 40, 40, 40, 40, 40, 30, 20},
              {20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 20},
              {20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20},
            };*/

  kernel =  {
              {20, 20, 20, 20, 20, 20, 20, 20, 20},
              {20, 40, 40, 40, 40, 40, 40, 40, 20},
              {20, 40, 60, 60, 60, 60, 60, 40, 20},
              {20, 40, 60, 80, 80, 80, 60, 40, 20},
              {20, 40, 60, 80,100, 80, 60, 40, 20},
              {20, 40, 60, 80, 80, 80, 60, 40, 20},
              {20, 40, 60, 60, 60, 60, 60, 40, 20},
              {20, 40, 40, 40, 40, 40, 40, 40, 20},
              {20, 20, 20, 20, 20, 20, 20, 20, 20},
            };

  /*kernel =  {
              {10, 10, 10, 10, 10, 10, 10},
              {10, 50, 50, 50, 50, 50, 10},
              {10, 50, 70, 70, 70, 50, 10},
              {10, 50, 70,100, 70, 50, 10},
              {10, 50, 70, 70, 70, 50, 10},
              {10, 50, 50, 50, 50, 50, 10},
              {10, 10, 10, 10, 10, 10, 10},
            };*/


  // Service
  service = pnh.advertiseService("obstacle_srv", &Obstacle_Detection::obstacle_srv, this);
  // Publisher
  pub_cloud = pnh.advertise<sensor_msgs::PointCloud2> ("pcl_preprocess", 1);
  pub_map = pnh.advertise<nav_msgs::OccupancyGrid> ("/ASV/occupancy_grid", 1);
  // Subscriber
  sub_cloud = pnh.subscribe("/scan", 1, &Obstacle_Detection::cbLaser, this);
}

vector<double> Obstacle_Detection::getStaticTf(void){
  vector<double> res;
  res.resize(3);
  //tf::TransformListener listener;
  tf::StampedTransform transform;
  try{
    listener.waitForTransform(robot_frame, lidar_frame, ros::Time(0), ros::Duration(5.0));
    listener.lookupTransform(robot_frame, lidar_frame, ros::Time(0), transform);
    res[0] = transform.getOrigin().getX(); 
    res[1] = transform.getOrigin().getY(); 
    res[2] = transform.getOrigin().getZ(); 
    return res;
  } catch (tf::TransformException ex){
    ROS_ERROR("%s",ex.what());
    assert(false);
  }
}
// Service callback template
bool Obstacle_Detection::obstacle_srv(std_srvs::Trigger::Request &req, std_srvs::Trigger::Response &res){
  res.success = 1;
  res.message = "Call obstacle detection service";
  cout << "Call detection service" << endl;
  return true;
}

void Obstacle_Detection::cbLaser(const sensor_msgs::LaserScanConstPtr& laser_msg){
  // transfer ros msg to point cloud
  /*PointCloudXYZRGB::Ptr cloud_in_rgb(new PointCloudXYZRGB()); 
  PointCloudXYZ::Ptr cloud_in(new PointCloudXYZ()); 
  PointCloudXYZRGB::Ptr cloud_out(new PointCloudXYZRGB());
  pcl::fromROSMsg (*cloud_msg, *cloud_in); 

  copyPointCloud(*cloud_in, *cloud_in_rgb); 
  clock_t time = clock();
  // Remove out of range points and robot points
  pcl_preprocess(cloud_in_rgb, cloud_out); //printf("PRE: %f\n", (double)(clock()-time)/CLOCKS_PER_SEC); 
  */
  if (!listener.waitForTransform(
          laser_msg->header.frame_id, 
          "robot_base", 
          laser_msg->header.stamp + 
          ros::Duration().fromSec(laser_msg->ranges.size()*laser_msg->time_increment),
          ros::Duration(1.0))){
    return;
  }
  sensor_msgs::PointCloud2 pcl_input;
  PointCloudXYZ::Ptr cloud_out(new PointCloudXYZ());
  projector_.transformLaserScanToPointCloud("laser", *laser_msg, pcl_input, listener);
  pcl::fromROSMsg (pcl_input, *cloud_out); 
  clock_t time = clock();
  mapping(cloud_out); //printf("Map: %f\n", (double)(clock()-time)/CLOCKS_PER_SEC);
  // Publish point cloud
  sensor_msgs::PointCloud2 pcl_output;
  pcl::toROSMsg(*cloud_out, pcl_output);
  pcl_output.header = laser_msg->header;
  pcl_output.header.frame_id = lidar_frame;
  pub_cloud.publish(pcl_output);
}

void Obstacle_Detection::pcl_preprocess(const PointCloudXYZRGB::Ptr cloud_in, PointCloudXYZRGB::Ptr cloud_out){
  clock_t time = clock();
  // Remove NaN point
  std::vector<int> indices;
  pcl::removeNaNFromPointCloud(*cloud_in, *cloud_in, indices);
  for(auto& p:cloud_in->points){
    p.x += velodyne2husky[0];
    //p.y += velodyne2husky[1];
    //p.z += velodyne2husky[2];
  } 
  //printf("Remove nan: %f\n", (double)(clock()-time)/CLOCKS_PER_SEC); time = clock();
  // Range filter
  float dis2, angle = 0;
  int num = 0; // Number of points counter
  // Conditional or to define range that out side the robot
  // x
  pcl::ConditionOr<pcl::PointXYZRGB>::Ptr range_cond(new pcl::ConditionOr<pcl::PointXYZRGB>());
  range_cond->addComparison(pcl::FieldComparison<pcl::PointXYZRGB>::ConstPtr(new
    pcl::FieldComparison<pcl::PointXYZRGB>("x", pcl::ComparisonOps::GT, robot_x_max)));
  range_cond->addComparison(pcl::FieldComparison<pcl::PointXYZRGB>::ConstPtr(new
    pcl::FieldComparison<pcl::PointXYZRGB>("x", pcl::ComparisonOps::LT, robot_x_min)));
  // y
  range_cond->addComparison(pcl::FieldComparison<pcl::PointXYZRGB>::ConstPtr(new
    pcl::FieldComparison<pcl::PointXYZRGB>("y", pcl::ComparisonOps::GT, robot_y_max)));
  range_cond->addComparison(pcl::FieldComparison<pcl::PointXYZRGB>::ConstPtr(new
    pcl::FieldComparison<pcl::PointXYZRGB>("y", pcl::ComparisonOps::LT, robot_y_min)));  
  // z
  range_cond->addComparison(pcl::FieldComparison<pcl::PointXYZRGB>::ConstPtr(new
    pcl::FieldComparison<pcl::PointXYZRGB>("z", pcl::ComparisonOps::LT, robot_z_max)));  
  range_cond->addComparison(pcl::FieldComparison<pcl::PointXYZRGB>::ConstPtr(new
    pcl::FieldComparison<pcl::PointXYZRGB>("z", pcl::ComparisonOps::LT, robot_z_min)));  
  // Build conditional removal filter
  pcl::ConditionalRemoval<pcl::PointXYZRGB> condrem;
  condrem.setCondition (range_cond);
  condrem.setInputCloud (cloud_in);
  // Then apply it
  condrem.filter (*cloud_in);  
  // Consider only pz in [height_min, height_max]  
  pcl::PassThrough<pcl::PointXYZRGB> pass;
  pass.setInputCloud(cloud_in);
  pass.setFilterFieldName("z");
  pass.setFilterLimits(height_min, height_max);
  pass.filter(*cloud_in);
  //printf("Range filter: %f\n", (double)(clock()-time)/CLOCKS_PER_SEC); time = clock();
  // Since we need to calculate angle of each point, use iteration to traverse through all points
  // This is not pretty computation heavy because we have filtered out lots points
  
  for(PointCloudXYZRGB::iterator it=cloud_in->begin(); it != cloud_in->end();it++){
    dis2 = it->x * it->x + it->y * it->y; // Only consider XY distance square
    angle = atan2f(it->y, it->x);
    angle = angle * 180 / M_PI; // Angle of the point in robot coordinate space
    // Filter out if the point is in or out of the range we define
    bool is_in_range =  dis2 >= range_min*range_min  &&  dis2 <= range_max*range_max && 
                        angle >= angle_min && angle <= angle_max;
    if(is_in_range){cloud_out->points.push_back(*it); ++num;}
  }
  cloud_out->width = num;
  cloud_out->height = 1;
  cloud_out->points.resize(num);
  
  /*
  // Project all inliers to XY-plane
  pcl::ModelCoefficients::Ptr coefficients (new pcl::ModelCoefficients());
  coefficients->values.resize(4);
  coefficients->values[0] = coefficients->values[1] = coefficients->values[3] = 0.0;
  coefficients->values[2] = 1.0;
  pcl::ProjectInliers<pcl::PointXYZRGB> proj;
  proj.setModelType(pcl::SACMODEL_PLANE);
  proj.setInputCloud(cloud_in);
  proj.setModelCoefficients(coefficients);
  proj.filter(*cloud_in);
  // Build KD tree
  pcl::KdTreeFLANN<pcl::PointXYZRGB> kdtree;
  kdtree.setInputCloud(cloud_in);
  pcl::PointXYZRGB search_point; // (0, 0, 0)
  search_point.x = search_point.y = search_point.z = 0.0;
  std::vector<int> pointIdxRadiusSearch;
  std::vector<float> pointRadiusSquareDistance;
  float radius = range_max;
  if(kdtree.radiusSearch(search_point, radius, pointIdxRadiusSearch, pointRadiusSquareDistance) >0){
    for(size_t i=0; i<pointIdxRadiusSearch.size(); ++i){
      cloud_out->points.push_back(cloud_in->points[pointIdxRadiusSearch[i]]);
    }
  }
  */
  //printf("Distance filter: %f\n", (double)(clock()-time)/CLOCKS_PER_SEC); time = clock();
  // Point cloud noise filter
  /* Cost too much time!
  pcl::RadiusOutlierRemoval<pcl::PointXYZRGB> outrem;
  outrem.setInputCloud(cloud_out);
  outrem.setRadiusSearch(0.8);
  outrem.setMinNeighborsInRadius(2);
  outrem.filter(*cloud_out);
  printf("Noise filter: %f\n", (double)(clock()-time)/CLOCKS_PER_SEC);
  */
}

void Obstacle_Detection::mapping(const PointCloudXYZ::Ptr cloud){
  float x;
  float y;
  occupancygrid.data.clear();

  int map_array[map_size][map_size] = {0};
  int potential_field[map_size][map_size] = {0};

  for (PointCloudXYZ::iterator it = cloud->begin(); it != cloud->end() ; ++it){
    x = it->x;
    y = it->y;
    map2occupancygrid(x, y);
    
// Check bound
    if (int(y) < map_size && int(x) < map_size && int(y) >= 0 && int(x) >= 0){
      map_array[int(y)][int(x)] = 1;
    }
  }

  // Map dilating
  int k_size = int(kernel.size()/2);
  int middle = int(map_size/2);

  for (int j = middle - compute_size; j < middle + compute_size; j++){
    for (int i = middle - compute_size; i < middle + compute_size; i++){
      // Convolution
      vector <int> conv_vec;
      for (int m = -k_size; m < k_size; m++){
        for (int n = -k_size; n < k_size; n++){
          conv_vec.push_back(kernel[m + k_size][n + k_size] * map_array[j + m][i + n]);
        }
      }
      potential_field[j][i] = *std::max_element(std::begin(conv_vec), std::end(conv_vec));
    }
  }

  /*for (int j = 0 + k_size; j < map_size - k_size; j++){
    for (int i = 0 + k_size; i < map_size - k_size; i++){
      // Convolution
      vector <int> conv_vec;
      for (int m = -k_size; m < k_size; m++){
        for (int n = -k_size; n < k_size; n++){
          conv_vec.push_back(kernel[m + k_size][n + k_size] * map_array[j + m][i + n]);
        }
      }
      potential_field[j][i] = *std::max_element(std::begin(conv_vec), std::end(conv_vec));
    }
  }*/

  /*for (int j = 0; j < map_size; j++){
    for (int i = 0; i < map_size; i++){
      if (map_array[j][i] == 100){
        for (int m = -dilating_size; m < dilating_size + 1; m++){
          for (int n = -dilating_size; n < dilating_size + 1; n++){
            if(j+m<0 or j+m>=map_size or i+n<0 or i+n>=map_size) continue;
            if (map_array[j+m][i+n] != 100){
              if (m > obs_size || m < -obs_size || n > obs_size || n < -obs_size){
                if (map_array[j+m][i+n] != 80){
                  map_array[j+m][i+n] = 50;
                }
              }
              else{
                if(j+m<0 or j+m>=map_size or i+n<0 or i+n>=map_size) continue;
                map_array[j+m][i+n] = 80;
              }
            }
          }
        }
      }
    }
  }*/

  for (int j = 0; j < map_size; j++){
    for (int i = 0; i < map_size; i++){
      occupancygrid.data.push_back(potential_field[j][i]);
    }
  }
  pub_map.publish(occupancygrid);
  return;
}

void Obstacle_Detection::map2occupancygrid(float& x, float& y){
  x = int((x - occupancygrid.info.origin.position.x)/map_resolution);
  y = int((y - occupancygrid.info.origin.position.y)/map_resolution);
}

int main (int argc, char** argv)
{
  ros::init (argc, argv, "velodyne_to_grid");
  ros::NodeHandle nh, pnh("~");
  Obstacle_Detection od(nh, pnh);
  ros::spin ();
  return 0;
}
