#ifndef _ROS_asv_msgs_RobotPath_h
#define _ROS_asv_msgs_RobotPath_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "asv_msgs/WayPoint.h"
#include "geometry_msgs/Pose.h"

namespace asv_msgs
{

  class RobotPath : public ros::Msg
  {
    public:
      uint32_t list_length;
      typedef asv_msgs::WayPoint _list_type;
      _list_type st_list;
      _list_type * list;
      typedef geometry_msgs::Pose _robot_type;
      _robot_type robot;

    RobotPath():
      list_length(0), list(NULL),
      robot()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->list_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->list_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->list_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->list_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->list_length);
      for( uint32_t i = 0; i < list_length; i++){
      offset += this->list[i].serialize(outbuffer + offset);
      }
      offset += this->robot.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t list_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      list_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      list_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      list_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->list_length);
      if(list_lengthT > list_length)
        this->list = (asv_msgs::WayPoint*)realloc(this->list, list_lengthT * sizeof(asv_msgs::WayPoint));
      list_length = list_lengthT;
      for( uint32_t i = 0; i < list_length; i++){
      offset += this->st_list.deserialize(inbuffer + offset);
        memcpy( &(this->list[i]), &(this->st_list), sizeof(asv_msgs::WayPoint));
      }
      offset += this->robot.deserialize(inbuffer + offset);
     return offset;
    }

    const char * getType(){ return "asv_msgs/RobotPath"; };
    const char * getMD5(){ return "c920aa12515b285cd278c2db86a84a9b"; };

  };

}
#endif