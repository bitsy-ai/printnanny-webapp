# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: monitoring.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='monitoring.proto',
  package='print_nanny_client.monitoring',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10monitoring.proto\x12\x1dprint_nanny_client.monitoring\"\xd7\x01\n\x12VideoRenderRequest\x12\x15\n\rprint_session\x18\x01 \x01(\t\x12\x18\n\x10print_session_id\x18\x02 \x01(\x05\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\x12\x1b\n\x13octoprint_device_id\x18\x04 \x01(\x05\x12\x1a\n\x12\x63loudiot_device_id\x18\x05 \x01(\x03\x12\n\n\x02ts\x18\x06 \x01(\x02\x12\x17\n\x0f\x63\x64n_output_path\x18\x07 \x01(\t\x12!\n\x19print_session_datesegment\x18\x08 \x01(\tb\x06proto3')
)




_VIDEORENDERREQUEST = _descriptor.Descriptor(
  name='VideoRenderRequest',
  full_name='print_nanny_client.monitoring.VideoRenderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='print_session', full_name='print_nanny_client.monitoring.VideoRenderRequest.print_session', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='print_session_id', full_name='print_nanny_client.monitoring.VideoRenderRequest.print_session_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='print_nanny_client.monitoring.VideoRenderRequest.user_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='octoprint_device_id', full_name='print_nanny_client.monitoring.VideoRenderRequest.octoprint_device_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloudiot_device_id', full_name='print_nanny_client.monitoring.VideoRenderRequest.cloudiot_device_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='print_nanny_client.monitoring.VideoRenderRequest.ts', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cdn_output_path', full_name='print_nanny_client.monitoring.VideoRenderRequest.cdn_output_path', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='print_session_datesegment', full_name='print_nanny_client.monitoring.VideoRenderRequest.print_session_datesegment', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=267,
)

DESCRIPTOR.message_types_by_name['VideoRenderRequest'] = _VIDEORENDERREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoRenderRequest = _reflection.GeneratedProtocolMessageType('VideoRenderRequest', (_message.Message,), dict(
  DESCRIPTOR = _VIDEORENDERREQUEST,
  __module__ = 'monitoring_pb2'
  # @@protoc_insertion_point(class_scope:print_nanny_client.monitoring.VideoRenderRequest)
  ))
_sym_db.RegisterMessage(VideoRenderRequest)


# @@protoc_insertion_point(module_scope)
