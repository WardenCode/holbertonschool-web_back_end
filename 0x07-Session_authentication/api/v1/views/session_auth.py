#!/usr/bin/env python3
""" Module of Session Auth views
"""

from os import getenv
from typing import List, Optional

from flask import abort, jsonify, request

from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=["POST"], strict_slashes=False)
def login():
    """
    Self Descriptive
    """

    email: Optional[str] = request.form.get("email")

    if (not email):
        return (jsonify({"error": "email missing"}), 400)

    if (not request.form.get("password")):
        return (jsonify({"error": "password missing"}), 400)

    try:
        users: List[User] = User.search({"email": email})
    except Exception:
        return (jsonify({"error": "no user found for this email"}), 404)

    if (not users):
        return (jsonify({"error": "no user found for this email"}), 404)

    for user in users:
        if (user.is_valid_password(request.form.get("password"))):
            from api.v1.app import auth
            session_name = getenv("SESSION_NAME")

            response = jsonify(user.to_json())
            response.set_cookie(session_name, auth.create_session(user.id))
            return (response)

    return (jsonify({"error": "wrong password"}), 401)


@app_views.route('/auth_session/logout',
                 methods=["DELETE"], strict_slashes=False)
def logout():
    """
    Self Descriptive
    """
    from api.v1.app import auth

    if (not auth.destroy_session(request)):
        abort(404)

    return (jsonify({}), 200)
