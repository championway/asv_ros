#include <cstdlib> // std::srand, std::rand
#include <algorithm>
#include <ros/ros.h>
#include <tf/transform_listener.h>
#include <std_msgs/Bool.h>
#include <std_msgs/ColorRGBA.h>
#include <geometry_msgs/Point.h>
#include <geometry_msgs/PoseStamped.h>
#include <nav_msgs/OccupancyGrid.h>
#include <nav_msgs/MapMetaData.h>
#include <nav_msgs/Path.h>
#include <visualization_msgs/Marker.h>
#include <visualization_msgs/MarkerArray.h>
#include <std_srvs/SetBool.h>
#include "astar.hpp"
#include "helper.hpp"
#include <std_srvs/SetBool.h>
#include <std_srvs/Trigger.h>
#include <asv_msgs/RobotGoal.h>
/*
 *   Wall following autonomously
 *
 *   Subscribe topic:
 *     ~occupancy_grid (nav_msgs::OccupancyGrid)
 *   Publish topic:
 *     ~planned_path (nav_msgs::Path)
 *     ~marker (visualization_msgs::Marker)
 *   Service Client:
 *     /emergency_stop (std_srvs::SetBool)
 *   Parameters:
 *     ~verbose (bool) Whether if publish marker, publish if set to true
 *     ~cml_verbose (bool) Whether bash will output verbose target index of searching
 *     ~left (bool) Near left or right, left if set to true
 *     ~radius (double) Radius of circle to search walkable pose
 *     ~timer_execution(int): 
 */

bool ASTAR_VERBOSE = false;
bool ASTAR_SHOWTIME = false;

class ObstacleAvoidance
{
private:
  // Parameters
  const static int NUM = 35;       // NUmber of search for target
  const static int STUCK_MAX = 10; // Stuck too long
  int timer_execution;             // Execution timer, from parameter server
  int count_reverse;
  int wait_reverse_cnt;
  int wait_threshold;
  int count;         // Execution counter
  int stuck_counter; // Counter to record stuck times
  bool use_odom;
  bool verbose;     // Whether publish marker
  bool cml_verbose; // Whether bash will output verbose target index of searching
  bool left;        // Follow left wall or right, true if left
  double radius;    // Look ahead distance for target
  double angle[NUM], reverse[NUM], search_angle[NUM];
  std::string MAP_FRAME = "/map";
  std::string ROBOT_FRAME = "/robot_base";

  // ROS
  ros::NodeHandle nh_, pnh_;
  ros::ServiceServer left_srv;
  ros::Subscriber sub_grid;
  ros::Subscriber sub_goal;
  ros::Publisher pub_path;
  ros::Publisher pub_marker;
  ros::Publisher pub_serach_arr;
  ros::Timer timer; // Timer to publish marker
  nav_msgs::OccupancyGrid grid;
  nav_msgs::MapMetaData mapMetaData;
  AStar::AStar planner;
  AStar::NODE_LIST res;
  Eigen::MatrixXd map;
  tf::Transform mat;
  visualization_msgs::Marker marker;
  // Callback for sub_goal
  void cbGoal(asv_msgs::RobotGoal msg){
    ros::Time START_TIME = ros::Time::now();
    res.clear();
    nav_msgs::Path planned_path;
    geometry_msgs::Pose msg_pose = msg.goal;
    convertFrame(mat, msg_pose);
    res = find_target(msg_pose.position.x, msg_pose.position.y);

    ros::Time END_TIME = ros::Time::now();
    if (res.empty()){
      return;
    }

    for (AStar::NODE_LIST::iterator it = res.begin(); it != res.end(); ++it)
    {
      geometry_msgs::PoseStamped ps = indice_to_pose(mapMetaData, it->get_x(), it->get_y());
      // If use_odom is true, we have to convert the pose back to odom frame
      if (use_odom)
        convertFrame(mat.inverse(), ps); // Have to convert back to fixed frame
      planned_path.poses.push_back(ps);
      if (verbose)
      {
        geometry_msgs::Point p = indice_to_point(mapMetaData, it->get_x(), it->get_y());
        if (use_odom)
          convertFrame(mat.inverse(), p); // Have to convert back to fixed frame
        marker.points.push_back(p);
        std_msgs::ColorRGBA c;
        c.r = 1.0f;
        c.a = 1.0f;
        marker.colors.push_back(c);
      }
    }
    ros::Time DONE_TIME = ros::Time::now();
    //std::cout << (DONE_TIME - END_TIME).toSec() << ", " << (END_TIME - START_TIME).toSec() << std::endl;
    planned_path.header.frame_id = (use_odom == true ? MAP_FRAME : ROBOT_FRAME);
    pub_path.publish(planned_path);
    if (verbose)
      pub_marker.publish(marker);
  }

  // Callback for sub_grid
  void cbMap(nav_msgs::OccupancyGrid msg)
  {
    ros::Time START_TIME = ros::Time::now();
    res.clear();
    nav_msgs::Path planned_path;
    mapMetaData = msg.info;
    map = Eigen::MatrixXd(mapMetaData.height, mapMetaData.width);
    if (count != timer_execution)
    {
      ++count;
      return;
    }
    else
    {
      count = 0;
      marker.points.clear();
      marker.colors.clear();
      if (cml_verbose)
        ROS_INFO("Counter set to 0.");
    }
    grid = msg;
    grid_to_matrix(msg, map);
    std::copy(std::begin(angle), std::end(angle), std::begin(search_angle));
    res = find_target();
    // Find reverse side
    if (res.empty())
    {
      if (wait_reverse_cnt < wait_threshold)
      {
        ROS_WARN("Wait for reverse: %d", wait_reverse_cnt);
        ros::Publisher pub_stop_cmd = nh_.advertise<std_msgs::Bool>("/husky/arrive", 1);
        std_msgs::Bool stop_cmd;
        stop_cmd.data = true;
        pub_stop_cmd.publish(stop_cmd);
        wait_reverse_cnt++;
        return;
      }
      //wait_reverse_cnt = 0;
      std::copy(std::begin(reverse), std::end(reverse), std::begin(search_angle));
      ++count_reverse;
      ROS_INFO("Reverse counter set to %d", count_reverse);

      res = find_target();

      // No path found
      if (res.empty())
      {
        ++stuck_counter;
        // Publish zero point if not found
        ROS_WARN("Not walkable for every searching position, stuck_counter is now: %d", stuck_counter);
        geometry_msgs::PoseStamped ps;
        planned_path.poses.clear();
        planned_path.poses.push_back(ps);
        planned_path.header.frame_id = (use_odom == true ? MAP_FRAME : ROBOT_FRAME);
        ros::Publisher pub_stop_cmd = nh_.advertise<std_msgs::Bool>("/husky/arrive", 1);
        std_msgs::Bool stop_cmd;
        stop_cmd.data = true;
        pub_stop_cmd.publish(stop_cmd);
        if (stuck_counter >= STUCK_MAX)
        { // Stuck too long time, stop and respawn node
          ROS_ERROR("Got stuck! Enter emergency stop mode...");
          ros::ServiceClient e_stop = nh_.serviceClient<std_srvs::SetBool>("/emergency_stop");
          std_srvs::SetBool e_stop_cmd;
          e_stop_cmd.request.data = true;
          e_stop.call(e_stop_cmd);
          return;
          /*
          // Publish zero point
          geometry_msgs::PoseStamped ps;
          planned_path.poses.clear();
          planned_path.poses.push_back(ps);
          planned_path.header.frame_id = (use_odom==true? MAP_FRAME: ROBOT_FRAME);
          pub_path.publish(planned_path);
          ros::Publisher pub_stop_cmd = nh_.advertise<std_msgs::Bool>("/husky/arrive", 1);
          std_msgs::Bool stop_cmd; stop_cmd.data=true; pub_stop_cmd.publish(stop_cmd);
          ros::shutdown();
          */
        } // End if
      }
      // Got a path with reverse side
      else
      {
        ROS_WARN("GOT OUT!!!");
        stuck_counter = 0;
        count_reverse = 0;
      }
    } // End if
    else
    {
      wait_reverse_cnt = 0;
      stuck_counter = 0;
      count_reverse = 0;
      //std::copy(std::begin(angle), std::end(angle), std::begin(search_angle));
    }

    ros::Time END_TIME = ros::Time::now();
    for (AStar::NODE_LIST::iterator it = res.begin(); it != res.end(); ++it)
    {
      geometry_msgs::PoseStamped ps = indice_to_pose(mapMetaData, it->get_x(), it->get_y());
      // If use_odom is true, we have to convert the pose back to odom frame
      if (use_odom)
        convertFrame(mat.inverse(), ps); // Have to convert back to fixed frame
      planned_path.poses.push_back(ps);
      if (verbose)
      {
        geometry_msgs::Point p = indice_to_point(mapMetaData, it->get_x(), it->get_y());
        if (use_odom)
          convertFrame(mat.inverse(), p); // Have to convert back to fixed frame
        marker.points.push_back(p);
        std_msgs::ColorRGBA c;
        c.r = 1.0f;
        c.a = 1.0f;
        marker.colors.push_back(c);
      }
    }
    ros::Time DONE_TIME = ros::Time::now();
    //std::cout << (DONE_TIME - END_TIME).toSec() << ", " << (END_TIME - START_TIME).toSec() << std::endl;
    planned_path.header.frame_id = (use_odom == true ? MAP_FRAME : ROBOT_FRAME);
    pub_path.publish(planned_path);
    if (verbose)
      pub_marker.publish(marker);
  }

  // Initial marker after constructed
  void initial_marker(visualization_msgs::Marker &marker)
  {
    marker.header.frame_id = (use_odom == true ? MAP_FRAME : ROBOT_FRAME); // Fixed frame, i.e., odom
    marker.header.stamp = ros::Time::now();
    marker.type = visualization_msgs::Marker::POINTS;
    marker.action = visualization_msgs::Marker::ADD;
    marker.pose.orientation.w = 1.0;
    marker.scale.x = 0.1;
    marker.scale.y = 0.1;
    marker.scale.z = 0.1;
  }

  // Try to find the walkable path
  AStar::NODE_LIST find_target(double x, double y) {
    AStar::NODE_LIST nl;
    //AStar::Node start(0, 0, NULL
    int idx_x, idx_y;
    pose_to_idx(mapMetaData, 0, 0, idx_x, idx_y);
    AStar::Node start(idx_y, idx_x, NULL); // Have to change xy order
    if (!pose_to_idx(mapMetaData, x, y, idx_x, idx_y))
      return nl;
    AStar::Node end(idx_y, idx_x, NULL); // Have to change xy order
    planner.initial(start, end, map);
    if (planner.plan(nl)) { // Find walkable path, exit for
      if (cml_verbose)
        ROS_INFO("[%s] Find walkable target, set pose to (%f, %f)", ros::this_node::getName().c_str(), x, y);
    }
    return nl;
  }

  // Try to find walkable target in the predefined searching points
  AStar::NODE_LIST find_target(void)
  {
    AStar::NODE_LIST nl;
    //AStar::Node start(0, 0, NULL);
    for (int i = 0; i < NUM; ++i)
    {
      int idx_x, idx_y;
      pose_to_idx(mapMetaData, 0, 0, idx_x, idx_y);
      AStar::Node start(idx_y, idx_x, NULL); // Have to change xy order
      double x = radius * cos(search_angle[i] * M_PI / 180.0),
             y = radius * sin(search_angle[i] * M_PI / 180.0);
      if (!pose_to_idx(mapMetaData, x, y, idx_x, idx_y))
        continue;
      AStar::Node end(idx_y, idx_x, NULL); // Have to change xy order
      planner.initial(start, end, map);
      if (planner.plan(nl))
      {
        if (cml_verbose)
          ROS_INFO("[%s] Find walkable target at index: %d, set pose to (%f, %f)", ros::this_node::getName().c_str(), i + 1, x, y);
        break; // Find walkable path, exit for
      }
    }
    return nl;
  }

  void pub_marker_arr_thread(const ros::TimerEvent &event)
  {
    visualization_msgs::MarkerArray marker_arr;
    // Initial marker array
    for (int i = 0; i < NUM; ++i)
    {
      visualization_msgs::Marker temp;
      temp.header.frame_id = ROBOT_FRAME;
      temp.id = i;
      temp.type = visualization_msgs::Marker::SPHERE;
      temp.action = visualization_msgs::Marker::ADD;
      temp.scale.x = temp.scale.y = temp.scale.z = 0.1;
      temp.color.b = temp.color.a = 1.0;
      temp.pose.position.x = radius * cos(search_angle[i] * M_PI / 180.0);
      temp.pose.position.y = radius * sin(search_angle[i] * M_PI / 180.0);
      temp.pose.orientation.w = 1.0;
      marker_arr.markers.push_back(temp);
    }
    pub_serach_arr.publish(marker_arr);
  }

  bool cbLeft(std_srvs::SetBool::Request &req, std_srvs::SetBool::Response &res)
  {
    bool is_left = req.data;
    res.success = true;
    res.message = "get srv";
    if (is_left)
    {
      search_left(true);
      ROS_INFO("SRV server: Left");
    }
    else
    {
      search_left(false);
      ROS_INFO("SRV server: Right");
    }
    return true;
  }

  void search_left(bool go_left)
  {
    if (go_left)
    {
      for (int i = 0; i < NUM; ++i)
        angle[i] = 60 - i * 135. / (NUM - 1); // Degree [60, -75]
      for (int i = 0; i < NUM; ++i)
        reverse[i] = -90 - i * 120. / (NUM - 1); // Degree [-90, -210]
    }
    else
    {
      for (int i = 0; i < NUM; ++i)
        angle[i] = -60 + i * 135. / (NUM - 1); // Degree [-60, 75]
      for (int i = 0; i < NUM; ++i)
        reverse[i] = 90 + i * 120. / (NUM - 1); // Degree [90, 210]
    }
    std::copy(std::begin(angle), std::end(angle), std::begin(search_angle));
  }

  void cbTimer(const ros::TimerEvent& event){
    printf("Timer\n");
    if(use_odom){
      tf::TransformListener listener;
      tf::StampedTransform transform;
      try{
        listener.waitForTransform(ROBOT_FRAME, MAP_FRAME, ros::Time(0), ros::Duration(1.0));
        listener.lookupTransform(ROBOT_FRAME, MAP_FRAME, ros::Time(0), transform);
      } catch(tf::TransformException ex) {ROS_ERROR("%s", ex.what());}
      mat = tf::Transform(transform.getRotation(), transform.getOrigin());
    }
    if(verbose) {
      pub_marker.publish(marker);
    } // End if
  }

public:
  ObstacleAvoidance(ros::NodeHandle nh, ros::NodeHandle pnh) : nh_(nh), pnh_(pnh), count(0), count_reverse(0), stuck_counter(0), wait_reverse_cnt(0)
  {
    // Subscriber and publisher
    sub_grid = pnh_.subscribe("/ASV/occupancy_grid", 1, &ObstacleAvoidance::cbMap, this);
    sub_goal = pnh_.subscribe("/ASV/robot_goal", 1, &ObstacleAvoidance::cbGoal, this);
    pub_path = pnh_.advertise<nav_msgs::Path>("planned_path", 1);
    left_srv = nh.advertiseService("/left_following", &ObstacleAvoidance::cbLeft, this);
    timer = pnh_.createTimer(ros::Duration(0.1), &ObstacleAvoidance::cbTimer, this);
    // Get parameters
    if (!pnh.getParam("robot_frame", ROBOT_FRAME))
      ROBOT_FRAME = "robot_base";
    if (!nh_.getParam("use_odom", use_odom))
    {
      use_odom = true;
      ROS_INFO("[%s] use_odom set to true", ros::this_node::getName().c_str());
    }
    if (!pnh_.getParam("verbose", verbose))
    {
      verbose = true;
      ROS_INFO("[%s] verbose set to true", ros::this_node::getName().c_str());
    }
    if (!pnh_.getParam("cml_verbose", cml_verbose))
    {
      cml_verbose = false;
      ROS_INFO("[%s] cml_verbose set to true", ros::this_node::getName().c_str());
    }
    if (!pnh_.getParam("left", left))
    {
      left = false;
      ROS_INFO("[%s] left set to true", ros::this_node::getName().c_str());
    }
    if (!pnh_.getParam("radius", radius))
    {
      radius = 3.;
      ROS_INFO("[%s] radius set to %f", ros::this_node::getName().c_str(), radius);
    }
    if (!pnh_.getParam("timer_execution", timer_execution))
    {
      timer_execution = 0;
      ROS_INFO("[%s] timer_execution set to %d", ros::this_node::getName().c_str(), timer_execution);
    }
    if (!pnh_.getParam("wait_threshold", wait_threshold))
    {
      wait_threshold = 3.;
      ROS_INFO("[%s] wait_threshold set to %f", ros::this_node::getName().c_str(), wait_threshold);
    }

    // Initial variables after get parameters
    if (left)
    {
      for (int i = 0; i < NUM; ++i)
        angle[i] = 60 - i * 135. / (NUM - 1); // Degree [60, -75]
      for (int i = 0; i < NUM; ++i)
        reverse[i] = -90 - i * 120. / (NUM - 1); // Degree [-90, -210]
    }
    else
    {
      for (int i = 0; i < NUM; ++i)
        angle[i] = -60 + i * 135. / (NUM - 1); // Degree [-60, 75]
      for (int i = 0; i < NUM; ++i)
        reverse[i] = 90 + i * 120. / (NUM - 1); // Degree [90, 210]
    }
    std::copy(std::begin(angle), std::end(angle), std::begin(search_angle));
    if (verbose)
    {
      pub_marker = pnh_.advertise<visualization_msgs::Marker>("marker", 1);
      initial_marker(marker);
      pub_serach_arr = pnh_.advertise<visualization_msgs::MarkerArray>("search_array", 1);
      // timer = pnh_.createTimer(ros::Duration(0.3), &ObstacleAvoidance::pub_marker_arr_thread, this);
    }
  }
};
