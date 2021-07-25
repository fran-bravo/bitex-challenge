import unittest
from src.validators.registration_validator import RegistrationValidator
from src.exceptions.missing_argument_exception import MissingArgumentException
from src.exceptions.wrong_date_format_exception import WrongDateFormatException


class TestRegistrationValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.registration_validator = RegistrationValidator()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_validate_ok(self):
        user_data = {
            'firstName': 'Test',
            'lastName': 'User',
            'birthDate': '2003-07-02',
            'country': 'AR',
        }

        self.registration_validator.validate(user_data)

    def test_validate_missing_required_argument(self):
        user_data = {
            'firstName': 'Test',
            'lastName': 'User',
            'birthDate': '2003-07-02',
        }

        self.assertRaises(MissingArgumentException, self.registration_validator.validate, user_data)

    def test_validate_wrong_date_format(self):
        user_data = {
            'firstName': 'Test',
            'lastName': 'User',
            'birthDate': '02/07/2003',
            'country': 'AR',
        }

        self.assertRaises(WrongDateFormatException, self.registration_validator.validate, user_data)


if __name__ == '__main__':
    unittest.main()
