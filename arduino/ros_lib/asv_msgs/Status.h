#ifndef _ROS_asv_msgs_Status_h
#define _ROS_asv_msgs_Status_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "std_msgs/Header.h"

namespace asv_msgs
{

  class Status : public ros::Msg
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
      typedef float _vertical_type;
      _vertical_type vertical;
      typedef bool _estop_type;
      _estop_type estop;
      typedef bool _manual_type;
      _manual_type manual;
      typedef bool _navigate_type;
      _navigate_type navigate;
      typedef bool _useVJoystick_type;
      _useVJoystick_type useVJoystick;

    Status():
      header(),
      left(0),
      right(0),
      horizontal(0),
      vertical(0),
      estop(0),
      manual(0),
      navigate(0),
      useVJoystick(0)
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
      } u_vertical;
      u_vertical.real = this->vertical;
      *(outbuffer + offset + 0) = (u_vertical.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_vertical.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_vertical.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_vertical.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->vertical);
      union {
        bool real;
        uint8_t base;
      } u_estop;
      u_estop.real = this->estop;
      *(outbuffer + offset + 0) = (u_estop.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->estop);
      union {
        bool real;
        uint8_t base;
      } u_manual;
      u_manual.real = this->manual;
      *(outbuffer + offset + 0) = (u_manual.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->manual);
      union {
        bool real;
        uint8_t base;
      } u_navigate;
      u_navigate.real = this->navigate;
      *(outbuffer + offset + 0) = (u_navigate.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->navigate);
      union {
        bool real;
        uint8_t base;
      } u_useVJoystick;
      u_useVJoystick.real = this->useVJoystick;
      *(outbuffer + offset + 0) = (u_useVJoystick.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->useVJoystick);
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
      } u_vertical;
      u_vertical.base = 0;
      u_vertical.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_vertical.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_vertical.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_vertical.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->vertical = u_vertical.real;
      offset += sizeof(this->vertical);
      union {
        bool real;
        uint8_t base;
      } u_estop;
      u_estop.base = 0;
      u_estop.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->estop = u_estop.real;
      offset += sizeof(this->estop);
      union {
        bool real;
        uint8_t base;
      } u_manual;
      u_manual.base = 0;
      u_manual.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->manual = u_manual.real;
      offset += sizeof(this->manual);
      union {
        bool real;
        uint8_t base;
      } u_navigate;
      u_navigate.base = 0;
      u_navigate.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->navigate = u_navigate.real;
      offset += sizeof(this->navigate);
      union {
        bool real;
        uint8_t base;
      } u_useVJoystick;
      u_useVJoystick.base = 0;
      u_useVJoystick.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->useVJoystick = u_useVJoystick.real;
      offset += sizeof(this->useVJoystick);
     return offset;
    }

    const char * getType(){ return "asv_msgs/Status"; };
    const char * getMD5(){ return "0e0f55809859e6ddc19e77cc75280eba"; };

  };

}
#endif