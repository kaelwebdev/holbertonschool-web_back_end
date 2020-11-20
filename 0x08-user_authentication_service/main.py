#!/usr/bin/env python3
"""
this file is used to test
the implemented functions
examples with terminal:
* curl -XPOST localhost:5000/users -d 'email=bob@bob.com'
-d 'password=mySuperPwd'

* curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com'
-d 'password=mySuperPwd' -v

* curl -XGET localhost:5000/profile -b "session_id=123"

* curl -XPOST localhost:5000/reset_password -d 'email=bob@bob.com'

* curl -XPOST localhost:5000/reset_password -d 'email=bob@bob.com'
-d 'reset_token=789' -d 'new_password=abc'
"""


import requests


def register_user(email: str, password: str) -> None:
    """
    register new user
    """
    r = requests.post('http://127.0.0.1:5000/users', data={
        'email': email,
        'password': password
    })
    assert r.status_code == 200
    assert r.json() == {'email': email, 'message': "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    login with wrong pwd
    """
    r = requests.post('http://127.0.0.1:5000/sessions', data={
        'email': email,
        'password': password
    })
    assert r.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    login with right pwd
    """
    r = requests.post('http://127.0.0.1:5000/sessions', data={
        'email': email,
        'password': password
    })
    assert r.status_code == 200
    assert r.json() == {'email': email, 'message': "logged in"}
    return r.cookies.get('session_id')


def profile_unlogged() -> None:
    """
    test if session_id = none
    """
    r = requests.get('http://127.0.0.1:5000/profile')
    assert r.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    test if we have session_id
    """
    r = requests.get('http://127.0.0.1:5000/profile', cookies={
        'session_id': session_id
    })
    assert r.status_code == 200
    assert r.json() == {'email': "guillaume@holberton.io"}


def log_out(session_id: str) -> None:
    """
    log out
    """
    r = requests.delete('http://127.0.0.1:5000/sessions', cookies={
        'session_id': session_id
    })
    for past_r in r.history:
        assert past_r.status_code == 302


def reset_password_token(email: str) -> str:
    """
    check pwd token
    """
    r = requests.post('http://127.0.0.1:5000/reset_password', data={
        'email': email,
    })
    assert r.status_code == 200
    return r.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    change password and put reset_token = None
    """
    r = requests.put('http://127.0.0.1:5000/reset_password', data={
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    })
    assert r.status_code == 200
    assert r.json() == {'email': email, 'message': "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
