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
