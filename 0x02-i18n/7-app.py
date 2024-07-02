#!/usr/bin/env python3
"""
A Basic Flask app with Babel localization.

This app renders a simple page using Flask and serves it at the
root URL ("/").
It supports language localization based on user preferences and detects
timezones.

Usage:
1. Run the app: `python app.py`
2. Access the home page: http://localhost:5000/
3. Append "?locale=en" or "?locale=fr" to the URL to set the language.
4. Append "?timezone=Europe/Paris" or "?timezone=US/Central" to set the
timezone.

Supported languages: English (en), French (fr).
"""

import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel

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
    return render_template('7-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages.
    Detects if the incoming request contains a locale parameter.

    Returns:
        str: The best-matching language based on user preferences.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    header_locale = request.headers.get('locale')
    if header_locale and header_locale in app.config['LANGUAGES']:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determines the best timezone based on user preferences.
    Detects if the incoming request contains a timezone parameter.

    Returns:
        str: The best-matching timezone.
    """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request() -> None:
    """
    Finds a user (if any) and stores it in the global context (g.user).
    """
    login_as = request.args.get('login_as')
    g.user = users.get(int(login_as)) if login_as else None


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
