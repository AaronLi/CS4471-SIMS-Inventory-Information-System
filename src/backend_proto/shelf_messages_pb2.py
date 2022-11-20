# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: backend_proto/shelf_messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"backend_proto/shelf_messages.proto\x12\x10sims_ims_backend\"2\n\tShelfInfo\x12\x10\n\x08shelf_id\x18\x01 \x01(\t\x12\x13\n\x0bshelf_count\x18\x02 \x01(\r\"P\n\x12\x43reateShelfRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12)\n\x04info\x18\x02 \x01(\x0b\x32\x1b.sims_ims_backend.ShelfInfo\"\x15\n\x13\x43reateShelfResponse\"3\n\x10ReadShelfRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\">\n\x11ReadShelfResponse\x12)\n\x04info\x18\x01 \x01(\x0b\x32\x1b.sims_ims_backend.ShelfInfo\"e\n\x12UpdateShelfRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\x12.\n\tnew_state\x18\x03 \x01(\x0b\x32\x1b.sims_ims_backend.ShelfInfo\"\x15\n\x13UpdateShelfResponse\"5\n\x12\x44\x65leteShelfRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06target\x18\x02 \x01(\t\"\x15\n\x13\x44\x65leteShelfResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'backend_proto.shelf_messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SHELFINFO._serialized_start=56
  _SHELFINFO._serialized_end=106
  _CREATESHELFREQUEST._serialized_start=108
  _CREATESHELFREQUEST._serialized_end=188
  _CREATESHELFRESPONSE._serialized_start=190
  _CREATESHELFRESPONSE._serialized_end=211
  _READSHELFREQUEST._serialized_start=213
  _READSHELFREQUEST._serialized_end=264
  _READSHELFRESPONSE._serialized_start=266
  _READSHELFRESPONSE._serialized_end=328
  _UPDATESHELFREQUEST._serialized_start=330
  _UPDATESHELFREQUEST._serialized_end=431
  _UPDATESHELFRESPONSE._serialized_start=433
  _UPDATESHELFRESPONSE._serialized_end=454
  _DELETESHELFREQUEST._serialized_start=456
  _DELETESHELFREQUEST._serialized_end=509
  _DELETESHELFRESPONSE._serialized_start=511
  _DELETESHELFRESPONSE._serialized_end=532
# @@protoc_insertion_point(module_scope)