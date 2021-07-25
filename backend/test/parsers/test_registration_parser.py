import unittest
from unittest.mock import MagicMock
from src.parsers.registration_parser import RegistrationParser


class TestRegistrationParser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user_parser = RegistrationParser()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_parse_request_ok(self):
        request_json = {
            'firstName': 'Test',
            'lastName': 'User',
            'birthDate': '2003-07-02',
            'country': 'AR'
        }
        mocked_request = MagicMock(json=request_json)

        parsed_user = self.user_parser.parse(mocked_request)
        self.assertEqual(parsed_user, request_json, 'Should be user data')


if __name__ == '__main__':
    unittest.main()
