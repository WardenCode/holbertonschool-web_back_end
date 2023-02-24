#!/usr/bin/env python3
"""
5. Mock logging in
"""

from typing import Dict, List, Optional

from flask import Flask, g, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

User = Dict[str, Optional[str]]
users: Dict[int, User] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[User]:
    """
    Retrieve a user

    Returns:
        Optional[User]: Return a user if it exists
        None otherwise
    """
    login_as: Optional[str] = request.args.get("login_as", "")
    user: Optional[User] = None

    if (login_as.isdigit()):
        user = users.get(int(login_as))

    return user


class Config(object):
    """
    Config class for available languages
    """
    LANGUAGES: List[str] = ['en', 'fr']


app.config.from_object(Config)

Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Get the best match in LANGUAGES variable or
    use the language of the user.

    Returns:
        Optional[str]: The best match in LANGUAGES variable
    """
    language: Optional[str] = request.args.get("locale")
    if language:
        return language

    return request.accept_languages.best_match(Config.LANGUAGES)


@app.before_request
def before_all():
    """
    Validate if login_as query param
    matches with a user
    """
    user = get_user()
    g.user = user
    # g.user = get_user()


@app.route('/', strict_slashes=False)
def main_page():
    """
    Endpoint for the main page
    """
    return (render_template('5-index.html'))


if (__name__ == '__main__'):
    app.run(debug=True)
