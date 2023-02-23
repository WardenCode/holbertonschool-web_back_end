#!/usr/bin/env python3
"""
3. Parametrize templates
"""

from typing import List, Optional

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class for available languages
    """
    LANGUAGES: List[str] = ['en', 'fr']


app.config.from_object(Config)

babel.default_locale = 'en'
babel.default_timezone = 'UTC'


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    Get the best match in LANGUAGES variable.

    Returns:
        Optional[str]: The best match in LANGUAGES variable
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def main_page():
    """
    Endpoint for the main page
    """
    return (render_template('3-index.html'))


if (__name__ == '__main__'):
    app.run(debug=True)
