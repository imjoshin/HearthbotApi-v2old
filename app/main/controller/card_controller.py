from flask import request
from flask_restplus import Resource

from ..util.decorator import authorization_required
from ..util.dto import CardDto

api = CardDto.api


@api.route('/')
class CardList(Resource):

    @api.doc('list_of_cards')
    @authorization_required()
    @api.marshal_list_with(CardDto.card, envelope='data')
    def get(self):
        """List all cards"""
        return []
