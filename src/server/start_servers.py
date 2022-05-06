"""
A script to start the authentication and information servers
"""

from concurrent import futures
import multiprocessing as mp

import grpc

import src.service.auth_pb2_grpc as auth_pb2_grpc
import src.service.info_pb2_grpc as info_pb2_grpc


def _start_auth_server():
    auth_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthenticatorServicer_to_server(
        auth_pb2_grpc.AuthenticatorServicer(), auth_server
    )
    auth_server.add_insecure_port("[::]:5901")
    auth_server.start()
    auth_server.wait_for_termination()


def _start_info_server():
    info_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    info_pb2_grpc.add_InformantServicer_to_server(
        info_pb2_grpc.InformantServicer(), info_server
    )
    info_server.add_insecure_port("[::]:6901")
    info_server.start()
    info_server.wait_for_termination()


def start_servers():
    auth_process = mp.Process(target=_start_auth_server)
    info_process = mp.Process(target=_start_info_server)

    auth_process.start()
    info_process.start()
    auth_process.join()
    info_process.join()
