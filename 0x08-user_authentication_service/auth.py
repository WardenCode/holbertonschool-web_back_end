#!/usr/bin/env python3
"""
Auth module
"""

from typing import Optional
from uuid import uuid4

from bcrypt import checkpw, gensalt, hashpw
from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
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
    return str(uuid4())


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
        except InvalidRequestError:
            raise ValueError("User {:s} already exists".format(email))

        if (is_already_registered):
            raise ValueError("User {:s} already exists".format(email))

        registered_user: User = self._db.add_user(
            email, _hash_password(password))

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
                   found_user.hashed_password):
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

        try:
            self._db.update_user(found_user.id, session_id=new_uuid)
        except ValueError:
            return None

        return (new_uuid)

    def get_user_from_session_id(self,
                                 session_id: Optional[str]) -> Optional[User]:
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

    def destroy_session(self, user_id: int) -> None:
        """
        Search a session through user_id and destroy it

        Args:
            user_id (int): UserID
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            return None

        return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a reset password token for the user

        Args:
            email (str): user email

        Raises:
            ValueError

        Returns:
            str: Reset password token
        """

        found_user: Optional[User] = None

        try:
            found_user = self._db.find_user_by(email=email)
            self._db.update_user(found_user.id, reset_token=_generate_uuid())
        except (InvalidRequestError, NoResultFound, ValueError):
            raise ValueError

        return found_user.reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update user password using a reset_token

        Args:
            reset_token (str): User reset token
            password (str): User password

        Raises:
            ValueError: Reset token doesn't match
        """
        found_user: Optional[User] = None

        try:
            found_user = self._db.find_user_by(reset_token=reset_token)
        except (InvalidRequestError, NoResultFound):
            raise ValueError

        try:
            self._db.update_user(
                found_user.id,
                hashed_password=_hash_password(password),
                reset_token=None)
        except ValueError:
            return
