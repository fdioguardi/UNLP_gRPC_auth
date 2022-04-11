import grpc

from src.server.db import Database, User
from src.service.info_pb2 import TokenRequest, Information
import src.service.info_pb2_grpc


class InformantServicer(src.service.info_pb2_grpc.InformantServicer):
    """
    A server to query information about users. It requires a JWT token
    to be sent in the request.
    """

    def __init__(self):
        self.db = Database()

    def GetInfo(self, request: TokenRequest, context: grpc.RpcContext) -> Information:
        """
        Get information about a user.
        """
        user: User | None = self.db.get_user_by_token(request.token)
        if user is None:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid token")
            return Information()

        return Information(username=user.username, name=user.name, surname=user.surname, email=user.email)
