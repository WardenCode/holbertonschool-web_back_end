#!/usr/bin/env python3
"""
App module
"""

from typing import Optional

from auth import Auth
from flask import Flask, abort, jsonify, redirect, request
from user import User

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome_page():
    """
    Route to welcome page
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def create_user():
    """
    Create user endpoint
    """
    form_data = request.form
    email = form_data.get("email")

    try:
        AUTH.register_user(email,
                           form_data.get("password"))
    except ValueError:
        return (jsonify({"message": "email already registered"}), 400)

    return jsonify({
        "email": email,
        "message": "user created"
    })


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """
    login / user_sessions endpoint
    """
    form_data = request.form
    email = form_data.get("email")

    if not AUTH.valid_login(email, form_data.get("password")):
        abort(401)

    session_id = AUTH.create_session(email)

    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """
    logout endpoint
    """
    session_id = request.cookies.get("session_id")

    if (session_id is None):
        abort(403)

    found_user: Optional[User] = AUTH.get_user_from_session_id(session_id)

    if (found_user is None):
        abort(403)

    AUTH.destroy_session(found_user.id)

    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """
    Get user profile
    """
    session_id = request.cookies.get("session_id")

    if (session_id is None):
        abort(403)

    found_user: Optional[User] = AUTH.get_user_from_session_id(session_id)

    if (found_user is None):
        abort(403)

    return (jsonify({"email": found_user.email}), 200)


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def reset_password():
    """
    Reset password token
    """
    email = request.form.get("email")
    reset_token: Optional[str] = None

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "reset_token": reset_token})


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password():
    """
    Update the user password
    """
    form_data = request.form

    email = form_data.get("email")
    reset_token = form_data.get("reset_token")

    try:
        AUTH.update_password(reset_token, form_data.get("new_password"))
    except ValueError:
        abort(403)

    return (jsonify({"email": email, "message": "Password updated"}), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
