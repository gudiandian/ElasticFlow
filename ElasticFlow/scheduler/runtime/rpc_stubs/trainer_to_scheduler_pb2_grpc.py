# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import common_pb2 as common__pb2
import trainer_to_scheduler_pb2 as trainer__to__scheduler__pb2


class TrainerToSchedulerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReportStable = channel.unary_unary(
                '/TrainerToScheduler/ReportStable',
                request_serializer=trainer__to__scheduler__pb2.ReportStableRequest.SerializeToString,
                response_deserializer=common__pb2.Empty.FromString,
                )
        self.ReportReady = channel.unary_unary(
                '/TrainerToScheduler/ReportReady',
                request_serializer=trainer__to__scheduler__pb2.ReportReadyRequest.SerializeToString,
                response_deserializer=common__pb2.Empty.FromString,
                )


class TrainerToSchedulerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReportStable(self, request, context):
        """Report to scheduler that the job is training stable
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReportReady(self, request, context):
        """Report to scheduler that the job is training ready
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrainerToSchedulerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReportStable': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportStable,
                    request_deserializer=trainer__to__scheduler__pb2.ReportStableRequest.FromString,
                    response_serializer=common__pb2.Empty.SerializeToString,
            ),
            'ReportReady': grpc.unary_unary_rpc_method_handler(
                    servicer.ReportReady,
                    request_deserializer=trainer__to__scheduler__pb2.ReportReadyRequest.FromString,
                    response_serializer=common__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TrainerToScheduler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrainerToScheduler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReportStable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TrainerToScheduler/ReportStable',
            trainer__to__scheduler__pb2.ReportStableRequest.SerializeToString,
            common__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReportReady(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TrainerToScheduler/ReportReady',
            trainer__to__scheduler__pb2.ReportReadyRequest.SerializeToString,
            common__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
