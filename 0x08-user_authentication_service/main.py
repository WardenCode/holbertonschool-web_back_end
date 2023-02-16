#!/usr/bin/env python3
"""
Main module (Test End to End)
"""
from json import loads
from typing import Dict

from requests import Response, delete, get, post, put

BASE_URL = "http://localhost:5000/"
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """
    Test the register user endpoint

    Args:
        email (str): User email
        password (str): User password
    """
    data: Dict[str, str] = {
        "email": email,
        "password": password
    }

    response: Response = post("{:s}users".format(BASE_URL), data)

    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Test the login endpoint with wrong password

    Args:
        email (str): User email
        password (str): User password
    """
    data: Dict[str, str] = {
        "email": "wrong_email@gmail.com",
        "password": "incorrect_password"
    }

    response: Response = post("{:s}sessions".format(BASE_URL), data)

    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    Test the login endpoint with correct arguments

    Args:
        email (str): User email
        password (str): User password

    Returns:
        str: User session id
    """
    data: Dict[str, str] = {
        "email": email,
        "password": password
    }

    response: Response = post("{:s}sessions".format(BASE_URL), data)

    assert response.status_code == 200

    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """
    Test profile endpoint when the user is unlogged
    """
    response: Response = get("{:s}profile".format(BASE_URL))

    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    Test the profile endpoint when the user is logged

    Args:
        session_id (str): User session_id
    """
    cookies: Dict[str, str] = {
        "session_id": session_id,
    }

    response: Response = get("{:s}profile".format(BASE_URL), cookies=cookies)

    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """
    Test logout endpoint

    Args:
        session_id (str): User session_id
    """
    cookies: Dict[str, str] = {
        "session_id": session_id,
    }

    response: Response = delete(
        "{:s}sessions".format(BASE_URL), cookies=cookies)

    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """
    Test reset password token endpoint

    Args:
        email (str): User email

    Returns:
        str: user reset token
    """
    data: Dict[str, str] = {
        "email": email,
    }

    response: Response = post("{:s}reset_password".format(BASE_URL), data)

    assert response.status_code == 200

    return loads(response.content).get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Test update password endpoint

    Args:
        email (str): User email
        reset_token (str): User reset token
        new_password (str): User new password
    """
    data: Dict[str, str] = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password,
    }

    response: Response = put("{:s}reset_password".format(BASE_URL), data)

    assert response.status_code == 200


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
