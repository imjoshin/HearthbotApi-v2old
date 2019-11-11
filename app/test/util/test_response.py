import unittest
import datetime
from http import HTTPStatus

from app.main.util.response import Response
from app.test.base import BaseTestCase

class TestResponse(BaseTestCase):

    def setUp(self):
        super(TestResponse, self).setUp()

    def test_basic_response(self):
        response_dict = {'status': 'ok', 'result': 'all good', 'code': HTTPStatus.OK}
        expected = (response_dict, response_dict['code'])
        response = Response('all good')
        actual = response.flask
        self.assertEqual(expected, actual)

    def test_basic_response_no_body(self):
        response_dict = {'status': 'ok', 'code': HTTPStatus.OK}
        expected = (response_dict, response_dict['code'])
        response = Response(None)
        actual = response.flask
        self.assertEqual(expected, actual)

    def test_basic_error_response(self):
        response_dict = {'status': 'failed', 'error': 'sumthin broke', 'code': HTTPStatus.BAD_REQUEST}
        expected = (response_dict, response_dict['code'])
        response = Response('sumthin broke', code=HTTPStatus.BAD_REQUEST)
        actual = response.flask
        self.assertEqual(expected, actual)

    def test_basic_error_response_no_body(self):
        response_dict = {'status': 'failed', 'error': 'Unknown error', 'code': HTTPStatus.BAD_REQUEST}
        expected = (response_dict, response_dict['code'])
        response = Response(None, code=HTTPStatus.BAD_REQUEST)
        actual = response.flask
        self.assertEqual(expected, actual)
