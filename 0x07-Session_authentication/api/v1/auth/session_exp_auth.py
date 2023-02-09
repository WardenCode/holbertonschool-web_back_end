#!/usr/bin/env python3
"""
SessionExpAuth module
"""

from datetime import datetime, timedelta
from os import getenv
from typing import Optional

from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """
    SessionExpAuth Class

    Args:
        SessionAuth (SessionAuth): Father Class
    """

    def __init__(self):
        """
        Overload SessionAuth constructor
        Setting session_duration variable
        """
        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except (ValueError, TypeError, OverflowError):
            self.session_duration = 0

    def create_session(self, user_id: Optional[str] = None):
        """
        Create a session with expire time

        Args:
            user_id (str, optional): userID. Defaults to None.
        """
        session_id = super().create_session(user_id)

        if (not session_id):
            return (None)

        user_id = self.user_id_by_session_id.get(session_id)

        if (not user_id):
            return (None)

        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        return (session_id)

    def user_id_for_session_id(self, session_id=None):
        """
        Get User Dictionary with id and datetime

        Args:
            session_id (str, optional): sessionId. Defaults to None.

        Returns:
            Optional[str]: user_id otherwise None
        """

        if (not session_id):
            return (None)

        user_obj: Optional[str] = self.user_id_by_session_id.get(session_id)

        if (not user_obj):
            return (None)

        user_id = user_obj.get("user_id")

        if (not user_id):
            return (None)

        if (self.session_duration <= 0):
            return (user_id)

        created_at = user_obj.get("created_at")

        if (not created_at):
            return (None)

        if ((created_at + timedelta(seconds=self.session_duration))
                < datetime.now()):
            return (None)

        return (user_id)
