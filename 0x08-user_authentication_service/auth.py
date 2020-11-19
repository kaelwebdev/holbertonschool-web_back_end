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
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    return a salted hash of the input password
    It is an encryption complicate dictionary attacks
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    new UUID
    """
    return str(uuid4())


class Auth:
    """
    Auth class
    note: Auth._db is a private property
    and should NEVER be used from outside the class.
    """

    def __init__(self):
        """ Initialize database """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ add a new user """
        try:
            u = self._db.find_user_by(email=email)
            if u:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pass
        n_user = self._db.add_user(email, _hash_password(password))
        return n_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        check password and return true || false
        """
        try:
            u = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), u.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Creates session
        """
        try:
            u = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(u.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
