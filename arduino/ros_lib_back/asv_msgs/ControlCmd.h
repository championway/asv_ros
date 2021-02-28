#ifndef _ROS_asv_msgs_ControlCmd_h
#define _ROS_asv_msgs_ControlCmd_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "std_msgs/Header.h"

namespace asv_msgs
{

  class ControlCmd : public ros::Msg
  {
    public:
      typedef std_msgs::Header _header_type;
      _header_type header;
      typedef float _right_type;
      _right_type right;
      typedef float _forward_type;
      _forward_type forward;
      typedef float _up_type;
      _up_type up;
      typedef bool _estop_type;
      _estop_type estop;
      typedef bool _manual_type;
      _manual_type manual;
      typedef bool _navigate_type;
      _navigate_type navigate;
      typedef bool _useVJoystick_type;
      _useVJoystick_type useVJoystick;

    ControlCmd():
      header(),
      right(0),
      forward(0),
      up(0),
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
      } u_forward;
      u_forward.real = this->forward;
      *(outbuffer + offset + 0) = (u_forward.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_forward.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_forward.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_forward.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->forward);
      union {
        float real;
        uint32_t base;
      } u_up;
      u_up.real = this->up;
      *(outbuffer + offset + 0) = (u_up.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_up.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_up.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_up.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->up);
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
      } u_forward;
      u_forward.base = 0;
      u_forward.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_forward.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_forward.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_forward.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->forward = u_forward.real;
      offset += sizeof(this->forward);
      union {
        float real;
        uint32_t base;
      } u_up;
      u_up.base = 0;
      u_up.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_up.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_up.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_up.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->up = u_up.real;
      offset += sizeof(this->up);
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

    const char * getType(){ return "asv_msgs/ControlCmd"; };
    const char * getMD5(){ return "2121b4a8cbf4ad30405991fcf9053c7d"; };

  };

}
#endif