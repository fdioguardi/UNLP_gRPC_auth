# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\"8\n\x0b\x43redentials\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x17\n\x0fhashed_password\x18\x02 \x01(\t\"\x1e\n\rTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t2?\n\rAuthenticator\x12.\n\x0c\x61uthenticate\x12\x0c.Credentials\x1a\x0e.TokenResponse\"\x00\x62\x06proto3')



_CREDENTIALS = DESCRIPTOR.message_types_by_name['Credentials']
_TOKENRESPONSE = DESCRIPTOR.message_types_by_name['TokenResponse']
Credentials = _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), {
  'DESCRIPTOR' : _CREDENTIALS,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:Credentials)
  })
_sym_db.RegisterMessage(Credentials)

TokenResponse = _reflection.GeneratedProtocolMessageType('TokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOKENRESPONSE,
  '__module__' : 'auth_pb2'
  # @@protoc_insertion_point(class_scope:TokenResponse)
  })
_sym_db.RegisterMessage(TokenResponse)

_AUTHENTICATOR = DESCRIPTOR.services_by_name['Authenticator']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREDENTIALS._serialized_start=14
  _CREDENTIALS._serialized_end=70
  _TOKENRESPONSE._serialized_start=72
  _TOKENRESPONSE._serialized_end=102
  _AUTHENTICATOR._serialized_start=104
  _AUTHENTICATOR._serialized_end=167
# @@protoc_insertion_point(module_scope)
