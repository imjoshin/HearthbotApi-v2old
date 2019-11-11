from flask_restplus import Namespace, fields


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


class SyncDto:
    api = Namespace('sync', description='sync related operations')
    card = api.model('sync_details', {})
