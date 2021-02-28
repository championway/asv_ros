#ifndef _ROS_rviz_cloud_annotation_UndoRedoState_h
#define _ROS_rviz_cloud_annotation_UndoRedoState_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace rviz_cloud_annotation
{

  class UndoRedoState : public ros::Msg
  {
    public:
      typedef bool _redo_enabled_type;
      _redo_enabled_type redo_enabled;
      typedef const char* _redo_description_type;
      _redo_description_type redo_description;
      typedef bool _undo_enabled_type;
      _undo_enabled_type undo_enabled;
      typedef const char* _undo_description_type;
      _undo_description_type undo_description;

    UndoRedoState():
      redo_enabled(0),
      redo_description(""),
      undo_enabled(0),
      undo_description("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_redo_enabled;
      u_redo_enabled.real = this->redo_enabled;
      *(outbuffer + offset + 0) = (u_redo_enabled.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->redo_enabled);
      uint32_t length_redo_description = strlen(this->redo_description);
      varToArr(outbuffer + offset, length_redo_description);
      offset += 4;
      memcpy(outbuffer + offset, this->redo_description, length_redo_description);
      offset += length_redo_description;
      union {
        bool real;
        uint8_t base;
      } u_undo_enabled;
      u_undo_enabled.real = this->undo_enabled;
      *(outbuffer + offset + 0) = (u_undo_enabled.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->undo_enabled);
      uint32_t length_undo_description = strlen(this->undo_description);
      varToArr(outbuffer + offset, length_undo_description);
      offset += 4;
      memcpy(outbuffer + offset, this->undo_description, length_undo_description);
      offset += length_undo_description;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_redo_enabled;
      u_redo_enabled.base = 0;
      u_redo_enabled.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->redo_enabled = u_redo_enabled.real;
      offset += sizeof(this->redo_enabled);
      uint32_t length_redo_description;
      arrToVar(length_redo_description, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_redo_description; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_redo_description-1]=0;
      this->redo_description = (char *)(inbuffer + offset-1);
      offset += length_redo_description;
      union {
        bool real;
        uint8_t base;
      } u_undo_enabled;
      u_undo_enabled.base = 0;
      u_undo_enabled.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->undo_enabled = u_undo_enabled.real;
      offset += sizeof(this->undo_enabled);
      uint32_t length_undo_description;
      arrToVar(length_undo_description, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_undo_description; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_undo_description-1]=0;
      this->undo_description = (char *)(inbuffer + offset-1);
      offset += length_undo_description;
     return offset;
    }

    const char * getType(){ return "rviz_cloud_annotation/UndoRedoState"; };
    const char * getMD5(){ return "43c106a96c078080d8c117fdd425c0a0"; };

  };

}
#endif