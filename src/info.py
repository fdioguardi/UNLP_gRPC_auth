import grpc

from src.server.db import Database, User
from src.service.info_pb2 import Information
import src.service.info_pb2_grpc


class InformantServicer(src.service.info_pb2_grpc.InformantServicer):
    """
    A server that provides information about the users in the database.
    It requires a JWT token to be sent in the header of the request.
    """

    def __init__(self):
        self.db = Database()

    def GetInfo(self, request: Information, context: grpc.RpcContext) -> Information:
        """
        Returns information about the users in the database.
        """
        if not context.is_active():
            return Information()

        user = User.from_token(context.peer(), request.token)
        if not user:
            return Information()

        return Information(users=[user.to_info() for user in self.db.get_users()])
