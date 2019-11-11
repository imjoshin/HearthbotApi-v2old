from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.card_controller import api as card_ns
from .main.controller.sync_controller import api as sync_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Hearthbot API',
          version='1.0',
          # description=''
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(card_ns, path='/cards')
api.add_namespace(sync_ns, path='/sync')
