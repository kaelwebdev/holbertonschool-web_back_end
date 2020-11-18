#!/usr/bin/env python3
"""
Database module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from typing import TypeVar
from user import Base
from user import User


class DB:
    """
    Data Base with SQLAlchemy
    """

    def __init__(self):
        """
        auto call
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """
        Create session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a user instance to the session DB
        """
        n_user = User(email=email, hashed_password=hashed_password)
        self._session.add(n_user)
        self._session.commit()
        return n_user

    def find_user_by(self, **kwargs: dict) -> User:
        """
        takes in arbitrary keyword arguments and returns
        the first row found in the users table as
        filtered by the method’s input arguments
        """
        if not kwargs:
            raise InvalidRequestError
        c_names = User.__table__.columns.keys()
        for k in kwargs.keys():
            if k not in c_names:
                raise InvalidRequestError
        u = self._session.query(User).filter_by(**kwargs).first()
        if u is None:
            raise NoResultFound
        return u
