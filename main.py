"""
Script to initialize the gRPC client and server.

    Usage:
        - python3.7 main.py --server    --> Start both gRPC servers
        - python3.7 main.py --client    --> Start a gRPC client
"""

import argparse
from src.server.start_servers import start_servers
from src.client.start_client import start_client


def main() -> None:
    """Main function."""

    args = get_args()
    args.func()


def get_args() -> argparse.Namespace:
    """Get arguments"""

    parser = argparse.ArgumentParser(description="Start gRPC systems.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-s",
        "--server",
        action="store_const",
        const=start_servers,
        dest="func",
        help="Start gRPC servers.",
    )
    group.add_argument(
        "-c",
        "--client",
        action="store_const",
        const=start_client,
        dest="func",
        help="Start gRPC client.",
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
