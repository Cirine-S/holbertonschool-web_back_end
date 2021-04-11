#!/usr/bin/env python3
"""
Module for Authentication
0x06-Basic_authentication
holbertonschool-web_back_end
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    Auth class that manage the API Authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """[Check if a specific path need authentication]
        Args:
            path (str): [path to check]
            excluded_paths (List[str]): [list of excluded paths]
        Returns:
            bool: [true if authentication need, false otherwise]
        """
        if excluded_paths is None or excluded_paths == [] or path is None:
            return True
        if not path.endswith("/"):
            path += "/"
        for excluded_path in excluded_paths:
            if excluded_path.endswith("*"):
                if path.startswith(excluded_path[:-1]):
                    return False
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """[return the value of the header request Authorization]
        Args:
            request ([type], optional): [description]. Defaults to None.
        Returns:
            str: [description]
        """
        if request is None or request.headers.get('authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """[summary]
        """

        return None
