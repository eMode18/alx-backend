#!/usr/bin/env python3
"""
Basic Flask app.

This app renders a welcome page using Flask and serves it
at the root URL ("/").
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Config class for app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


def welcome() -> str:
    """
    Renders the welcome page.

    Returns:
        str: HTML content for the welcome page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
