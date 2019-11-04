from flask_restful import Resource

class Cards(Resource):
	def get(self):
		return ['cards']
