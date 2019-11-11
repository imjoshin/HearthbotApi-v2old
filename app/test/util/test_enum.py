import unittest
import datetime

from app.main.util import enum
from app.test.base import BaseTestCase

class TEST_ENUM:
    GOOD_VALUE = 0
    STILL_GOOD_VALUE = 1
    WOO_ANOTHER_ONE = 2
    DEFAULT = 3

class TestEnum(BaseTestCase):

    def setUp(self):
        super(TestEnum, self).setUp()

    def test_from_string_is_present(self):
        expected = TEST_ENUM.GOOD_VALUE
        actual = enum.from_string(TEST_ENUM, 'GOOD_VALUE')
        self.assertEqual(expected, actual)

    def test_from_string_is_present_using_list_one_value(self):
        expected = [TEST_ENUM.GOOD_VALUE]
        actual = enum.from_string(TEST_ENUM, ['GOOD_VALUE'])
        self.assertEqual(expected, actual)

    def test_from_string_is_present_using_list_multiple_values(self):
        expected = [
            TEST_ENUM.GOOD_VALUE,
            TEST_ENUM.STILL_GOOD_VALUE,
            TEST_ENUM.WOO_ANOTHER_ONE,
        ]
        actual = enum.from_string(TEST_ENUM, ['GOOD_VALUE', 'STILL_GOOD_VALUE', 'WOO_ANOTHER_ONE'])
        self.assertEqual(expected, actual)

    def test_from_string_is_not_present_no_default(self):
        expected = None
        actual = enum.from_string(TEST_ENUM, 'BAD_VALUE')
        self.assertEqual(expected, actual)

    def test_from_string_is_not_present_using_list_one_value(self):
        expected = [None]
        actual = enum.from_string(TEST_ENUM, ['BAD_VALUE'])
        self.assertEqual(expected, actual)

    def test_from_string_is_not_present_using_list_multiple_values(self):
        expected = [
            TEST_ENUM.GOOD_VALUE,
            None,
            TEST_ENUM.WOO_ANOTHER_ONE
        ]
        actual = enum.from_string(TEST_ENUM, ['GOOD_VALUE', 'BAD_VALUE', 'WOO_ANOTHER_ONE'])
        self.assertEqual(expected, actual)

    def test_from_string_is_not_present_with_default(self):
        expected = TEST_ENUM.DEFAULT
        actual = enum.from_string(TEST_ENUM, 'BAD_VALUE', default=TEST_ENUM.DEFAULT)
        self.assertEqual(expected, actual)

    def test_from_string_is_not_present_with_default_using_list_multiple_values(self):
        expected = [
            TEST_ENUM.GOOD_VALUE,
            TEST_ENUM.DEFAULT,
            TEST_ENUM.WOO_ANOTHER_ONE
        ]
        actual = enum.from_string(TEST_ENUM, ['GOOD_VALUE', 'BAD_VALUE', 'WOO_ANOTHER_ONE'], default=TEST_ENUM.DEFAULT)
        self.assertEqual(expected, actual)
