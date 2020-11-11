#!/usr/bin/env python3
"""
session authentication
"""
from api.v1.auth.auth import Auth


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
