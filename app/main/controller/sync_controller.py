from flask import request
from flask_restplus import Resource

from ..util.decorator import authorization_required
from ..util.dto import SyncDto
from ..service.sync_service import SyncService

api = SyncDto.api


@api.route('/')
class SyncController(Resource):

    @api.doc('run_sync')
    @authorization_required(super_cred=True)
    def post(self):
        """ Sync card data """
        data = request.json
        return SyncService.run_sync(data)
