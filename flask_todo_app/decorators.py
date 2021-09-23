from functools import wraps
from flask import g, request, redirect, session, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('userID') == None:
            return redirect(url_for('register'))

        return f(*args, **kwargs)
    return decorated_function