#!/usr/bin/env python3
"""
Basic Flask app.

This app renders a welcome page using Flask and serves it at the root
URL ("/").
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


def welcome() -> str:
    """
    Renders the welcome page.

    Returns:
        str: HTML content for the welcome page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
