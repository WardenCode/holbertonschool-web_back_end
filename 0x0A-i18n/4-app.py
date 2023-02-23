#!/usr/bin/env python3
"""
4. Force locale with URL parameter
"""

from typing import List, Optional

from flask import Flask, g, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


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
    if language and (language in Config.LANGUAGES):
        return language

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def main_page():
    """
    Endpoint for the main page
    """
    return (render_template('3-index.html'))


if (__name__ == '__main__'):
    app.run(debug=True)
