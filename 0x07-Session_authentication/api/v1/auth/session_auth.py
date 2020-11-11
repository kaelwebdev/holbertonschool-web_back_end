#!/usr/bin/env python3
"""
session authentication
"""
from api.v1.auth.auth import Auth
import uuid
from typing import TypeVar
from models.user import User


class SessionAuth(Auth):
    """
    session authentication class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None or type(user_id) is not str:
            return None
        s_id = str(uuid.uuid4())
        self.user_id_by_session_id[s_id] = user_id
        return s_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID:
        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns a User instance based on a cookie value
        """
        if not request:
            return None
        c = self.session_cookie(request)
        if not c:
            return None
        user_id = self.user_id_for_session_id(c)
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """
        destroy a current session
        """
        if request is None:
            return None
        c = self.session_cookie(request)
        if not c:
            return False
        u_id = self.user_id_for_session_id(c)
        if not u_id:
            return False
        self.user_id_by_session_id.pop(c)
        return True
