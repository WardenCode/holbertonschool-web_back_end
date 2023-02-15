#!/usr/bin/env python3
"""
DB module
"""

from typing import List, Optional

from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        # self._engine = create_engine("sqlite:///a.db", echo=True)
        self._engine = create_engine("sqlite:///a.db", echo=False)  # for dev
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Creates a user and saves it in the DB

        Args:
            email (str): User email
            hashed_password (str): User Hashed Password

        Returns:
            User: The new User entered to the DB
        """
        new_user = User()
        new_user.email = email
        new_user.hashed_password = hashed_password
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a User using some filters provided by kwargs

        Args:
            **kwargs: Arbitrary keyword arguments.

        Raises:
            InvalidRequestError: Some key(s) of kwargs doesn't
            exists in users table
            NoResultFound: User not found

        Returns:
            User: Found User.
        """

        fields: List[str] = [column.key for column in User.__table__.c]

        for key in kwargs.keys():
            if (key not in fields):
                raise InvalidRequestError

        requested_user = self._session.query(
            User).filter_by(**kwargs).first()

        if requested_user is None:
            raise NoResultFound

        return requested_user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Update the attributes of a user

        Args:
            user_id (int): User ID

        Raises:
            ValueError: Some key(s) of kwargs doesn't exists in users table
        """

        fields: List[str] = [column.key for column in User.__table__.c]

        for key in kwargs.keys():
            if (key not in fields):
                raise ValueError

        try:
            user_to_update: User = self.find_user_by(id=user_id)
        except (InvalidRequestError, NoResultFound):
            raise ValueError

        for key, value in kwargs.items():
            setattr(user_to_update, key, value)
        self._session.commit()
