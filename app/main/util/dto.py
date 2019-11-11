from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operation')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    auth = api.model('auth_details', {
        'client': fields.String(required=True, description='The client id'),
        'secret': fields.String(required=True, description='The client secret'),
    })


class CardDto:
    api = Namespace('card', description='card related operations')
    card = api.model('card_details', {
        'name': fields.String(required=True, description='The card name'),
    })
