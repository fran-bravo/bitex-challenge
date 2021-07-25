import requests
import unittest
from unittest.mock import MagicMock
from src.api.bitex import Bitex
from src.api.exceptions.bitex_api_exception import BitexAPIException
from src.api.serializers.serializer_selector import SerializerSelector
from src.api.models.user import User
from src.api.models.issue import Issue
from src.api.models.seeds.natural_docket_seed import NaturalDocketSeed
from src.api.models.seeds.identification_seed import IdentificationSeed
from src.api.models.seeds.domicile_seed import DomicileSeed
from src.api.models.seeds.attachment_seed import AttachmentSeed


class TestBitex(unittest.TestCase):
    API_KEY = 'TEST_KEY'
    BITEX_CONFIG = {
        'base_url': 'https://bitextest.com',
        'users_endpoint': 'users',
        'issues_endpoint': 'issues',
        'natural_docket_seed_endpoint': 'natural_docket_seeds',
        'identification_seed_endpoint': 'identification_seeds',
        'domicile_seed_endpoint': 'domicile_seeds',
        'attachments_endpoint': 'attachments',
        'version': '0.0'
    }

    @classmethod
    def setUpClass(cls):
        cls.serializer_selector = SerializerSelector()
        cls.bitex_api = Bitex(TestBitex.API_KEY, TestBitex.BITEX_CONFIG, cls.serializer_selector)
        cls.mocked_headers = {
            'Content-Type': 'application/json',
            'Authorization': 'TEST_KEY',
            'Version': '0.0'
        }
        cls.mocked_domicile = MagicMock()
        cls.mocked_domicile.configure_mock(
            street_address='address', street_number='1234', city='city', floor='4', postal_code='1111', country='AR'
        )
        cls.user = User('Test', 'User', '2020-07-03', 'AR')
        cls.issue = Issue(11)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_list_users_ok(self):
        mocked_response = MagicMock(ok=True)
        requests.get = MagicMock(return_value=mocked_response)
        params = {
            'page': {
                'page': 0,
                'per_page': 10
            }
        }

        self.bitex_api.list_users()
        requests.get.assert_called_with('https://bitextest.com/users', headers=self.mocked_headers, json=params)

    def test_list_users_error(self):
        mocked_response = MagicMock(ok=False)
        requests.get = MagicMock(return_value=mocked_response)
        params = {
            'page': {
                'page': 0,
                'per_page': 10
            }
        }

        self.assertRaises(BitexAPIException, self.bitex_api.list_users)
        requests.get.assert_called_with('https://bitextest.com/users', headers=self.mocked_headers, json=params)

    def test_create_users_ok(self):
        serialized_user = MagicMock()
        user_serializer = MagicMock()
        user_serializer.serialize = MagicMock(return_value=serialized_user)
        self.serializer_selector['users'] = user_serializer
        response_text = '{"data":{"id":"11","type":"users","attributes":{}}}'
        mocked_response = MagicMock(ok=True, text=response_text)
        requests.post = MagicMock(return_value=mocked_response)

        self.assertEqual(self.user.id, None, 'Should have id None')
        user_id = self.bitex_api.create_user(self.user)

        requests.post.assert_called_with(
            'https://bitextest.com/users',
            headers=self.mocked_headers,
            json=serialized_user
        )
        self.assertEqual(user_id, '11', 'Should have id 11')

    def test_create_users_error(self):
        serialized_user = MagicMock()
        user_serializer = MagicMock()
        user_serializer.serialize = MagicMock(return_value=serialized_user)
        self.serializer_selector['users'] = user_serializer
        mocked_response = MagicMock(ok=False)
        requests.post = MagicMock(return_value=mocked_response)

        self.assertRaises(BitexAPIException, self.bitex_api.create_user, self.user)

    def test_create_issues_ok(self):
        serialized_issue = MagicMock()
        issue_serializer = MagicMock()
        issue_serializer.serialize = MagicMock(return_value=serialized_issue)
        self.serializer_selector['issues'] = issue_serializer
        response_text = '{"data":{"id":"22","type":"issues","attributes":{}}}'
        mocked_response = MagicMock(ok=True, text=response_text)
        requests.post = MagicMock(return_value=mocked_response)

        self.assertEqual(self.issue.id, None, 'Should have id None')
        issue_id = self.bitex_api.create_issue(self.issue)

        requests.post.assert_called_with(
            'https://bitextest.com/issues',
            headers=self.mocked_headers,
            json=serialized_issue
        )
        self.assertEqual(issue_id, '22', 'Should have id 22')

    def test_create_natural_docket_seed(self):
        seed = NaturalDocketSeed('Test', 'User', 'AR', '2020-07-03', 22)
        serialized_seed = MagicMock()
        seed_serializer = MagicMock()
        seed_serializer.serialize = MagicMock(return_value=serialized_seed)
        self.serializer_selector['natural_docket_seeds'] = seed_serializer
        response_text = '{"data":{"id":"33","type":"natural_docket_seeds","attributes":{}}}'
        mocked_response = MagicMock(ok=True, text=response_text)
        requests.post = MagicMock(return_value=mocked_response)

        self.assertEqual(seed.id, None, 'Should have id None')
        seed_id = self.bitex_api.create_natural_docket_seed(seed)

        requests.post.assert_called_with(
            'https://bitextest.com/natural_docket_seeds',
            headers=self.mocked_headers,
            json=serialized_seed
        )
        self.assertEqual(seed_id, '33', 'Should have id 33')

    def test_create_identification_seed(self):
        seed = IdentificationSeed('national_id', 'AR', '123456789', 22)
        serialized_seed = MagicMock()
        seed_serializer = MagicMock()
        seed_serializer.serialize = MagicMock(return_value=serialized_seed)
        self.serializer_selector['identification_seeds'] = seed_serializer
        response_text = '{"data":{"id":"33","type":"identification_seeds","attributes":{}}}'
        mocked_response = MagicMock(ok=True, text=response_text)
        requests.post = MagicMock(return_value=mocked_response)

        self.assertEqual(seed.id, None, 'Should have id None')
        seed_id = self.bitex_api.create_identification_seed(seed)

        requests.post.assert_called_with(
            'https://bitextest.com/identification_seeds',
            headers=self.mocked_headers,
            json=serialized_seed
        )
        self.assertEqual(seed_id, '33', 'Should have id 33')

    def test_create_domicile_seed(self):
        seed = DomicileSeed('ciudad', 'AR', '1111', 'calle', '1234', 22)
        serialized_seed = MagicMock()
        seed_serializer = MagicMock()
        seed_serializer.serialize = MagicMock(return_value=serialized_seed)
        self.serializer_selector['domicile_seeds'] = seed_serializer
        response_text = '{"data":{"id":"33","type":"domicile_seeds","attributes":{}}}'
        mocked_response = MagicMock(ok=True, text=response_text)
        requests.post = MagicMock(return_value=mocked_response)

        self.assertEqual(seed.id, None, 'Should have id None')
        seed_id = self.bitex_api.create_domicile_seed(seed)

        requests.post.assert_called_with(
            'https://bitextest.com/domicile_seeds',
            headers=self.mocked_headers,
            json=serialized_seed
        )
        self.assertEqual(seed_id, '33', 'Should have id 33')

    def test_create_attachments(self):
        mocked_file = MagicMock()
        seed = AttachmentSeed(mocked_file, 22, [])
        serialized_seed = MagicMock()
        seed_serializer = MagicMock()
        seed_serializer.serialize = MagicMock(return_value=serialized_seed)
        self.serializer_selector['attachments'] = seed_serializer
        response_text = '{"data":{"id":"33","type":"attachments","attributes":{}}}'
        mocked_response = MagicMock(ok=True, text=response_text)
        requests.post = MagicMock(return_value=mocked_response)

        self.assertEqual(seed.id, None, 'Should have id None')
        seed_id = self.bitex_api.create_attachments(seed)

        requests.post.assert_called_with(
            'https://bitextest.com/attachments',
            headers=self.mocked_headers,
            json=serialized_seed
        )
        self.assertEqual(seed_id, '33', 'Should have id 33')


if __name__ == '__main__':
    unittest.main()
