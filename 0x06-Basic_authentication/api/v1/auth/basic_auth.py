#!/usr/bin/env python3
"""
Module for Authentication
0x06-Basic_authentication
holbertonschool-web_back_end
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """[BasicAuth Class]
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns Base64 part of the Authorization header for a BasicAuth"""

        if authorization_header is None:
            return None
        elif type(authorization_header) is not str:
            return None
        elif not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header[6:]

    def isBase64(self, s):
        """try/except method to check base64 encoding"""
        try:
            return base64.b64encode(base64.b64decode(s)).decode("utf-8") == s
        except Exception:
            return False

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """generates the decoded value of a Base64 string ]

        Args:
            base64_authorization_header (str): [description]

        Returns:
            str: [the decoded value of a Base64 string]
        """
        if base64_authorization_header is None:
            return None
        elif type(base64_authorization_header) is not str:
            return None
        elif not self.isBase64(base64_authorization_header):
            return None
        else:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """[returns the user email and password from the Base64 decoded value]

        Args:
            self ([type]): [description]
            str ([type]): [description]
        Returns:
            2 values
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        emailAndPass = decoded_base64_authorization_header.split(':')
        return tuple(emailAndPass)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """[returns the User instance based on his email and password]"""
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception as e:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
