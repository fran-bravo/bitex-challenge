import unittest
from src.validators.domicile_validator import DomicileValidator
from src.exceptions.missing_argument_exception import MissingArgumentException


class TestUserValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.domicile_validator = DomicileValidator()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_validate_user_ok(self):
        domicile_data = {
            'streetAddress': 'Calle',
            'streetNumber': '1234',
            'city': 'Ciudad',
            'floor': '',
            'postalCode': '1111',
            'country': 'AR'
        }

        self.domicile_validator.validate(domicile_data)

    def test_validate_user_missing_required_argument(self):
        domicile_data = {
            'streetAddress': 'Calle',
            'streetNumber': '1234',
            'city': 'Ciudad',
            'floor': '',
            'country': 'AR'
        }

        self.assertRaises(MissingArgumentException, self.domicile_validator.validate, domicile_data)

    def test_validate_user_missing_optional_argument(self):
        domicile_data = {
            'streetAddress': 'Calle',
            'streetNumber': '1234',
            'city': 'Ciudad',
            'postalCode': '1111',
            'country': 'AR'
        }

        self.domicile_validator.validate(domicile_data)


if __name__ == '__main__':
    unittest.main()
