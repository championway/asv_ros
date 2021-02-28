#ifndef _ROS_SERVICE_SetRobotPath_h
#define _ROS_SERVICE_SetRobotPath_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "asv_msgs/RobotPath.h"

namespace asv_msgs
{

static const char SETROBOTPATH[] = "asv_msgs/SetRobotPath";

  class SetRobotPathRequest : public ros::Msg
  {
    public:
      typedef asv_msgs::RobotPath _data_type;
      _data_type data;

    SetRobotPathRequest():
      data()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->data.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->data.deserialize(inbuffer + offset);
     return offset;
    }

    const char * getType(){ return SETROBOTPATH; };
    const char * getMD5(){ return "5fdc7d7d67cfce8d99517e77cdbbe1be"; };

  };

  class SetRobotPathResponse : public ros::Msg
  {
    public:
      typedef bool _success_type;
      _success_type success;

    SetRobotPathResponse():
      success(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_success;
      u_success.real = this->success;
      *(outbuffer + offset + 0) = (u_success.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->success);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_success;
      u_success.base = 0;
      u_success.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->success = u_success.real;
      offset += sizeof(this->success);
     return offset;
    }

    const char * getType(){ return SETROBOTPATH; };
    const char * getMD5(){ return "358e233cde0c8a8bcfea4ce193f8fc15"; };

  };

  class SetRobotPath {
    public:
    typedef SetRobotPathRequest Request;
    typedef SetRobotPathResponse Response;
  };

}
#endif
