#!/usr/bin/env python3
"""
Flask app

This app renders a welcome page using Flask and serves it at the
root URL ("/").
"""

from flask_babel import Babel
from flask import Flask, render_template, request


class Config(object):
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Select and return the best language match based on supported languages.

    Returns:
        str: The best-matching language based on user preferences.
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the home/index page.

    Returns:
        str: HTML content for the welcome page.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
