from flask import request
from flask_restplus import Resource

from app.main.service.authentication_service import AuthenticationService
from ..util.dto import AuthDto

api = AuthDto.api


@api.route('/')
class AuthHandler(Resource):
    """
        Credentials Resource
    """
    @api.doc('user login')
    @api.expect(AuthDto.auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return AuthenticationService.get_token(data=post_data)
