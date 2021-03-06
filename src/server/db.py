from __future__ import annotations
import hashlib

import jwt
import mongoengine


def hash_passwd(password: str) -> str:
    """Hash a string using the SHA-256 algorithm."""
    return hashlib.sha256(bytes(password, "utf-8")).hexdigest()


SECRET: str = "secret23804"
USERS: list[dict[str, str]] = [
    {
        "username": "user1",
        "hashed_password": hash_passwd("password1"),
        "name": "Roberto",
        "surname": "Carlos",
        "email": "rc@email.com",
    },
    {
        "username": "admin",
        "hashed_password": hash_passwd("admin"),
        "name": "Admin",
        "surname": "Admin",
        "email": "admin@email.com",
    },
]


class Database:
    """A class to manage the Users' database."""

    def __init__(self):
        """Initialize the database."""

        mongoengine.connect("users")

        if not User.objects.count():
            for user in USERS:
                User(**user).save()

    def authenticate(self, username: str, password: str) -> User | None:
        """
        Authenticate a user.

        :param username: the username of the user.
        :param password: the password of the user.
        :return: The user if exists, None otherwise.
        """
        user: User | None = User.objects(username=username).first()

        if user is None:
            return None

        if user.is_password(password):
            return user

        return None

    def get_user_by_token(self, token: str) -> User | None:
        """
        Get the user from the token.

        :param token: the token.
        :return: the user if exists, None otherwise.
        """
        try:
            username: str = jwt.decode(token, SECRET, algorithms=["HS256"])["username"]
        except jwt.InvalidTokenError:
            return None

        return User.objects(username=username).first()


class User(mongoengine.Document):
    """A model for a User."""

    username = mongoengine.StringField(required=True, max_length=50)
    name = mongoengine.StringField(required=True)
    surname = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)
    hashed_password = mongoengine.StringField(required=True)

    meta = {"db_alias": "default", "collection": "users"}

    def generate_token(self) -> str:
        """
        Generate a JWT token for the user.

        :return: the JWT token.
        """
        return jwt.encode({"username": self.username}, SECRET, algorithm="HS256")

    def is_password(self, password: str) -> bool:
        """
        Check if the password is correct.

        :param password: the password.
        :return: True if the password is correct, False otherwise.
        """
        return self.hashed_password == hash_passwd(password)
