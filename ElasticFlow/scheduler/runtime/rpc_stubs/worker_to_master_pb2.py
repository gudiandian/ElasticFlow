# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: worker_to_master.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='worker_to_master.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16worker_to_master.proto\x1a\x0c\x63ommon.proto\"H\n\x15RegisterWorkerRequest\x12\x0f\n\x07ip_addr\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x10\n\x08num_gpus\x18\x03 \x01(\r\"S\n\x16RegisterWorkerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x11\n\tworker_id\x18\x02 \x01(\r\x12\x15\n\rerror_message\x18\x03 \x01(\t\"0\n\x0b\x44oneRequest\x12\x11\n\tworker_id\x18\x01 \x01(\r\x12\x0e\n\x06job_id\x18\x02 \x01(\r2u\n\x0eWorkerToMaster\x12\x43\n\x0eRegisterWorker\x12\x16.RegisterWorkerRequest\x1a\x17.RegisterWorkerResponse\"\x00\x12\x1e\n\x04\x44one\x12\x0c.DoneRequest\x1a\x06.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_REGISTERWORKERREQUEST = _descriptor.Descriptor(
  name='RegisterWorkerRequest',
  full_name='RegisterWorkerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_addr', full_name='RegisterWorkerRequest.ip_addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='RegisterWorkerRequest.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_gpus', full_name='RegisterWorkerRequest.num_gpus', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=40,
  serialized_end=112,
)


_REGISTERWORKERRESPONSE = _descriptor.Descriptor(
  name='RegisterWorkerResponse',
  full_name='RegisterWorkerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='RegisterWorkerResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='worker_id', full_name='RegisterWorkerResponse.worker_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='RegisterWorkerResponse.error_message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=114,
  serialized_end=197,
)


_DONEREQUEST = _descriptor.Descriptor(
  name='DoneRequest',
  full_name='DoneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worker_id', full_name='DoneRequest.worker_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='DoneRequest.job_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=199,
  serialized_end=247,
)

DESCRIPTOR.message_types_by_name['RegisterWorkerRequest'] = _REGISTERWORKERREQUEST
DESCRIPTOR.message_types_by_name['RegisterWorkerResponse'] = _REGISTERWORKERRESPONSE
DESCRIPTOR.message_types_by_name['DoneRequest'] = _DONEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterWorkerRequest = _reflection.GeneratedProtocolMessageType('RegisterWorkerRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERWORKERREQUEST,
  '__module__' : 'worker_to_master_pb2'
  # @@protoc_insertion_point(class_scope:RegisterWorkerRequest)
  })
_sym_db.RegisterMessage(RegisterWorkerRequest)

RegisterWorkerResponse = _reflection.GeneratedProtocolMessageType('RegisterWorkerResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERWORKERRESPONSE,
  '__module__' : 'worker_to_master_pb2'
  # @@protoc_insertion_point(class_scope:RegisterWorkerResponse)
  })
_sym_db.RegisterMessage(RegisterWorkerResponse)

DoneRequest = _reflection.GeneratedProtocolMessageType('DoneRequest', (_message.Message,), {
  'DESCRIPTOR' : _DONEREQUEST,
  '__module__' : 'worker_to_master_pb2'
  # @@protoc_insertion_point(class_scope:DoneRequest)
  })
_sym_db.RegisterMessage(DoneRequest)



_WORKERTOMASTER = _descriptor.ServiceDescriptor(
  name='WorkerToMaster',
  full_name='WorkerToMaster',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=249,
  serialized_end=366,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterWorker',
    full_name='WorkerToMaster.RegisterWorker',
    index=0,
    containing_service=None,
    input_type=_REGISTERWORKERREQUEST,
    output_type=_REGISTERWORKERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Done',
    full_name='WorkerToMaster.Done',
    index=1,
    containing_service=None,
    input_type=_DONEREQUEST,
    output_type=common__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKERTOMASTER)

DESCRIPTOR.services_by_name['WorkerToMaster'] = _WORKERTOMASTER

# @@protoc_insertion_point(module_scope)
