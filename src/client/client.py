"""
A gRPC client to interact with an authentication server and get the
user information from an information server.
"""

import grpc

import src.service.auth_pb2 as auth_pb2
import src.service.auth_pb2_grpc as auth_pb2_grpc
import src.service.info_pb2 as info_pb2
import src.service.info_pb2_grpc as info_pb2_grpc

import hashlib


# Create a channel to the server
auth_channel = grpc.insecure_channel("localhost:5901")

# Connect to the authentication server
auth_stub = auth_pb2_grpc.AuthenticatorStub(auth_channel)

hashed_password = hashlib.sha256(b"password1").hexdigest()
auth_request = auth_pb2.Credentials(username="user1", hashed_password=hashed_password)

try:
    auth_response = auth_stub.authenticate(auth_request)
    print("Authentication successful")
except grpc.RpcError as e:
    print(e.details())
    print("Authentication failed")
    exit(1)

# ------------------

# Connect to the information server
info_channel = grpc.insecure_channel("localhost:6901")

# Connect to the information server
info_stub = info_pb2_grpc.InformantStub(info_channel)

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
    exit(1)
