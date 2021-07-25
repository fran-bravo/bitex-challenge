import unittest
from unittest.mock import MagicMock
from src.api.serializers.issue_serializer import IssueSerializer


class TestIssueSerializer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.issue_serializer = IssueSerializer()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_serialization(self):
        mocked_issue = MagicMock(user_id=1, reason_code='new_client')
        expected_serialization = {
            'data': {
                'type': 'issues',
                'attributes': {
                    'reason_code': 'new_client'
                },
                'relationships': {
                    'issue': {
                        'data': {
                            'type': 'User',
                            'id': 1
                        }
                    }
                }
            }
        }
        serialized_issue = self.issue_serializer.serialize(mocked_issue)
        self.assertEqual(serialized_issue, expected_serialization, 'Should be expected serialization')


if __name__ == '__main__':
    unittest.main()
