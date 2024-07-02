#!/usr/bin/env python3
"""
A Basic Flask app with Babel localization.

This app renders a simple page using Flask and serves it at the
root URL ("/").
It supports language localization based on user preferences.

Usage:
1. Run the app: `python app.py`
2. Access the home page: http://localhost:5000/
3. Append "?locale=en" or "?locale=fr" to the URL to set the language.

Supported languages: English (en), French (fr).
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

# Sample user data (for demonstration purposes)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Babel configuration."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    """
    Renders the home page.

    Returns:
        str: HTML content for the welcome page.
    """
    return render_template('5-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages.
    Detects if the incoming request contains a locale parameter.

    Returns:
        str: The best-matching language based on user preferences.
    """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """
    Retrieves user information based on the "login_as" query parameter.

    Returns:
        Union[dict, None]: A user dictionary or None if not found.
    """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """
    Finds a user (if any) and stores it in the global context (g.user).
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
