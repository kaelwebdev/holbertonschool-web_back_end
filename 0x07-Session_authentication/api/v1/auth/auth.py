#!/usr/bin/env python3
"""
Authentication
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """
    Class Auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        check if the path needs authorization
        """
        if path is None or excluded_paths is None:
            return True
        if path[-1] is not "/":
            path += "/"

        wcp = [p[:-1] for p in excluded_paths if p.endswith('*')]

        for p in wcp:
            if path.startswith(p):
                return False

        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """
        return the value of the header request 'Authorization'.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Do nothing """
        return None

    def session_cookie(self, request=None):
        """
        return cookie value from a request
        """
        if request is None:
            return None
        return request.cookies.get(getenv("SESSION_NAME"), None)
