import unittest
import datetime

from app.main import db
from app.main.model.credential import Credential
from app.test.base import BaseTestCase


class TestCredential(BaseTestCase):
    def setUp(self):
        super(TestCredential, self).setUp()
        self.creds = Credential(
            client='client',
            secret_hash='secret',
            super_cred=0,
        )
        db.session.add(self.creds)
        db.session.commit()

    def test_encode_token(self):
        token = Credential.encode_token(self.creds.id)
        self.assertTrue(isinstance(token, bytes))

    def test_decode_auth_token(self):
        expected = self.creds.id
        token = Credential.encode_token(self.creds.id)
        actual = Credential.decode_token(token.decode("utf-8"))
        self.assertEqual(expected, actual)

    def test_secret_cant_be_read(self):
        with self.assertRaises(AttributeError):
            self.creds.secret

if __name__ == '__main__':
    unittest.main()
