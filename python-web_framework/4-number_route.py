#!/usr/bin/python3
"""
This module creates a Flask web application that responds
to an HTTP GET request on the route '/'.

Features:
- Starts a local web server on host 0.0.0.0 and port 5000.
- Responds to the route '/' with the message "Hello HBNB!".
"""

from flask import Flask

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
    return "HBNB"


"""
    Vue associée à la route '/hbnb'.
    Retourne le message "HBNB" lorsqu'un utilisateur accède à cette route.

    strict_slashes=False permet à la route de fonctionner avec ou
    sans le slash final ('/hbnb' ou '/hbnb/').
    """


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Route handler for '/c/<text>'.

    This function takes a dynamic variable 'text' from the URL, replaces any
    underscores ('_') with spaces (' '), and returns a formatted string.

    Args:
        text (str): The dynamic part of the URL, which is a string that may
                    include underscores.

    Returns:
        str: A string in the format "C <text>", where underscores are replaced
             with spaces.

    Example:
        - URL: /c/is_fun
          Response: "C is fun"

        - URL: /c/cool
          Response: "C cool"
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


if __name__ == "__main__":
    # Run the Flask development server on host 0.0.0.0 and port 5000
    app.run(host="0.0.0.0", port=5000)
