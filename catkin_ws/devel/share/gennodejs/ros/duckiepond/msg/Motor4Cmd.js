// Auto-generated. Do not edit!

// (in-package duckiepond.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Motor4Cmd {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.lf = null;
      this.rf = null;
      this.lr = null;
      this.rr = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('lf')) {
        this.lf = initObj.lf
      }
      else {
        this.lf = 0.0;
      }
      if (initObj.hasOwnProperty('rf')) {
        this.rf = initObj.rf
      }
      else {
        this.rf = 0.0;
      }
      if (initObj.hasOwnProperty('lr')) {
        this.lr = initObj.lr
      }
      else {
        this.lr = 0.0;
      }
      if (initObj.hasOwnProperty('rr')) {
        this.rr = initObj.rr
      }
      else {
        this.rr = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Motor4Cmd
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [lf]
    bufferOffset = _serializer.float32(obj.lf, buffer, bufferOffset);
    // Serialize message field [rf]
    bufferOffset = _serializer.float32(obj.rf, buffer, bufferOffset);
    // Serialize message field [lr]
    bufferOffset = _serializer.float32(obj.lr, buffer, bufferOffset);
    // Serialize message field [rr]
    bufferOffset = _serializer.float32(obj.rr, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Motor4Cmd
    let len;
    let data = new Motor4Cmd(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [lf]
    data.lf = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [rf]
    data.rf = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [lr]
    data.lr = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [rr]
    data.rr = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'duckiepond/Motor4Cmd';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '77d80b96b13055bc97b62acface81cb7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Thrust command - typically ranges from {-1.0 - 1.0}
    Header header
    float32 lf
    float32 rf
    float32 lr
    float32 rr
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Motor4Cmd(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.lf !== undefined) {
      resolved.lf = msg.lf;
    }
    else {
      resolved.lf = 0.0
    }

    if (msg.rf !== undefined) {
      resolved.rf = msg.rf;
    }
    else {
      resolved.rf = 0.0
    }

    if (msg.lr !== undefined) {
      resolved.lr = msg.lr;
    }
    else {
      resolved.lr = 0.0
    }

    if (msg.rr !== undefined) {
      resolved.rr = msg.rr;
    }
    else {
      resolved.rr = 0.0
    }

    return resolved;
    }
};

module.exports = Motor4Cmd;
