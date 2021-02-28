#ifndef _ROS_SERVICE_SetString_h
#define _ROS_SERVICE_SetString_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace asv_msgs
{

static const char SETSTRING[] = "asv_msgs/SetString";

  class SetStringRequest : public ros::Msg
  {
    public:
      typedef const char* _str_type;
      _str_type str;

    SetStringRequest():
      str("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t length_str = strlen(this->str);
      varToArr(outbuffer + offset, length_str);
      offset += 4;
      memcpy(outbuffer + offset, this->str, length_str);
      offset += length_str;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_str;
      arrToVar(length_str, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_str; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_str-1]=0;
      this->str = (char *)(inbuffer + offset-1);
      offset += length_str;
     return offset;
    }

    const char * getType(){ return SETSTRING; };
    const char * getMD5(){ return "994972b6e03928b2476860ce6c4c8e17"; };

  };

  class SetStringResponse : public ros::Msg
  {
    public:
      typedef bool _success_type;
      _success_type success;

    SetStringResponse():
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

    const char * getType(){ return SETSTRING; };
    const char * getMD5(){ return "358e233cde0c8a8bcfea4ce193f8fc15"; };

  };

  class SetString {
    public:
    typedef SetStringRequest Request;
    typedef SetStringResponse Response;
  };

}
#endif
