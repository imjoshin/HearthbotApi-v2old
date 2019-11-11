from flask import request
from flask_restplus import Resource

from ..util.decorator import authorization_required
from ..util.dto import CardDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = CardDto.api


@api.route('/')
class CardList(Resource):

    @api.doc('list_of_cards')
    @authorization_required
    @api.marshal_list_with(CardDto.card, envelope='data')
    def get(self):
        """List all cards"""
        print(request.credentials)
        return []
