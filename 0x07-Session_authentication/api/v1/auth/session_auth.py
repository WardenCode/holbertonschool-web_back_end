#!/usr/bin/env python3
"""
Session Auth Module
"""

from typing import Dict, Optional
from uuid import uuid4

from api.v1.auth.auth import Auth


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
