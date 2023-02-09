#!/usr/bin/env python3
"""
SesionDBAuth module
"""


from datetime import datetime, timedelta
from sys import stderr
from typing import List

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    SessionDBAuth class for the application

    Args:
        SessionExpAuth (SessionExpAuth): Main SessionExpAuth class
    """

    def create_session(self, user_id=None):
        """
        Create a session with expire time

        Args:
            user_id (str, optional): userID. Defaults to None.
        """
        session_id = super().create_session(user_id)

        if (not session_id):
            return (None)

        new_session = UserSession(
            **{'user_id': user_id, 'session_id': session_id}
        )
        new_session.save()
        UserSession.save_to_file()

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

        UserSession.load_from_file()
        users: List = UserSession.search({
            "session_id": session_id
        })

        if (not users):
            return (None)

        user = users[0]

        user_id = user.user_id

        if (not user_id):
            return (None)

        if (self.session_duration <= 0):
            return (user_id)

        created_at = user.created_at

        if (not created_at):
            return (None)

        if ((created_at + timedelta(seconds=self.session_duration))
                < datetime.utcnow()):
            return (None)

        return (user_id)

    def destroy_session(self, request=None):
        """
        Delete a session

        Args:
            request (Request, optional): Flask Request.
            Defaults to None.

        Returns:
            (bool): True if session is deleted, False otherwise
        """

        if (not request):
            return (False)

        session_cookie = self.session_cookie(request)

        if (not session_cookie):
            return (False)

        user_id = self.user_id_for_session_id(session_cookie)

        if (not user_id):
            return (False)

        user_session = UserSession.search({
            'session_id': session_cookie
        })

        if not user_session:
            return (False)

        user_session = user_session[0]

        try:
            user_session.remove()
            UserSession.save_to_file()
        except Exception:
            return (False)

        return (True)
