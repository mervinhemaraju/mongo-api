import base64
from functools import wraps
from flask import request, abort


def require_credentials(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Retrieve the request headers
        headers = request.headers

        # ! Abort if Authorization is not present
        if "Authorization" not in headers:
            abort(401, description="Authentication failed.")

        # Retrieve thu auth
        auth = request.headers.get("Authorization").split(" ")[1]

        # Split to obtain credentials
        credentials = base64.b64decode(auth).decode("utf-8").split(":")

        # Retrieve the username and password
        username = credentials[0]
        password = credentials[1]

        # Set the kwargs
        kwargs["username"] = username
        kwargs["password"] = password

        return f(*args, **kwargs)

    return decorated
