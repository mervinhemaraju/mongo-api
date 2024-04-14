from functools import wraps
from flask import request, abort


def require_credentials(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data = request.get_json()
        if not data or "username" not in data or "password" not in data:
            abort(400, description="Missing username or password")
        return f(*args, **kwargs)

    return decorated
