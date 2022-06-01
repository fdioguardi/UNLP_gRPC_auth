"""
A script to start the authentication and information servers
"""

from concurrent import futures
import multiprocessing as mp
import os

import grpc

from src.server.auth import AuthenticatorServicer
from src.server.info import InformantServicer
import src.service.auth_pb2_grpc as auth_grpc
import src.service.info_pb2_grpc as stub


def _start_auth_server():
    auth_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_grpc.add_AuthenticatorServicer_to_server(AuthenticatorServicer(), auth_server)
    auth_server.add_insecure_port("[::]:5000")
    auth_server.start()
    auth_server.wait_for_termination()


def _start_info_server():
    info_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    stub.add_InformantServicer_to_server(InformantServicer(), info_server)
    info_server.add_insecure_port("[::]:5001")
    info_server.start()
    info_server.wait_for_termination()


def _start_mongodb():
    os.system("mongod")


def start_servers():
    auth_process = mp.Process(target=_start_auth_server)
    info_process = mp.Process(target=_start_info_server)
    mp.Process(target=_start_mongodb).start()

    auth_process.start()
    info_process.start()
    auth_process.join()
    info_process.join()
