// Generated by gencpp from file duckiepond/Motor4Cmd.msg
// DO NOT EDIT!


#ifndef DUCKIEPOND_MESSAGE_MOTOR4CMD_H
#define DUCKIEPOND_MESSAGE_MOTOR4CMD_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace duckiepond
{
template <class ContainerAllocator>
struct Motor4Cmd_
{
  typedef Motor4Cmd_<ContainerAllocator> Type;

  Motor4Cmd_()
    : header()
    , lf(0.0)
    , rf(0.0)
    , lr(0.0)
    , rr(0.0)  {
    }
  Motor4Cmd_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , lf(0.0)
    , rf(0.0)
    , lr(0.0)
    , rr(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef float _lf_type;
  _lf_type lf;

   typedef float _rf_type;
  _rf_type rf;

   typedef float _lr_type;
  _lr_type lr;

   typedef float _rr_type;
  _rr_type rr;





  typedef boost::shared_ptr< ::duckiepond::Motor4Cmd_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::duckiepond::Motor4Cmd_<ContainerAllocator> const> ConstPtr;

}; // struct Motor4Cmd_

typedef ::duckiepond::Motor4Cmd_<std::allocator<void> > Motor4Cmd;

typedef boost::shared_ptr< ::duckiepond::Motor4Cmd > Motor4CmdPtr;
typedef boost::shared_ptr< ::duckiepond::Motor4Cmd const> Motor4CmdConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::duckiepond::Motor4Cmd_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::duckiepond::Motor4Cmd_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace duckiepond

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'sensor_msgs': ['/opt/ros/melodic/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg'], 'duckiepond': ['/home/arg/asv_ros/catkin_ws/src/duckiepond/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::duckiepond::Motor4Cmd_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::duckiepond::Motor4Cmd_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::duckiepond::Motor4Cmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::duckiepond::Motor4Cmd_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::duckiepond::Motor4Cmd_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::duckiepond::Motor4Cmd_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::duckiepond::Motor4Cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "77d80b96b13055bc97b62acface81cb7";
  }

  static const char* value(const ::duckiepond::Motor4Cmd_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x77d80b96b13055bcULL;
  static const uint64_t static_value2 = 0x97b62acface81cb7ULL;
};

template<class ContainerAllocator>
struct DataType< ::duckiepond::Motor4Cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "duckiepond/Motor4Cmd";
  }

  static const char* value(const ::duckiepond::Motor4Cmd_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::duckiepond::Motor4Cmd_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Thrust command - typically ranges from {-1.0 - 1.0}\n"
"Header header\n"
"float32 lf\n"
"float32 rf\n"
"float32 lr\n"
"float32 rr\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::duckiepond::Motor4Cmd_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::duckiepond::Motor4Cmd_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.lf);
      stream.next(m.rf);
      stream.next(m.lr);
      stream.next(m.rr);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Motor4Cmd_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::duckiepond::Motor4Cmd_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::duckiepond::Motor4Cmd_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "lf: ";
    Printer<float>::stream(s, indent + "  ", v.lf);
    s << indent << "rf: ";
    Printer<float>::stream(s, indent + "  ", v.rf);
    s << indent << "lr: ";
    Printer<float>::stream(s, indent + "  ", v.lr);
    s << indent << "rr: ";
    Printer<float>::stream(s, indent + "  ", v.rr);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DUCKIEPOND_MESSAGE_MOTOR4CMD_H
