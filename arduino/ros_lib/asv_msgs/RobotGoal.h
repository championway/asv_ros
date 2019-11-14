#ifndef _ROS_asv_msgs_RobotGoal_h
#define _ROS_asv_msgs_RobotGoal_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "geometry_msgs/Pose.h"
#include "std_msgs/Bool.h"

namespace asv_msgs
{

  class RobotGoal : public ros::Msg
  {
    public:
      typedef geometry_msgs::Pose _goal_type;
      _goal_type goal;
      typedef geometry_msgs::Pose _robot_type;
      _robot_type robot;
      typedef std_msgs::Bool _only_angle_type;
      _only_angle_type only_angle;

    RobotGoal():
      goal(),
      robot(),
      only_angle()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->goal.serialize(outbuffer + offset);
      offset += this->robot.serialize(outbuffer + offset);
      offset += this->only_angle.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->goal.deserialize(inbuffer + offset);
      offset += this->robot.deserialize(inbuffer + offset);
      offset += this->only_angle.deserialize(inbuffer + offset);
     return offset;
    }

    const char * getType(){ return "asv_msgs/RobotGoal"; };
    const char * getMD5(){ return "4c8cc83ce83d88ad6d752b474b287b17"; };

  };

}
#endif