# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)


class RebootRequest(google___protobuf___message___Message):

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RebootRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
