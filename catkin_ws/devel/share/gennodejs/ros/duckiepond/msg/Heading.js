// Auto-generated. Do not edit!

// (in-package duckiepond.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Heading {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.phi = null;
      this.speed = null;
    }
    else {
      if (initObj.hasOwnProperty('phi')) {
        this.phi = initObj.phi
      }
      else {
        this.phi = 0.0;
      }
      if (initObj.hasOwnProperty('speed')) {
        this.speed = initObj.speed
      }
      else {
        this.speed = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Heading
    // Serialize message field [phi]
    bufferOffset = _serializer.float32(obj.phi, buffer, bufferOffset);
    // Serialize message field [speed]
    bufferOffset = _serializer.float32(obj.speed, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Heading
    let len;
    let data = new Heading(null);
    // Deserialize message field [phi]
    data.phi = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [speed]
    data.speed = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'duckiepond/Heading';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8fe8a91eef3de9ae7860b3f07a1529db';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 phi
    float32 speed
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Heading(null);
    if (msg.phi !== undefined) {
      resolved.phi = msg.phi;
    }
    else {
      resolved.phi = 0.0
    }

    if (msg.speed !== undefined) {
      resolved.speed = msg.speed;
    }
    else {
      resolved.speed = 0.0
    }

    return resolved;
    }
};

module.exports = Heading;
