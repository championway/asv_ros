#include "obstacle_avoidance.hpp"

int main(int argc, char** argv)
{
  ros::init(argc, argv, "obstacle_avoidance");
  ros::NodeHandle nh, pnh("~");
  ObstacleAvoidance wf(nh, pnh);
  while(ros::ok()) ros::spinOnce();
  return 0;
}
