import time
from functools import wraps
from flask import request
from app.main.service.authentication_service import AuthenticationService


def authorization_required(super_cred=False):
    def inner(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            authorized_credentials = AuthenticationService.get_credentials(request)

            if not authorized_credentials or (super_cred and not authorized_credentials.super_cred):
                data = {
                    "status": "fail",
                    "code": 401
                }
                return data, 401

            request.credentials = authorized_credentials
            return f(*args, **kwargs)

        return wrapper
    return inner


def timed_response(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        response, code = f(*args, **kwargs)
        end = time.time()

        response['took'] = end - start

        return response, code

    return wrapper
