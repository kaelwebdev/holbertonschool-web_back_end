#!/usr/bin/env python3
"""
core app
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """
    test function
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def reg_user() -> str:
    """
    new user
    """
    try:
        email = request.form['email']
        pwd = request.form['password']
    except KeyError:
        abort(400)
    try:
        user = AUTH.register_user(email, pwd)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    Login auth
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    if not AUTH.valid_login(email, pwd):
        abort(401)
    s_id = AUTH.create_session(email)
    r = jsonify({"email": email, "message": "logged in"})
    r.set_cookie("session_id", s_id)
    return r


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    destroy session and redirect
    """
    s_id = request.cookies.get("session_id")
    try:
        u = AUTH.get_user_from_session_id(s_id)
        AUTH.destroy_session(u.id)
        return redirect("/")
    except Exception:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """
    find profile user in db
    """
    s_id = request.cookies.get('session_id')
    try:
        u = AUTH.get_user_from_session_id(s_id)
        return jsonify({"email": u.email}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """
    new reset password token
    """
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """
    Update password for user endpoint
    """
    email = request.form.get("email")
    token = request.form.get("reset_token")
    new_pwd = request.form.get("new_password")
    try:
        AUTH.update_password(token, new_pwd)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
