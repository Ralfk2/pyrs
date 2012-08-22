# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='rspeers.proto',
  package='',
  serialized_pb='\n\rrspeers.proto\"\x1f\n\x0crequestPeers\x12\x0f\n\x07options\x18\x01 \x02(\t\"(\n\x04peer\x12\x0e\n\x06peerId\x18\x01 \x02(\t\x12\x10\n\x08peerName\x18\x02 \x02(\t')




_REQUESTPEERS = descriptor.Descriptor(
  name='requestPeers',
  full_name='requestPeers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='options', full_name='requestPeers.options', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=17,
  serialized_end=48,
)


_PEER = descriptor.Descriptor(
  name='peer',
  full_name='peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='peerId', full_name='peer.peerId', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='peerName', full_name='peer.peerName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=50,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['requestPeers'] = _REQUESTPEERS
DESCRIPTOR.message_types_by_name['peer'] = _PEER

class requestPeers(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTPEERS
  
  # @@protoc_insertion_point(class_scope:requestPeers)

class peer(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PEER
  
  # @@protoc_insertion_point(class_scope:peer)

# @@protoc_insertion_point(module_scope)
