#ifndef _ROS_asv_msgs_MotorCmd_h
#define _ROS_asv_msgs_MotorCmd_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "std_msgs/Header.h"

namespace asv_msgs
{

  class MotorCmd : public ros::Msg
  {
    public:
      typedef std_msgs::Header _header_type;
      _header_type header;
      typedef float _left_type;
      _left_type left;
      typedef float _right_type;
      _right_type right;
      typedef float _horizontal_type;
      _horizontal_type horizontal;
      typedef float _front_type;
      _front_type front;

    MotorCmd():
      header(),
      left(0),
      right(0),
      horizontal(0),
      front(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->header.serialize(outbuffer + offset);
      union {
        float real;
        uint32_t base;
      } u_left;
      u_left.real = this->left;
      *(outbuffer + offset + 0) = (u_left.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_left.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_left.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_left.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->left);
      union {
        float real;
        uint32_t base;
      } u_right;
      u_right.real = this->right;
      *(outbuffer + offset + 0) = (u_right.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_right.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_right.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_right.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->right);
      union {
        float real;
        uint32_t base;
      } u_horizontal;
      u_horizontal.real = this->horizontal;
      *(outbuffer + offset + 0) = (u_horizontal.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_horizontal.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_horizontal.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_horizontal.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->horizontal);
      union {
        float real;
        uint32_t base;
      } u_front;
      u_front.real = this->front;
      *(outbuffer + offset + 0) = (u_front.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_front.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_front.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_front.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->front);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->header.deserialize(inbuffer + offset);
      union {
        float real;
        uint32_t base;
      } u_left;
      u_left.base = 0;
      u_left.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_left.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_left.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_left.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->left = u_left.real;
      offset += sizeof(this->left);
      union {
        float real;
        uint32_t base;
      } u_right;
      u_right.base = 0;
      u_right.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_right.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_right.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_right.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->right = u_right.real;
      offset += sizeof(this->right);
      union {
        float real;
        uint32_t base;
      } u_horizontal;
      u_horizontal.base = 0;
      u_horizontal.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_horizontal.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_horizontal.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_horizontal.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->horizontal = u_horizontal.real;
      offset += sizeof(this->horizontal);
      union {
        float real;
        uint32_t base;
      } u_front;
      u_front.base = 0;
      u_front.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_front.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_front.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_front.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->front = u_front.real;
      offset += sizeof(this->front);
     return offset;
    }

    const char * getType(){ return "asv_msgs/MotorCmd"; };
    const char * getMD5(){ return "4a8f4dd8c4a2266928b94573a25d3ad9"; };

  };

}
#endif