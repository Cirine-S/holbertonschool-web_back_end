#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """method that takes in a password string arguments and returns bytes.
    Args:
            password (str): input password to crypt

    Returns:
            str: The returned bytes is a salted hash of the input password,
                        hashed with bcrypt.hashpw.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """if the user doesn't exist, hash the password with _hash_password,
        save the user to the database using self._db
        and return the User object.
        Args:
            email (str): [mandatory input]
            password (str): [mandatory input]

        Raises:
            ValueError: [if the user already exists in DB]

        Returns:
            User: User Object
        """
        try:
            user_object = self._db.find_user_by(email=email)
            if user_object:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)
