import base64
import unittest
from unittest.mock import MagicMock
from src.services.domicile_service import DomicileService
from src.services.seed_service import SeedService
from src.api.factories.seed_factory import SeedFactory
from src.api.models.issue import Issue


class TestDomicileService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = MagicMock()
        seed_factory = SeedFactory()
        seed_service = SeedService(cls.api, seed_factory)
        cls.domicile_service = DomicileService(seed_service)

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
        domicile_data = {
            'city': 'ciudad',
            'country': 'AR',
            'postal_code': '1111',
            'street_address': 'calle',
            'street_number': '1234',
            'floor': '4'
        }

        base64.b64encode = MagicMock(return_value='encoded')
        issue = Issue(1)
        issue.id = 2

        self.api.create_domicile_seed = MagicMock(return_value=3)
        self.api.create_attachments = MagicMock()
        self.api.create_attachments.side_effect = [4]

        seed, attachment_seed = self.domicile_service.create(domicile_data, mocked_file, issue)

        self.assertEqual(seed.id, 3, 'Should have id 3')
        self.assertEqual(seed.city, 'ciudad', 'Should be ciudad')
        self.assertEqual(attachment_seed.id, 4, 'Should have id 4')
        self.assertEqual(attachment_seed.issue_id, issue.id, 'Should have issue with id 2')


if __name__ == '__main__':
    unittest.main()
