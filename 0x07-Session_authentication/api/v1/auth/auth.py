#!/usr/bin/env python3
"""
Auth module for the application
"""

from os import getenv
from typing import List, Optional

from models.user import User


class Auth():
    """
    Auth class for the application
    """

    def require_auth(self, path: Optional[str],
                     excluded_paths: Optional[List[str]]) -> bool:
        """
        Validate if the path require auth or not

        Args:
            path (Optional[str]): Path to test
            excluded_paths (Optional[List[str]]): Paths that doesn't need auth

        Returns:
            bool: True if the path is not in the list of strings
            excluded_paths, False otherwise
        """

        if ((not path) or (not excluded_paths) or (not len(excluded_paths))):
            return (True)

        if (path[-1] != '/'):
            path = path + '/'

        for excluded_path in excluded_paths:
            if (excluded_path.endswith("*") and excluded_path[:-1] in path):
                return (False)

        return (path not in excluded_paths)

    def authorization_header(self, request=None) -> Optional[str]:
        """
        Validate and get if the authorization header exists

        Args:
            request (Dict[str, str], optional): HTTP Header Dict.
            Defaults to None.

        Returns:
            str: value of the header request Authorization or
            None if not found
        """

        if (not request):
            return (None)

        return (request.headers.get("Authorization"))

    def current_user(self, request=None) -> User:
        """
        Nothing

        Args:
            request (Request, optional): Flask Request. Defaults to None.

        Returns:
            (User, optional): User from Database or None.
        """
        return (None)

    def session_cookie(self, request=None) -> Optional[str]:
        """
        Retrieve the session cookie

        Args:
            request (Request, optional): HTTP request from the Client.
            Defaults to None.
        """
        if (not request):
            return (None)

        return (request.cookies.get(getenv("SESSION_NAME") or ""))
