# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import auth_pb2 as auth__pb2


class AuthenticatorStub(object):
    """The authentication service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.authenticate = channel.unary_unary(
                '/Authenticator/authenticate',
                request_serializer=auth__pb2.Credentials.SerializeToString,
                response_deserializer=auth__pb2.TokenResponse.FromString,
                )


class AuthenticatorServicer(object):
    """The authentication service definition.
    """

    def authenticate(self, request, context):
        """Authenticates the user with the given credentials.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthenticatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'authenticate': grpc.unary_unary_rpc_method_handler(
                    servicer.authenticate,
                    request_deserializer=auth__pb2.Credentials.FromString,
                    response_serializer=auth__pb2.TokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Authenticator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Authenticator(object):
    """The authentication service definition.
    """

    @staticmethod
    def authenticate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Authenticator/authenticate',
            auth__pb2.Credentials.SerializeToString,
            auth__pb2.TokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)