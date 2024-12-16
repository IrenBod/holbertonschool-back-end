#!/usr/bin/python3
"""
Ce module crée une application Flask qui répond
à une requête HTTP GET sur la route '/'.

Fonctionnalités:
- Démarre un serveur web local sur l'hôte 0.0.0.0 et le port 5000.
- Répond à la route '/' avec un message "Hello HBNB!".
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """
    Vue associée à la route '/'.
    Retourne un message de bienvenue "Hello HBNB!" lorsqu'un
    utilisateur accède à cette route.
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
