#!/usr/bin/env python3
"""
App module
"""

from typing import Optional

from flask import Flask, abort, jsonify, request

from auth import Auth

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

    try:
        AUTH.register_user(form_data.get("email", ""),
                           form_data.get("password", ""))
        return (jsonify({"email": form_data.get("email"), "message": "user created"}))
    except ValueError:
        return (jsonify({"message": "email already registered"}), 400)


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
