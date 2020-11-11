#!/usr/bin/env python3
"""
session authentication - view
"""
from flask import jsonify, request, abort
from models.user import User
from api.v1.views import app_views
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    send and check login data
    """
    u_email = request.form.get('email')
    if not u_email:
        return jsonify({"error": "email missing"}), 400

    u_pwd = request.form.get('password')
    if not u_pwd:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({"email": u_email})
    except BaseException:
        return jsonify({"error": "no user found for this email"}), 404

    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for u in users:
        if not u.is_valid_password(u_pwd):
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        s_id = auth.create_session(u.id)
        r = jsonify(u.to_json())
        r.set_cookie(getenv('SESSION_NAME'), s_id)
        return r
    return jsonify({"error": "no user found for this email"}), 404


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def delete():
    """
    remove a session
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
