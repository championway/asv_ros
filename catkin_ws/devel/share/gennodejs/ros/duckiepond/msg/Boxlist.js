// Auto-generated. Do not edit!

// (in-package duckiepond.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Box = require('./Box.js');
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------

class Boxlist {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.list = null;
      this.image_width = null;
      this.image_height = null;
      this.image = null;
    }
    else {
      if (initObj.hasOwnProperty('list')) {
        this.list = initObj.list
      }
      else {
        this.list = [];
      }
      if (initObj.hasOwnProperty('image_width')) {
        this.image_width = initObj.image_width
      }
      else {
        this.image_width = 0;
      }
      if (initObj.hasOwnProperty('image_height')) {
        this.image_height = initObj.image_height
      }
      else {
        this.image_height = 0;
      }
      if (initObj.hasOwnProperty('image')) {
        this.image = initObj.image
      }
      else {
        this.image = new sensor_msgs.msg.CompressedImage();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Boxlist
    // Serialize message field [list]
    // Serialize the length for message field [list]
    bufferOffset = _serializer.uint32(obj.list.length, buffer, bufferOffset);
    obj.list.forEach((val) => {
      bufferOffset = Box.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [image_width]
    bufferOffset = _serializer.int32(obj.image_width, buffer, bufferOffset);
    // Serialize message field [image_height]
    bufferOffset = _serializer.int32(obj.image_height, buffer, bufferOffset);
    // Serialize message field [image]
    bufferOffset = sensor_msgs.msg.CompressedImage.serialize(obj.image, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Boxlist
    let len;
    let data = new Boxlist(null);
    // Deserialize message field [list]
    // Deserialize array length for message field [list]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.list = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.list[i] = Box.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [image_width]
    data.image_width = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [image_height]
    data.image_height = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [image]
    data.image = sensor_msgs.msg.CompressedImage.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 24 * object.list.length;
    length += sensor_msgs.msg.CompressedImage.getMessageSize(object.image);
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'duckiepond/Boxlist';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '64ed701dbabc3b78cf16142116cf4f2f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Box[] list
    int32 image_width
    int32 image_height
    sensor_msgs/CompressedImage image
    ================================================================================
    MSG: duckiepond/Box
    int32 x
    int32 y
    int32 w
    int32 h
    float32 confidence
    int32 id
    ================================================================================
    MSG: sensor_msgs/CompressedImage
    # This message contains a compressed image
    
    Header header        # Header timestamp should be acquisition time of image
                         # Header frame_id should be optical frame of camera
                         # origin of frame should be optical center of camera
                         # +x should point to the right in the image
                         # +y should point down in the image
                         # +z should point into to plane of the image
    
    string format        # Specifies the format of the data
                         #   Acceptable values:
                         #     jpeg, png
    uint8[] data         # Compressed image buffer
    
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
    const resolved = new Boxlist(null);
    if (msg.list !== undefined) {
      resolved.list = new Array(msg.list.length);
      for (let i = 0; i < resolved.list.length; ++i) {
        resolved.list[i] = Box.Resolve(msg.list[i]);
      }
    }
    else {
      resolved.list = []
    }

    if (msg.image_width !== undefined) {
      resolved.image_width = msg.image_width;
    }
    else {
      resolved.image_width = 0
    }

    if (msg.image_height !== undefined) {
      resolved.image_height = msg.image_height;
    }
    else {
      resolved.image_height = 0
    }

    if (msg.image !== undefined) {
      resolved.image = sensor_msgs.msg.CompressedImage.Resolve(msg.image)
    }
    else {
      resolved.image = new sensor_msgs.msg.CompressedImage()
    }

    return resolved;
    }
};

module.exports = Boxlist;
