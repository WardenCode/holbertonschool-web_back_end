#!/usr/bin/env python3
"""
Session Auth Module
"""

from typing import Dict, Optional
from uuid import uuid4

from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """
    Session Auth class for the application

    Args:
        Auth (Auth): Main auth class
    """

    user_id_by_session_id: Dict[str, str] = {}

    def create_session(self, user_id: Optional[str] = None) -> Optional[str]:
        """
        Take a userID and creates a session

        Args:
            user_id (str, optional): UserID. Defaults to None.

        Returns:
            str: Session ID
        """
        if ((not isinstance(user_id, str)) or (not user_id)):
            return (None)

        Base: str = str(uuid4())

        self.user_id_by_session_id[Base] = user_id

        return (Base)

    def user_id_for_session_id(
            self, session_id: Optional[str] = None) -> Optional[str]:
        """
        Retrieve a userID through sessionID

        Args:
            session_id (Optional[str], optional): SessionID
            Defaults to None.

        Returns:
            Optional[str]: UserID that match with SessionID, None otherwise
        """

        if ((not isinstance(session_id, str)) or (not session_id)):
            return (None)

        return (self.user_id_by_session_id.get(session_id))

    def current_user(self, request=None) -> User:
        """
        Based on sessionID get the assosiated user

        Args:
            request (Request, optional): Flask Request.
            Defaults to None.

        Returns:
            User: Current User
        """

        session_cookie = self.session_cookie(request)

        user_id = self.user_id_for_session_id(session_cookie)

        return (User.get(user_id or ""))

    def destroy_session(self, request=None) -> bool:
        """
        Delete a session

        Args:
            request (Request, optional): Flask Request.
            Defaults to None.

        Returns:
            (bool): True if session is deleted, False
            otherwise
        """

        if (not request):
            return (False)

        session_cookie = self.session_cookie(request)

        if (not session_cookie):
            return (False)

        user_id = self.user_id_for_session_id(session_cookie)

        if (not user_id):
            return (False)

        del self.user_id_by_session_id[session_cookie]
        return (True)
