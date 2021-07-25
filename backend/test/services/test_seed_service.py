import unittest
from unittest.mock import MagicMock
from src.services.seed_service import SeedService
from src.api.factories.seed_factory import SeedFactory
from src.api.models.user import User
from src.api.models.seeds.natural_docket_seed import NaturalDocketSeed
from src.api.models.seeds.identification_seed import IdentificationSeed
from src.api.models.seeds.domicile_seed import DomicileSeed
from src.api.models.seeds.attachment_seed import AttachmentSeed


class TestSeedService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = MagicMock()
        cls.seed_factory = SeedFactory()
        cls.seed_service = SeedService(cls.api, cls.seed_factory)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_create_natural_docket(self):
        user = User('Test', 'User', '2003-07-02', 'AR')
        user.id = 1
        issue_id = 2
        self.api.create_natural_docket_seed = MagicMock(return_value=3)

        seed = self.seed_service.create_natural_docket(user, issue_id)

        self.assertEqual(seed.id, 3, 'Should have id 3')
        self.assertEqual(seed.issue_id, 2, 'Should have issue id 2')
        self.assertIsInstance(seed, NaturalDocketSeed)

    def test_create_identification(self):
        seed_data = {
            'kind_code': 'national_id',
            'issuer': 'AR',
            'number': '123456789'
        }
        issue_id = 2
        self.api.create_identification_seed = MagicMock(return_value=3)

        seed = self.seed_service.create_identification(seed_data, issue_id)

        self.assertEqual(seed.id, 3, 'Should have id 3')
        self.assertEqual(seed.issue_id, 2, 'Should have issue id 2')
        self.assertIsInstance(seed, IdentificationSeed)

    def test_create_domicile(self):
        seed_data = {
            'city': 'ciudad',
            'country': 'AR',
            'postal_code': '1111',
            'street_address': 'calle',
            'street_number': '1234',
            'floor': '4'
        }
        issue_id = 2
        self.api.create_domicile_seed = MagicMock(return_value=3)

        seed = self.seed_service.create_domicile(seed_data, issue_id)

        self.assertEqual(seed.id, 3, 'Should have id 3')
        self.assertEqual(seed.issue_id, 2, 'Should have issue id 2')
        self.assertIsInstance(seed, DomicileSeed)

    def test_create_attachments(self):
        mocked_file = MagicMock()
        mocked_seed = MagicMock()
        issue_id = 2
        self.api.create_attachments = MagicMock(return_value=3)

        seed = self.seed_service.create_attachments(mocked_file, mocked_seed, issue_id)

        self.assertEqual(seed.id, 3, 'Should have id 3')
        self.assertEqual(seed.issue_id, 2, 'Should have issue id 2')
        self.assertIsInstance(seed, AttachmentSeed)


if __name__ == '__main__':
    unittest.main()
