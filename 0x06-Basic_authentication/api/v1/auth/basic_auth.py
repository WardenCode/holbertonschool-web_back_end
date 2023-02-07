#!/usr/bin/env python3
"""
Basic Auth Module
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Empty class of a Basic Auth

    Args:
        Auth (Auth): Main auth class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
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
