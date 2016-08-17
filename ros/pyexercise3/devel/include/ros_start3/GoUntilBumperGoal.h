// Generated by gencpp from file ros_start3/GoUntilBumperGoal.msg
// DO NOT EDIT!


#ifndef ROS_START3_MESSAGE_GOUNTILBUMPERGOAL_H
#define ROS_START3_MESSAGE_GOUNTILBUMPERGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/Twist.h>

namespace ros_start3
{
template <class ContainerAllocator>
struct GoUntilBumperGoal_
{
  typedef GoUntilBumperGoal_<ContainerAllocator> Type;

  GoUntilBumperGoal_()
    : target_vel()
    , timeout_sec(0)  {
    }
  GoUntilBumperGoal_(const ContainerAllocator& _alloc)
    : target_vel(_alloc)
    , timeout_sec(0)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::Twist_<ContainerAllocator>  _target_vel_type;
  _target_vel_type target_vel;

   typedef int32_t _timeout_sec_type;
  _timeout_sec_type timeout_sec;




  typedef boost::shared_ptr< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> const> ConstPtr;

}; // struct GoUntilBumperGoal_

typedef ::ros_start3::GoUntilBumperGoal_<std::allocator<void> > GoUntilBumperGoal;

typedef boost::shared_ptr< ::ros_start3::GoUntilBumperGoal > GoUntilBumperGoalPtr;
typedef boost::shared_ptr< ::ros_start3::GoUntilBumperGoal const> GoUntilBumperGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ros_start3

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/indigo/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'ros_start3': ['/home/jsupratman13/github/workspace/ros/pyexercise3/devel/share/ros_start3/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c9b5f8f2aced60d6e82fa76ca79b621a";
  }

  static const char* value(const ::ros_start3::GoUntilBumperGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc9b5f8f2aced60d6ULL;
  static const uint64_t static_value2 = 0xe82fa76ca79b621aULL;
};

template<class ContainerAllocator>
struct DataType< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ros_start3/GoUntilBumperGoal";
  }

  static const char* value(const ::ros_start3::GoUntilBumperGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
geometry_msgs/Twist target_vel\n\
int32 timeout_sec\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Twist\n\
# This expresses velocity in free space broken into its linear and angular parts.\n\
Vector3  linear\n\
Vector3  angular\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
# It is only meant to represent a direction. Therefore, it does not\n\
# make sense to apply a translation to it (e.g., when applying a \n\
# generic rigid transformation to a Vector3, tf2 will only apply the\n\
# rotation). If you want your data to be translatable too, use the\n\
# geometry_msgs/Point message instead.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const ::ros_start3::GoUntilBumperGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.target_vel);
      stream.next(m.timeout_sec);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GoUntilBumperGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ros_start3::GoUntilBumperGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ros_start3::GoUntilBumperGoal_<ContainerAllocator>& v)
  {
    s << indent << "target_vel: ";
    s << std::endl;
    Printer< ::geometry_msgs::Twist_<ContainerAllocator> >::stream(s, indent + "  ", v.target_vel);
    s << indent << "timeout_sec: ";
    Printer<int32_t>::stream(s, indent + "  ", v.timeout_sec);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROS_START3_MESSAGE_GOUNTILBUMPERGOAL_H