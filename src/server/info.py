import grpc

from src.server.db import Database, User
from src.service.info_pb2 import Information, TokenRequest
import src.service.info_pb2_grpc


class InformantServicer(src.service.info_pb2_grpc.InformantServicer):
    """
    A server to query information about users. It requires a JWT token
    to be sent in the request.
    """

    def __init__(self, *args, **kwargs):
        self.db = Database()
        super().__init__(*args, **kwargs)

    def getInfo(self, request: TokenRequest, context: grpc.RpcContext) -> Information:
        """
        Get information about a user.

        :param request: A TokenRequest object containing the JWT token.
        :param context: The context of the request.
        :return: An Information object containing the user's data.
        """
        user: User | None = self.db.get_user_by_token(request.token)
        if user is None:
            context.set_code(grpc.StatusCode.UNAUTHENTICATED)
            context.set_details("Invalid token")
            return Information()

        return Information(
            username=user.username,
            name=user.name,
            surname=user.surname,
            email=user.email,
        )
