"""
A gRPC client to interact with an authentication server and get the
user information from an information server.
"""

from collections import namedtuple

import grpc

from src import utils
import src.service.auth_pb2 as auth_pb2
import src.service.auth_pb2_grpc as auth_grpc
import src.service.info_pb2 as info_pb2
import src.service.info_pb2_grpc as info_grpc

User = namedtuple("User", ["username", "password"])
USERS = [
    User(username="user1", password="password1"),
    User(username="user2", password="password2"),
]


def start_client():
    # Create a channel to the server
    auth_channel = grpc.insecure_channel("localhost:5000")

    # Connect to the authentication server
    auth_stub = auth_grpc.AuthenticatorStub(auth_channel)

    # Connect to the information server
    info_channel = grpc.insecure_channel("localhost:5001")

    # Connect to the information server
    info_stub = info_grpc.InformantStub(info_channel)

    # ------------------

    for user in USERS:
        print("----------------------------------------------------")
        auth_request = auth_pb2.Credentials(
            username=user.username, hashed_password=utils.hash_passwd(user.password)
        )

        try:
            auth_response = auth_stub.authenticate(auth_request)
            print("Authentication successful")
        except grpc.RpcError as e:
            print(e.details())
            print("Authentication failed")
            continue

        info_request = info_pb2.TokenRequest(token=auth_response.token)

        try:
            info_response = info_stub.getInfo(info_request)
            print("User information:")
            print(f"\tUsername: {info_response.username}")
            print(f"\tName: {info_response.name}")
            print(f"\tSurname: {info_response.surname}")
            print(f"\tEmail: {info_response.email}")
        except grpc.RpcError as e:
            print(e.details())
            print("Failed to get user information")
            continue

    print("----------------------------------------------------")
