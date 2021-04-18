#!/usr/bin/env python3
"""
Module for Authentication
0x07-Session_authentication
holbertonschool-web_back_end
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
import uuid


class SessionAuth(Auth):
    """[SessionAuth Class]
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """[an instance method that creates a Session ID for a user_id]

        Args:
            user_id (str): [user's ID]

        Returns:
            str: [the session ID created]
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        self.id = str(uuid.uuid4())
        self.user_id_by_session_id[self.id] = user_id
        return self.id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """[retreives a User ID based on a Session ID]
        Args:
            session_id (str, optional): [session ID]
        Returns:
            str: [the value (the User ID) for the key session_id in the
            dictionary user_id_by_session_id]
        """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)
