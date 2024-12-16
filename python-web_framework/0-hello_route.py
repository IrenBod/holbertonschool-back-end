#!/usr/bin/python3
"""
This module creates a Flask web application that responds
to an HTTP GET request on the route '/'.

Features:
- Starts a local web server on host 0.0.0.0 and port 5000.
- Responds to the route '/' with the message "Hello HBNB!".
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """
    View associated with the route '/'.
    Returns a welcome message "Hello HBNB!" when a user
    accesses this route.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
