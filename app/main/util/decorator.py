from functools import wraps
from flask import request
from app.main.service.authentication_service import AuthenticationService


def authorization_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authorized_credentials = AuthenticationService.get_credentials(request)

        if not authorized_credentials:
            data = {
                "status": "fail",
                "code": 401
            }
            return data, 401

        request.credentials = authorized_credentials
        return f(*args, **kwargs)

    return decorated
