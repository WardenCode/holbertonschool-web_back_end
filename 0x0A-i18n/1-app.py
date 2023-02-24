#!/usr/bin/env python3
"""
1. Basic Babel setup
"""

from typing import List

from flask import Flask, render_template
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


@app.route('/', strict_slashes=False)
def main_page():
    """
    Endpoint for the main page
    """
    return (render_template('1-index.html'))


if (__name__ == '__main__'):
    app.run()
