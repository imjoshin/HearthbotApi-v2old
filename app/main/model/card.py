from .. import db

class Card(db.Model):
	"""Model for cards."""

	__tablename__ = "card"
	id = db.Column(db.String(32), primary_key=True, unique=True)
	artist = db.Column(db.String(128), nullable=True)
	attack = db.Column(db.Integer, nullable=False)
	classes = db.Column(db.String(128), nullable=False)
	collectible = db.Column(db.Boolean, nullable=False)
	cost = db.Column(db.Integer, nullable=False)
	dbfid = db.Column(db.Integer, nullable=False, unique=True)
	flavor = db.Column(db.Text, nullable=True)
	health = db.Column(db.Integer, nullable=False)
	name = db.Column(db.Text, nullable=False)
	rarity = db.Column(db.Integer, nullable=False)
	set = db.Column(db.String(64), nullable=False)
	text = db.Column(db.Text, nullable=True)
	type = db.Column(db.Integer, nullable=False)
	tribes = db.Column(db.Text, nullable=True)

	def __repr__(self):
		return "<Card {}>".format(self.id)
