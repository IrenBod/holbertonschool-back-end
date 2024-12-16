#!/usr/bin/python3
"""
Ce module cree une application Flask qui repond
a une requete HTTP GET sur la route '/'.

Fonctionnalites:
- Demarre un serveur web local sur l hote 0.0.0.0 et le port 5000.
- Repond a la route '/' avec un message "Hello HBNB!".
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """
    Vue associee a la route '/'.
    Retourne un message de bienvenue "Hello HBNB!" lorsqu un
    utilisateur accede a cette route.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
