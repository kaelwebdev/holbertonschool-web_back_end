#!/usr/bin/env python3
"""
core app
"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """
    test function
    """
    return jsonify({"message": "Bienvenue"})


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    new user
    """
    email = request.form.get('email')
    pwd = request.form('password')
    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": email}, {"message", "user created"}), 200
    except Exception:
        return jsonify({"message", "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
