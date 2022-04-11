import grpc

from src.server.db import Database, User
from src.service.auth_pb2 import Credentials, TokenResponse
import src.service.auth_pb2_grpc


class AuthenticatorServicer(src.service.auth_pb2_grpc.AuthenticatorServicer):
    """
    A server that implements the Authenticator service. This server
    authenticates users and returns a JWT token that can be used to
    authenticate users in other services.
    """

    def __init__(self):
        self.db = Database()

    def Authenticate(self, request: Credentials, context: grpc.RpcContext) -> TokenResponse:
        """
        Authenticates a user and returns a JWT token.

        :param request: The request containing the username and 
            hashed password.
        :param context: The context of the request.
        :return: A token response containing the JWT token.
        """
        user: User | None = self.db.authenticate(request.username, request.hashed_password)

        if user is None:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid username or password")
            return TokenResponse()

        return TokenResponse(token=user.generate_token())
