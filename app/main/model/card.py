from sqlalchemy.orm import relationship

from .. import db

class Card(db.Model):
    """Model for cards."""

    __tablename__ = "card"
    id = db.Column(db.String(32), primary_key=True, unique=True)
    artist = db.Column(db.String(128), nullable=True)
    attack = db.Column(db.Integer, nullable=True)
    classes = db.Column(db.String(128), nullable=False)
    collectible = db.Column(db.Boolean, nullable=False)
    cost = db.Column(db.Integer, nullable=True)
    dbfid = db.Column(db.Integer, nullable=False, unique=True)
    flavor = db.Column(db.Text, nullable=True)
    health = db.Column(db.Integer, nullable=True)
    name = db.Column(db.Text, nullable=False)
    rarity = db.Column(db.Integer, nullable=True)
    set_id = db.Column(db.String(32), nullable=False)
    text = db.Column(db.Text, nullable=True)
    type = db.Column(db.Integer, nullable=True)
    tribes = db.Column(db.Text, nullable=True)
    translations = db.relationship("CardTranslation")

    def __repr__(self):
        return "<Card {}>".format(self.id)


class CardTranslation(db.Model):
    """Model for card name translations."""

    __tablename__ = "card_translation"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    card_id = db.Column(db.String(32), db.ForeignKey('card.id'))
    locale = db.Column(db.String(8), nullable=False)
    name = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return "<CardTranslation {} ({}-{})>".format(self.id, self.card_id, self.locale)


class CardSet(db.Model):
    """Model for card sets."""
    __tablename__ = "card_set"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    api_name = db.Column(db.String(64))
    name = db.Column(db.String(128))
    release_date = db.Column(db.Date)
    shortname = db.Column(db.String(8))

    def __repr__(self):
        return "<CardSet {}>".format(self.id)
