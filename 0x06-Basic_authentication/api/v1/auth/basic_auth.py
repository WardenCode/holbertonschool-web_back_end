#!/usr/bin/env python3
"""
Basic Auth Module
"""

from base64 import b64decode
from sys import stderr

from api.v1.auth.auth import Auth


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
