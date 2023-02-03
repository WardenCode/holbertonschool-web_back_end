#!/usr/bin/env python3
"""

"""

from bcrypt import checkpw, gensalt, hashpw


def hash_password(password: str) -> bytes:
    """
    Hash a password

    Args:
        password (str): Password to be hashed

    Returns:
        bytes: Password hashed and salted
    """
    return (hashpw(password.encode("utf-8"), gensalt()))


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate if a password match with hashed password

    Args:
        hashed_password (bytes): Hashed password
        password (str): Password to be evaluated

    Returns:
        bool: True if the password is valid, False otherwise
    """

    return (checkpw(password.encode("utf-8"), hashed_password))
