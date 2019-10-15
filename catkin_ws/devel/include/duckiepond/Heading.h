// Generated by gencpp from file duckiepond/Heading.msg
// DO NOT EDIT!


#ifndef DUCKIEPOND_MESSAGE_HEADING_H
#define DUCKIEPOND_MESSAGE_HEADING_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace duckiepond
{
template <class ContainerAllocator>
struct Heading_
{
  typedef Heading_<ContainerAllocator> Type;

  Heading_()
    : phi(0.0)
    , speed(0.0)  {
    }
  Heading_(const ContainerAllocator& _alloc)
    : phi(0.0)
    , speed(0.0)  {
  (void)_alloc;
    }



   typedef float _phi_type;
  _phi_type phi;

   typedef float _speed_type;
  _speed_type speed;





  typedef boost::shared_ptr< ::duckiepond::Heading_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::duckiepond::Heading_<ContainerAllocator> const> ConstPtr;

}; // struct Heading_

typedef ::duckiepond::Heading_<std::allocator<void> > Heading;

typedef boost::shared_ptr< ::duckiepond::Heading > HeadingPtr;
typedef boost::shared_ptr< ::duckiepond::Heading const> HeadingConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::duckiepond::Heading_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::duckiepond::Heading_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace duckiepond

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'sensor_msgs': ['/opt/ros/melodic/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg'], 'duckiepond': ['/home/arg/asv_ros/catkin_ws/src/duckiepond/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::duckiepond::Heading_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::duckiepond::Heading_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::duckiepond::Heading_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::duckiepond::Heading_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::duckiepond::Heading_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::duckiepond::Heading_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::duckiepond::Heading_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8fe8a91eef3de9ae7860b3f07a1529db";
  }

  static const char* value(const ::duckiepond::Heading_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8fe8a91eef3de9aeULL;
  static const uint64_t static_value2 = 0x7860b3f07a1529dbULL;
};

template<class ContainerAllocator>
struct DataType< ::duckiepond::Heading_<ContainerAllocator> >
{
  static const char* value()
  {
    return "duckiepond/Heading";
  }

  static const char* value(const ::duckiepond::Heading_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::duckiepond::Heading_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 phi\n"
"float32 speed\n"
;
  }

  static const char* value(const ::duckiepond::Heading_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::duckiepond::Heading_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.phi);
      stream.next(m.speed);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Heading_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::duckiepond::Heading_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::duckiepond::Heading_<ContainerAllocator>& v)
  {
    s << indent << "phi: ";
    Printer<float>::stream(s, indent + "  ", v.phi);
    s << indent << "speed: ";
    Printer<float>::stream(s, indent + "  ", v.speed);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DUCKIEPOND_MESSAGE_HEADING_H