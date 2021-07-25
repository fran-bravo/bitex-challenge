import unittest
from unittest.mock import MagicMock
from src.api.factories.seed_factory import SeedFactory


class TestSeedFactory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.seed_factory = SeedFactory()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_natural_docket_creation(self):
        mocked_user = MagicMock(first_name='Test', last_name='User', country='AR', date_of_birth='2020-07-07')
        issue_id = 1
        seed = self.seed_factory.create_natural_docket(mocked_user, issue_id)
        self.assertEqual(seed.first_name, mocked_user.first_name, 'Should be Test')
        self.assertEqual(seed.last_name, mocked_user.last_name, 'Should be User')
        self.assertEqual(seed.nationality, mocked_user.country, 'Should be AR')
        self.assertEqual(seed.birth_date, mocked_user.date_of_birth, 'Should be 2020-07-07')
        self.assertEqual(seed.issue_id, issue_id, 'Should be 1')

    def test_identification_creation(self):
        issue_id = 1
        seed_data = {
            'kind_code': 'national_id',
            'issuer': 'AR',
            'number': '123456789'
        }
        seed = self.seed_factory.create_identification(seed_data, issue_id)
        self.assertEqual(seed.kind_code, 'national_id', 'Should be national_id')
        self.assertEqual(seed.issuer, 'AR', 'Should be AR')
        self.assertEqual(seed.number, '123456789', 'Should be 123456789')
        self.assertEqual(seed.issue_id, issue_id, 'Should be 1')

    def test_domicile_creation(self):
        issue_id = 1
        seed_data = {
            'city': 'ciudad',
            'country': 'AR',
            'postal_code': '1111',
            'street_address': 'calle',
            'street_number': '1234',
            'floor': '4'
        }
        seed = self.seed_factory.create_domicile(seed_data, issue_id)
        self.assertEqual(seed.city, 'ciudad', 'Should be ciudad')
        self.assertEqual(seed.country, 'AR', 'Should be AR')
        self.assertEqual(seed.postal_code, '1111', 'Should be 1111')
        self.assertEqual(seed.street_address, 'calle', 'Should be calle')
        self.assertEqual(seed.street_number, '1234', 'Should be 1234')
        self.assertEqual(seed.floor, '4', 'Should be 4')
        self.assertEqual(seed.issue_id, issue_id, 'Should be 1')

    def test_attachments_creation(self):
        mocked_file = MagicMock()
        mocked_seed = MagicMock()
        issue_id = 1
        seed = self.seed_factory.create_attachments(mocked_file, mocked_seed, issue_id)
        self.assertEqual(seed.file, mocked_file, 'Should be Mocked File')
        self.assertEqual(seed.included_seeds, mocked_seed, 'Should be Mocked Seed')
        self.assertEqual(seed.issue_id, issue_id, 'Should be 1')


if __name__ == '__main__':
    unittest.main()
