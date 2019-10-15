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

class RobotGoal {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.goal = null;
      this.robot = null;
    }
    else {
      if (initObj.hasOwnProperty('goal')) {
        this.goal = initObj.goal
      }
      else {
        this.goal = new geometry_msgs.msg.Pose();
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
    // Serializes a message object of type RobotGoal
    // Serialize message field [goal]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.goal, buffer, bufferOffset);
    // Serialize message field [robot]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.robot, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RobotGoal
    let len;
    let data = new RobotGoal(null);
    // Deserialize message field [goal]
    data.goal = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    // Deserialize message field [robot]
    data.robot = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 112;
  }

  static datatype() {
    // Returns string type for a message object
    return 'asv_msgs/RobotGoal';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '98c7ffdb4ffaa1a7d09b7aef3442e3f1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Pose goal
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
    const resolved = new RobotGoal(null);
    if (msg.goal !== undefined) {
      resolved.goal = geometry_msgs.msg.Pose.Resolve(msg.goal)
    }
    else {
      resolved.goal = new geometry_msgs.msg.Pose()
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

module.exports = RobotGoal;
