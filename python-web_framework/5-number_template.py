#!/usr/bin/python3
"""
This module creates a Flask web application with dynamic routes
and template rendering for specific routes.
"""

from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """
    View associated with the route '/'.
    Returns a welcome message "Hello HBNB!" when a user
    accesses this route.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Route '/hbnb'.
    Returns 'HBNB' when accessed.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Route handler for '/c/<text>'.
    Takes a dynamic variable 'text', replaces underscores with spaces,
    and returns a formatted string.
    """
    return f"C {text.replace('_', ' ')}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """
    Route '/python/' and '/python/<text>'.
    Returns 'Python <text>' where underscores are replaced with spaces.
    Default value of 'text' is 'is cool'.
    """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Route '/number/<n>'.
    Displays '<n> is a number' only if 'n' is an integer.
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Route '/number_template/<n>'.
    Displays an HTML page with '<h1>Number: n</h1>' if 'n' is an integer.
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    # Run the Flask development server on host 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
