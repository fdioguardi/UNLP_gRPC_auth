import hashlib


def hash_passwd(password: str) -> str:
    """Hash a string using the SHA-256 algorithm."""
    return hashlib.sha256(bytes(password, "utf-8")).hexdigest()
