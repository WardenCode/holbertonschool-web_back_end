#!/usr/bin/env python3
"""
Auth module
"""

import uuid
from typing import Optional

from bcrypt import checkpw, gensalt, hashpw
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hash a string (password)

    Args:
        password (str): Password/String to be hashed

    Returns:
        bytes: Hashed password on bytes
    """

    return hashpw(password.encode("utf-8"), gensalt())


def _generate_uuid() -> str:
    """
    Generate a uuid

    Returns:
        str: new uuid
    """
    return str(uuid.uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a User in the DB

        Args:
            email (str): Email to be registered
            password (str): Password of the user

        Raises:
            ValueError: The email was already used, the user already exist.

        Returns:
            User: Registered user
        """
        is_already_registered: Optional[User] = None

        try:
            is_already_registered = self._db.find_user_by(
                email=email)
        except NoResultFound:
            pass

        if (is_already_registered):
            raise ValueError("User {:s} already exists".format(email))

        registered_user: User = self._db.add_user(
            email, _hash_password(password).decode("utf-8"))

        return registered_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate if email and password is part of a valid user

        Args:
            email (str): user email
            password (str): user password

        Returns:
            bool: True if the user and password is valid,
            False otherwise
        """
        try:
            found_user = self._db.find_user_by(email=email)
        except (NoResultFound, InvalidRequestError):
            return False

        if checkpw(password.encode("utf-8"),
                   found_user.hashed_password.encode("utf-8")):
            return (True)

        return (False)

    def create_session(self, email: str) -> Optional[str]:
        """
        Create a session for a user

        Args:
            email (str): User email

        Returns:
            str: Session id (uuid) as string
        """

        found_user: Optional[User] = None

        try:
            found_user = self._db.find_user_by(email=email)
        except (NoResultFound, InvalidRequestError):
            return None

        new_uuid: str = _generate_uuid()

        self._db.update_user(found_user.id, session_id=new_uuid)

        return (new_uuid)

    def get_user_from_session_id(self, session_id: Optional[str]) -> Optional[User]:
        """
        Get a User instance corresponding to session_id

        Args:
            session_id (str): session_id

        Returns:
            Optional[User]: User if the session_id match
            with it's own session_id
        """
        found_user: Optional[User] = None

        if (session_id is None):
            return None

        try:
            found_user = self._db.find_user_by(session_id=session_id)
        except (InvalidRequestError, NoResultFound):
            return None

        return found_user

    def destoy_session(self, user_id: int) -> None:
        """
        Search a session through user_id and destroy it

        Args:
            user_id (int): UserID
        """
        try:
            self._db.find_user_by(user_id=user_id)
        except (InvalidRequestError, NoResultFound):
            return None

        self._db.update_user(user_id, session_id=None)

        return None
