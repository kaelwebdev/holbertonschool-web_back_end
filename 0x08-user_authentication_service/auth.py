#!/usr/bin/env python3
"""
Auth module
"""

from user import User
from db import DB
from typing import TypeVar
import bcrypt
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> str:
    """
    return a salted hash of the input password
    It is an encryption complicate dictionary attacks
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
