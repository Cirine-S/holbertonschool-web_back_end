#!/usr/bin/env python3
"""
Module for Authentication
0x06-Basic_authentication
holbertonschool-web_back_end
"""
from api.v1.auth.auth import Auth
import base64


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
