#!/usr/bin/env python3
"""
App module
"""

from auth import Auth
from flask import Flask, jsonify, request

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
