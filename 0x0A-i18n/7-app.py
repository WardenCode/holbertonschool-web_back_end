#!/usr/bin/env python3
"""
6. Use user locale
"""

from typing import Dict, List, Optional, Union

from flask import Flask, g, render_template, request
from flask_babel import Babel
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError

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
    user_lang: Optional[str] = g.user.get('locale')
    header_lang: Optional[str] = request.headers.get('locale')

    if language and (language in Config.LANGUAGES):
        return language

    if (user_lang and (user_lang in Config.LANGUAGES)):
        return user_lang

    if (header_lang and (header_lang in Config.LANGUAGES)):
        return header_lang

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Get the best match in timezone variable or
    use the timezone of the user.

    Returns:
        _UTCclass | StaticTzInfo | DstTzInfo: The best match in timezone
    """
    selected_timezone = 'UTC'
    query_timezone: Optional[str] = request.args.get("timezone")
    user_timezone: Optional[str] = g.user.get('timezone')
    header_timezone: Optional[str] = request.headers.get('timezone')

    if query_timezone:
        selected_timezone = query_timezone
    elif user_timezone:
        selected_timezone = user_timezone
    elif header_timezone:
        selected_timezone = header_timezone

    try:
        selected_timezone = timezone(selected_timezone)
    except UnknownTimeZoneError:
        pass

    return selected_timezone


@app.before_request
def before_request():
    """
    Validate if login_as query param
    matches with a user
    """
    g.user = get_user()


@app.route('/', strict_slashes=False)
def main_page():
    """
    Endpoint for the main page
    """
    return (render_template('7-index.html'))


if (__name__ == '__main__'):
    app.run(debug=True)
