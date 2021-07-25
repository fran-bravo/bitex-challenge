import unittest
from src.validators.domicile_validator import DomicileValidator
from src.exceptions.missing_argument_exception import MissingArgumentException


class TestDomicileValidator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.domicile_validator = DomicileValidator()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_validate_user_ok(self):
        domicile_data = {
            'domicile': {},
            'files': [],
            'issue': {}
        }

        self.domicile_validator.validate(domicile_data)

    def test_validate_user_missing_required_argument(self):
        domicile_data = {
            'domicile': {},
            'files': []
        }

        self.assertRaises(MissingArgumentException, self.domicile_validator.validate, domicile_data)


if __name__ == '__main__':
    unittest.main()
