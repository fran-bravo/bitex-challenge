import base64
import unittest
from unittest.mock import MagicMock
from src.services.identification_service import IdentificationService
from src.services.seed_service import SeedService
from src.api.factories.seed_factory import SeedFactory
from src.api.models.issue import Issue


class TestIdentificationService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = MagicMock()
        seed_factory = SeedFactory()
        seed_service = SeedService(cls.api, seed_factory)
        cls.identification_service = IdentificationService(seed_service)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_create(self):
        mocked_stream = MagicMock()
        mocked_file = MagicMock(
            stream=mocked_stream,
            filename='attachment.png',
            mimetype='image/png',
            content_length=10
        )
        identification_data = {
            'kind_code': 'national_id',
            'issuer': 'AR',
            'number': '11111111'
        }
        files = [mocked_file, mocked_file]

        base64.b64encode = MagicMock(return_value='encoded')
        issue = Issue(1)
        issue.id = 2

        self.api.create_identification_seed = MagicMock(return_value=3)
        self.api.create_attachments = MagicMock()
        self.api.create_attachments.side_effect = [4, 5]

        seed, attachment_seeds = self.identification_service.create(identification_data, files, issue.id)

        self.assertEqual(seed.id, 3, 'Should have id 3')
        self.assertEqual(seed.kind_code, 'national_id', 'Should be national_id')
        self.assertEqual(attachment_seeds[0].id, 4, 'Should have id 4')
        self.assertEqual(attachment_seeds[0].issue_id, issue.id, 'Should have issue with id 2')
        self.assertEqual(attachment_seeds[1].id, 5, 'Should have id 5')
        self.assertEqual(attachment_seeds[1].issue_id, issue.id, 'Should have issue with id 2')


if __name__ == '__main__':
    unittest.main()
