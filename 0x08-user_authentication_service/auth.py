#!/usr/bin/env python3
"""
Auth module
"""

from typing import Optional

from bcrypt import gensalt, hashpw
from db import DB
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
            email, str(_hash_password(password)))

        return registered_user
