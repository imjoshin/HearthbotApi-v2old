from .. import db
from flask import current_app as app
import flask_bcrypt
import jwt
import datetime

class Credential(db.Model):
    """Model for credentials."""

    __tablename__ = "credential"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    client = db.Column(db.String(128), nullable=False, unique=True)
    secret_hash = db.Column(db.String(256), nullable=False)
    token = db.Column(db.String(128), nullable=True)
    super_cred = db.Column(db.Boolean, nullable=False)
    token_expire = db.Column(db.DateTime, nullable=True)
    cred_expire = db.Column(db.DateTime, nullable=True)

    @property
    def secret(self):
        raise AttributeError('password: write-only field')

    @secret.setter
    def secret(self, secret):
        self.secret_hash = flask_bcrypt.generate_password_hash(secret).decode('utf-8')

    def check_secret(self, secret):
        return flask_bcrypt.check_password_hash(self.secret_hash, secret)

    @staticmethod
    def encode_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            app.config["SECRET_KEY"],
            algorithm='HS256'
        )

    @staticmethod
    def decode_token(token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(token, app.config["SECRET_KEY"])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please re-authorize.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please re-authorize.'

    def __repr__(self):
        return "<Credential {}>".format(self.id)
