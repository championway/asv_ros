#ifndef _ROS_rviz_cloud_annotation_RectangleSelectionViewport_h
#define _ROS_rviz_cloud_annotation_RectangleSelectionViewport_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "geometry_msgs/Pose.h"

namespace rviz_cloud_annotation
{

  class RectangleSelectionViewport : public ros::Msg
  {
    public:
      typedef uint32_t _start_x_type;
      _start_x_type start_x;
      typedef uint32_t _start_y_type;
      _start_y_type start_y;
      typedef uint32_t _end_x_type;
      _end_x_type end_x;
      typedef uint32_t _end_y_type;
      _end_y_type end_y;
      typedef uint32_t _viewport_height_type;
      _viewport_height_type viewport_height;
      typedef uint32_t _viewport_width_type;
      _viewport_width_type viewport_width;
      typedef float _focal_length_type;
      _focal_length_type focal_length;
      float projection_matrix[16];
      typedef geometry_msgs::Pose _camera_pose_type;
      _camera_pose_type camera_pose;
      typedef bool _is_deep_selection_type;
      _is_deep_selection_type is_deep_selection;
      uint32_t polyline_x_length;
      typedef int32_t _polyline_x_type;
      _polyline_x_type st_polyline_x;
      _polyline_x_type * polyline_x;
      uint32_t polyline_y_length;
      typedef int32_t _polyline_y_type;
      _polyline_y_type st_polyline_y;
      _polyline_y_type * polyline_y;

    RectangleSelectionViewport():
      start_x(0),
      start_y(0),
      end_x(0),
      end_y(0),
      viewport_height(0),
      viewport_width(0),
      focal_length(0),
      projection_matrix(),
      camera_pose(),
      is_deep_selection(0),
      polyline_x_length(0), polyline_x(NULL),
      polyline_y_length(0), polyline_y(NULL)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->start_x >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->start_x >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->start_x >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->start_x >> (8 * 3)) & 0xFF;
      offset += sizeof(this->start_x);
      *(outbuffer + offset + 0) = (this->start_y >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->start_y >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->start_y >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->start_y >> (8 * 3)) & 0xFF;
      offset += sizeof(this->start_y);
      *(outbuffer + offset + 0) = (this->end_x >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->end_x >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->end_x >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->end_x >> (8 * 3)) & 0xFF;
      offset += sizeof(this->end_x);
      *(outbuffer + offset + 0) = (this->end_y >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->end_y >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->end_y >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->end_y >> (8 * 3)) & 0xFF;
      offset += sizeof(this->end_y);
      *(outbuffer + offset + 0) = (this->viewport_height >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->viewport_height >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->viewport_height >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->viewport_height >> (8 * 3)) & 0xFF;
      offset += sizeof(this->viewport_height);
      *(outbuffer + offset + 0) = (this->viewport_width >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->viewport_width >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->viewport_width >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->viewport_width >> (8 * 3)) & 0xFF;
      offset += sizeof(this->viewport_width);
      union {
        float real;
        uint32_t base;
      } u_focal_length;
      u_focal_length.real = this->focal_length;
      *(outbuffer + offset + 0) = (u_focal_length.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_focal_length.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_focal_length.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_focal_length.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->focal_length);
      for( uint32_t i = 0; i < 16; i++){
      union {
        float real;
        uint32_t base;
      } u_projection_matrixi;
      u_projection_matrixi.real = this->projection_matrix[i];
      *(outbuffer + offset + 0) = (u_projection_matrixi.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_projection_matrixi.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_projection_matrixi.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_projection_matrixi.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->projection_matrix[i]);
      }
      offset += this->camera_pose.serialize(outbuffer + offset);
      union {
        bool real;
        uint8_t base;
      } u_is_deep_selection;
      u_is_deep_selection.real = this->is_deep_selection;
      *(outbuffer + offset + 0) = (u_is_deep_selection.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->is_deep_selection);
      *(outbuffer + offset + 0) = (this->polyline_x_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->polyline_x_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->polyline_x_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->polyline_x_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->polyline_x_length);
      for( uint32_t i = 0; i < polyline_x_length; i++){
      union {
        int32_t real;
        uint32_t base;
      } u_polyline_xi;
      u_polyline_xi.real = this->polyline_x[i];
      *(outbuffer + offset + 0) = (u_polyline_xi.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_polyline_xi.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_polyline_xi.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_polyline_xi.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->polyline_x[i]);
      }
      *(outbuffer + offset + 0) = (this->polyline_y_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->polyline_y_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->polyline_y_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->polyline_y_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->polyline_y_length);
      for( uint32_t i = 0; i < polyline_y_length; i++){
      union {
        int32_t real;
        uint32_t base;
      } u_polyline_yi;
      u_polyline_yi.real = this->polyline_y[i];
      *(outbuffer + offset + 0) = (u_polyline_yi.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_polyline_yi.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_polyline_yi.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_polyline_yi.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->polyline_y[i]);
      }
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->start_x =  ((uint32_t) (*(inbuffer + offset)));
      this->start_x |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->start_x |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->start_x |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      offset += sizeof(this->start_x);
      this->start_y =  ((uint32_t) (*(inbuffer + offset)));
      this->start_y |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->start_y |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->start_y |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      offset += sizeof(this->start_y);
      this->end_x =  ((uint32_t) (*(inbuffer + offset)));
      this->end_x |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->end_x |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->end_x |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      offset += sizeof(this->end_x);
      this->end_y =  ((uint32_t) (*(inbuffer + offset)));
      this->end_y |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->end_y |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->end_y |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      offset += sizeof(this->end_y);
      this->viewport_height =  ((uint32_t) (*(inbuffer + offset)));
      this->viewport_height |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->viewport_height |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->viewport_height |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      offset += sizeof(this->viewport_height);
      this->viewport_width =  ((uint32_t) (*(inbuffer + offset)));
      this->viewport_width |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->viewport_width |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->viewport_width |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      offset += sizeof(this->viewport_width);
      union {
        float real;
        uint32_t base;
      } u_focal_length;
      u_focal_length.base = 0;
      u_focal_length.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_focal_length.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_focal_length.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_focal_length.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->focal_length = u_focal_length.real;
      offset += sizeof(this->focal_length);
      for( uint32_t i = 0; i < 16; i++){
      union {
        float real;
        uint32_t base;
      } u_projection_matrixi;
      u_projection_matrixi.base = 0;
      u_projection_matrixi.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_projection_matrixi.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_projection_matrixi.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_projection_matrixi.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->projection_matrix[i] = u_projection_matrixi.real;
      offset += sizeof(this->projection_matrix[i]);
      }
      offset += this->camera_pose.deserialize(inbuffer + offset);
      union {
        bool real;
        uint8_t base;
      } u_is_deep_selection;
      u_is_deep_selection.base = 0;
      u_is_deep_selection.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->is_deep_selection = u_is_deep_selection.real;
      offset += sizeof(this->is_deep_selection);
      uint32_t polyline_x_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      polyline_x_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      polyline_x_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      polyline_x_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->polyline_x_length);
      if(polyline_x_lengthT > polyline_x_length)
        this->polyline_x = (int32_t*)realloc(this->polyline_x, polyline_x_lengthT * sizeof(int32_t));
      polyline_x_length = polyline_x_lengthT;
      for( uint32_t i = 0; i < polyline_x_length; i++){
      union {
        int32_t real;
        uint32_t base;
      } u_st_polyline_x;
      u_st_polyline_x.base = 0;
      u_st_polyline_x.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_st_polyline_x.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_st_polyline_x.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_st_polyline_x.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->st_polyline_x = u_st_polyline_x.real;
      offset += sizeof(this->st_polyline_x);
        memcpy( &(this->polyline_x[i]), &(this->st_polyline_x), sizeof(int32_t));
      }
      uint32_t polyline_y_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      polyline_y_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      polyline_y_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      polyline_y_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->polyline_y_length);
      if(polyline_y_lengthT > polyline_y_length)
        this->polyline_y = (int32_t*)realloc(this->polyline_y, polyline_y_lengthT * sizeof(int32_t));
      polyline_y_length = polyline_y_lengthT;
      for( uint32_t i = 0; i < polyline_y_length; i++){
      union {
        int32_t real;
        uint32_t base;
      } u_st_polyline_y;
      u_st_polyline_y.base = 0;
      u_st_polyline_y.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_st_polyline_y.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_st_polyline_y.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_st_polyline_y.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->st_polyline_y = u_st_polyline_y.real;
      offset += sizeof(this->st_polyline_y);
        memcpy( &(this->polyline_y[i]), &(this->st_polyline_y), sizeof(int32_t));
      }
     return offset;
    }

    const char * getType(){ return "rviz_cloud_annotation/RectangleSelectionViewport"; };
    const char * getMD5(){ return "6a3c9a6075ac79ec934409411b5e99c9"; };

  };

}
#endif