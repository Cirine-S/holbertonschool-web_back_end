#!/usr/bin/env python3
"""Auth module
"""
import bcrypt


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
