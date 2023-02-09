#!/usr/bin/env python3
""" User Session module
"""

from sys import stderr

from models.base import Base


class UserSession(Base):
    """
    UserSession class for the application

    Args:
        Base (Base): Main Base class
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Define the instance attributes
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
