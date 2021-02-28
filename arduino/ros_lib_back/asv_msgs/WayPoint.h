#ifndef _ROS_asv_msgs_WayPoint_h
#define _ROS_asv_msgs_WayPoint_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "geometry_msgs/Pose.h"
#include "std_msgs/Bool.h"
#include "std_msgs/Float32.h"

namespace asv_msgs
{

  class WayPoint : public ros::Msg
  {
    public:
      typedef geometry_msgs::Pose _waypoint_type;
      _waypoint_type waypoint;
      typedef std_msgs::Bool _bridge_start_type;
      _bridge_start_type bridge_start;
      typedef std_msgs::Bool _bridge_end_type;
      _bridge_end_type bridge_end;
      typedef std_msgs::Float32 _stop_time_type;
      _stop_time_type stop_time;

    WayPoint():
      waypoint(),
      bridge_start(),
      bridge_end(),
      stop_time()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->waypoint.serialize(outbuffer + offset);
      offset += this->bridge_start.serialize(outbuffer + offset);
      offset += this->bridge_end.serialize(outbuffer + offset);
      offset += this->stop_time.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->waypoint.deserialize(inbuffer + offset);
      offset += this->bridge_start.deserialize(inbuffer + offset);
      offset += this->bridge_end.deserialize(inbuffer + offset);
      offset += this->stop_time.deserialize(inbuffer + offset);
     return offset;
    }

    const char * getType(){ return "asv_msgs/WayPoint"; };
    const char * getMD5(){ return "65297cb2f98385b8cadd5f088028013d"; };

  };

}
#endif