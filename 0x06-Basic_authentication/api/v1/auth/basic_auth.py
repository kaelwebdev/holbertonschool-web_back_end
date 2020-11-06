#!/usr/bin/env python3
"""
Basic authentication
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    basic authentication
    """
    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """ return Base64 part of auth header for a basic authentication. """
        if auth_header is None or type(auth_header) is not str:
            return None
        return auth_header[6:] if auth_header.startswith('Basic ') else None

    def decode_base64_authorization_header(self, b64_auth_header: str) -> str:
        """ return decoded value of a Base64 string. """
        if b64_auth_header is None or type(b64_auth_header) is not str:
            return None
        try:
            h = b64_auth_header.encode('utf-8')
            h = b64decode(h)
            h = h.decode('utf-8')
            return h
        except BaseException:
            return None

    def extract_user_credentials(self, base64_auth_header: str) -> (str, str):
        """ return information in tuple form. (username, password). """
        if base64_auth_header is None or type(base64_auth_header) is not str \
                or ':' not in base64_auth_header:
            return (None, None)
        return tuple(base64_auth_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str, user_pwd: str) ->\
            TypeVar('User'):
        """
        return matching user in list of users by email/pwd.
        """
        if user_email is None or user_pwd is None or \
                type(user_email) is not str or type(user_pwd) is not str:
            return None

        users = User.search({'email': user_email})

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        overloads Auth and retrieves the User instance for a request
        """
        h = self.authorization_header(request)
        if not h:
            return None
        h = self.extract_base64_authorization_header(h)
        h = self.decode_base64_authorization_header(h)
        if not h:
            return None
        user = self.extract_user_credentials(h)

        return self.user_object_from_credentials(user[0], user[1])
