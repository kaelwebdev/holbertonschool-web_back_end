#!/usr/bin/env python3
"""
Basic authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    basic authentication
    """
    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """ return Base64 part of auth header for a basic authentication. """
        if auth_header is None or type(auth_header) is not str:
            return None
        return auth_header[6:] if auth_header.startswith('Basic ') else None
