# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from asv_msgs/Boxlist.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import asv_msgs.msg
import std_msgs.msg
import sensor_msgs.msg

class Boxlist(genpy.Message):
  _md5sum = "64ed701dbabc3b78cf16142116cf4f2f"
  _type = "asv_msgs/Boxlist"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """Box[] list
int32 image_width
int32 image_height
sensor_msgs/CompressedImage image
================================================================================
MSG: asv_msgs/Box
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
"""
  __slots__ = ['list','image_width','image_height','image']
  _slot_types = ['asv_msgs/Box[]','int32','int32','sensor_msgs/CompressedImage']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       list,image_width,image_height,image

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Boxlist, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.list is None:
        self.list = []
      if self.image_width is None:
        self.image_width = 0
      if self.image_height is None:
        self.image_height = 0
      if self.image is None:
        self.image = sensor_msgs.msg.CompressedImage()
    else:
      self.list = []
      self.image_width = 0
      self.image_height = 0
      self.image = sensor_msgs.msg.CompressedImage()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.list)
      buff.write(_struct_I.pack(length))
      for val1 in self.list:
        _x = val1
        buff.write(_get_struct_4ifi().pack(_x.x, _x.y, _x.w, _x.h, _x.confidence, _x.id))
      _x = self
      buff.write(_get_struct_2i3I().pack(_x.image_width, _x.image_height, _x.image.header.seq, _x.image.header.stamp.secs, _x.image.header.stamp.nsecs))
      _x = self.image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.image.format
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.list is None:
        self.list = None
      if self.image is None:
        self.image = sensor_msgs.msg.CompressedImage()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.list = []
      for i in range(0, length):
        val1 = asv_msgs.msg.Box()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.w, _x.h, _x.confidence, _x.id,) = _get_struct_4ifi().unpack(str[start:end])
        self.list.append(val1)
      _x = self
      start = end
      end += 20
      (_x.image_width, _x.image_height, _x.image.header.seq, _x.image.header.stamp.secs, _x.image.header.stamp.nsecs,) = _get_struct_2i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.image.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.image.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.image.format = str[start:end].decode('utf-8')
      else:
        self.image.format = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.image.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.list)
      buff.write(_struct_I.pack(length))
      for val1 in self.list:
        _x = val1
        buff.write(_get_struct_4ifi().pack(_x.x, _x.y, _x.w, _x.h, _x.confidence, _x.id))
      _x = self
      buff.write(_get_struct_2i3I().pack(_x.image_width, _x.image_height, _x.image.header.seq, _x.image.header.stamp.secs, _x.image.header.stamp.nsecs))
      _x = self.image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.image.format
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.list is None:
        self.list = None
      if self.image is None:
        self.image = sensor_msgs.msg.CompressedImage()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.list = []
      for i in range(0, length):
        val1 = asv_msgs.msg.Box()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.w, _x.h, _x.confidence, _x.id,) = _get_struct_4ifi().unpack(str[start:end])
        self.list.append(val1)
      _x = self
      start = end
      end += 20
      (_x.image_width, _x.image_height, _x.image.header.seq, _x.image.header.stamp.secs, _x.image.header.stamp.nsecs,) = _get_struct_2i3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.image.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.image.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.image.format = str[start:end].decode('utf-8')
      else:
        self.image.format = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.image.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4ifi = None
def _get_struct_4ifi():
    global _struct_4ifi
    if _struct_4ifi is None:
        _struct_4ifi = struct.Struct("<4ifi")
    return _struct_4ifi
_struct_2i3I = None
def _get_struct_2i3I():
    global _struct_2i3I
    if _struct_2i3I is None:
        _struct_2i3I = struct.Struct("<2i3I")
    return _struct_2i3I
