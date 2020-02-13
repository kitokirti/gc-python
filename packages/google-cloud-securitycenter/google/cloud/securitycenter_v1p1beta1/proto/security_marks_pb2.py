# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/securitycenter_v1p1beta1/proto/security_marks.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/securitycenter_v1p1beta1/proto/security_marks.proto",
    package="google.cloud.securitycenter.v1p1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n)com.google.cloud.securitycenter.v1p1beta1P\001ZSgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1p1beta1;securitycenter\252\002%Google.Cloud.SecurityCenter.V1P1Beta1\312\002%Google\\Cloud\\SecurityCenter\\V1p1beta1\352\002(Google::Cloud::SecurityCenter::V1p1beta1"
    ),
    serialized_pb=_b(
        '\n@google/cloud/securitycenter_v1p1beta1/proto/security_marks.proto\x12%google.cloud.securitycenter.v1p1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/api/resource.proto"\xda\x02\n\rSecurityMarks\x12\x0c\n\x04name\x18\x01 \x01(\t\x12N\n\x05marks\x18\x02 \x03(\x0b\x32?.google.cloud.securitycenter.v1p1beta1.SecurityMarks.MarksEntry\x1a,\n\nMarksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:\xbc\x01\xea\x41\xb8\x01\n+securitycenter.googleapis.com/SecurityMarks\x12\x39organizations/{organization}/assets/{asset}/securityMarks\x12Norganizations/{organization}/sources/{source}/findings/{finding}/securityMarksB\xfd\x01\n)com.google.cloud.securitycenter.v1p1beta1P\x01ZSgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1p1beta1;securitycenter\xaa\x02%Google.Cloud.SecurityCenter.V1P1Beta1\xca\x02%Google\\Cloud\\SecurityCenter\\V1p1beta1\xea\x02(Google::Cloud::SecurityCenter::V1p1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
    ],
)


_SECURITYMARKS_MARKSENTRY = _descriptor.Descriptor(
    name="MarksEntry",
    full_name="google.cloud.securitycenter.v1p1beta1.SecurityMarks.MarksEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.securitycenter.v1p1beta1.SecurityMarks.MarksEntry.key",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.securitycenter.v1p1beta1.SecurityMarks.MarksEntry.value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=276,
    serialized_end=320,
)

_SECURITYMARKS = _descriptor.Descriptor(
    name="SecurityMarks",
    full_name="google.cloud.securitycenter.v1p1beta1.SecurityMarks",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.securitycenter.v1p1beta1.SecurityMarks.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="marks",
            full_name="google.cloud.securitycenter.v1p1beta1.SecurityMarks.marks",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[_SECURITYMARKS_MARKSENTRY,],
    enum_types=[],
    serialized_options=_b(
        "\352A\270\001\n+securitycenter.googleapis.com/SecurityMarks\0229organizations/{organization}/assets/{asset}/securityMarks\022Norganizations/{organization}/sources/{source}/findings/{finding}/securityMarks"
    ),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=165,
    serialized_end=511,
)

_SECURITYMARKS_MARKSENTRY.containing_type = _SECURITYMARKS
_SECURITYMARKS.fields_by_name["marks"].message_type = _SECURITYMARKS_MARKSENTRY
DESCRIPTOR.message_types_by_name["SecurityMarks"] = _SECURITYMARKS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SecurityMarks = _reflection.GeneratedProtocolMessageType(
    "SecurityMarks",
    (_message.Message,),
    dict(
        MarksEntry=_reflection.GeneratedProtocolMessageType(
            "MarksEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_SECURITYMARKS_MARKSENTRY,
                __module__="google.cloud.securitycenter_v1p1beta1.proto.security_marks_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1p1beta1.SecurityMarks.MarksEntry)
            ),
        ),
        DESCRIPTOR=_SECURITYMARKS,
        __module__="google.cloud.securitycenter_v1p1beta1.proto.security_marks_pb2",
        __doc__="""User specified security marks that are attached to the parent Cloud
  Security Command Center (Cloud SCC) resource. Security marks are scoped
  within a Cloud SCC organization -- they can be modified and viewed by
  all users who have proper permissions on the organization.
  
  
  Attributes:
      name:
          The relative resource name of the SecurityMarks. See: https://
          cloud.google.com/apis/design/resource\_names#relative\_resourc
          e\_name Examples: "organizations/{organization\_id}/assets/{as
          set\_id}/securityMarks" "organizations/{organization\_id}/sour
          ces/{source\_id}/findings/{finding\_id}/securityMarks".
      marks:
          Mutable user specified security marks belonging to the parent
          resource. Constraints are as follows:  -  Keys and values are
          treated as case insensitive -  Keys must be between 1 - 256
          characters (inclusive) -  Keys must be letters, numbers,
          underscores, or dashes -  Values have leading and trailing
          whitespace trimmed, remaining    characters must be between 1
          - 4096 characters (inclusive)
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1p1beta1.SecurityMarks)
    ),
)
_sym_db.RegisterMessage(SecurityMarks)
_sym_db.RegisterMessage(SecurityMarks.MarksEntry)


DESCRIPTOR._options = None
_SECURITYMARKS_MARKSENTRY._options = None
_SECURITYMARKS._options = None
# @@protoc_insertion_point(module_scope)
