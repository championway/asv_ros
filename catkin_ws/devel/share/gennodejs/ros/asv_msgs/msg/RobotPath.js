// Auto-generated. Do not edit!

// (in-package asv_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class RobotPath {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.list = null;
      this.robot = null;
    }
    else {
      if (initObj.hasOwnProperty('list')) {
        this.list = initObj.list
      }
      else {
        this.list = [];
      }
      if (initObj.hasOwnProperty('robot')) {
        this.robot = initObj.robot
      }
      else {
        this.robot = new geometry_msgs.msg.Pose();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RobotPath
    // Serialize message field [list]
    // Serialize the length for message field [list]
    bufferOffset = _serializer.uint32(obj.list.length, buffer, bufferOffset);
    obj.list.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Pose.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [robot]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.robot, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RobotPath
    let len;
    let data = new RobotPath(null);
    // Deserialize message field [list]
    // Deserialize array length for message field [list]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.list = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.list[i] = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [robot]
    data.robot = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 56 * object.list.length;
    return length + 60;
  }

  static datatype() {
    // Returns string type for a message object
    return 'asv_msgs/RobotPath';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '26644de2debc53d8bba799cb1ae600b6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Pose[] list
    geometry_msgs/Pose robot
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RobotPath(null);
    if (msg.list !== undefined) {
      resolved.list = new Array(msg.list.length);
      for (let i = 0; i < resolved.list.length; ++i) {
        resolved.list[i] = geometry_msgs.msg.Pose.Resolve(msg.list[i]);
      }
    }
    else {
      resolved.list = []
    }

    if (msg.robot !== undefined) {
      resolved.robot = geometry_msgs.msg.Pose.Resolve(msg.robot)
    }
    else {
      resolved.robot = new geometry_msgs.msg.Pose()
    }

    return resolved;
    }
};

module.exports = RobotPath;
