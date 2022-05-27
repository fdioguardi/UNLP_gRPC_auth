from __future__ import annotations
import mongoengine
import jwt


class Database:
    """A class to manage the Users database"""

    def __init__(self):
        """
        Initialize the database
        """
        mongoengine.connect("users")

    def authenticate(self, username: str, hashed_password: str) -> User | None:
        """
        Authenticate a user
        :param username: the username of the user
        :param hashed_password: the hashed password of the user
        :return: The user if exists, None otherwise
        """
        user: User | None = User.objects(username=username).first()

        print(user)

        if user is None:
            return None

        if user.hashed_password == hashed_password:
            return user

        return None

    def get_user_by_token(self, token: str) -> User | None:
        """
        Get the user from the token
        :param token: the token
        :return: the user if exists, None otherwise
        """
        try:
            username: str = jwt.decode(token, "secret23804", algorithms=["HS256"])[
                "username"
            ]
        except jwt.InvalidTokenError:
            return None

        return User.objects(username=username).first()


class User(mongoengine.Document):
    """A model for a User"""

    username = mongoengine.StringField(required=True, max_length=50)
    name = mongoengine.StringField(required=True)
    surname = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)
    hashed_password = mongoengine.StringField(required=True)

    meta = {"db_alias": "default", "collection": "users"}

    def generate_token(self) -> str:
        """
        Generate a JWT token for the user.
        :return: the JWT token
        """
        return jwt.encode({"username": self.username}, "secret23804", algorithm="HS256")
