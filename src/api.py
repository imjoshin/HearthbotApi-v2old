from flask import Flask
from flask_restful import Api, Resource
from cards import handlers as card_handlers

app = Flask(__name__)
api = Api(app)

class RootHandler(Resource):
	def get(self):
		return {'status': 'ok'}

api.add_resource(RootHandler, '/')
api.add_resource(card_handlers.Cards, '/cards/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8081, debug=True)
