#!/usr/bin/env python3
"""
Basic Auth Module
"""

from base64 import b64decode
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """
    Empty class of a Basic Auth

    Args:
        Auth (Auth): Main auth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        self descriptive

        Args:
            authorization_header (str): Value of authorization_header

        Returns:
            str | Nonw: Base64 authorization header
        """

        if (not authorization_header):
            return (None)

        if (not isinstance(authorization_header, str)):
            return (None)

        if "Basic " not in authorization_header:
            return (None)

        return (authorization_header[6:])

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        self descriptive

        Args:
            base64_authorization_header (str): Header to be decoded

        Returns:
            str | None: Decoded string or None if is impossible
        """

        if (not base64_authorization_header):
            return (None)

        if (not isinstance(base64_authorization_header, str)):
            return (None)

        try:
            return (b64decode(base64_authorization_header).decode('utf-8'))
        except Exception:
            return (None)

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        self descriptive

        Args:
            decoded_base64_authorization_header (str): info
            of authorization header

        Returns:
            Tuple[str, str] | Tuple[None, None]: email and password
            if exists, None otherwise
        """

        result = (None, None)

        if (not decoded_base64_authorization_header):
            return result

        if (not isinstance(decoded_base64_authorization_header, str)):
            return result

        if (':' not in decoded_base64_authorization_header):
            return result

        result = tuple(decoded_base64_authorization_header.split(":"))

        return result

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Get a user from DB if the credentials match

        Args:
            user_email (str): Email of the user
            user_pwd (str): Password of the user

        Returns:
            TypeVar('User'): A User from the database,
            None if The user not exist, or the password
            isn't valid
        """

        if ((not user_email) or (not isinstance(user_email, str))):
            return (None)

        if ((not user_pwd) or (not isinstance(user_pwd, str))):
            return (None)

        try:
            users = User.search({"email": user_email})
        except Exception:
            return (None)

        for user in users:
            if (user.is_valid_password(user_pwd)):
                return (user)

        return (None)
