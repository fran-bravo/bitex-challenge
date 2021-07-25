import unittest
from unittest.mock import MagicMock
from src.services.issue_service import IssueService
from src.api.factories.issue_factory import IssueFactory
from src.api.models.issue import Issue


class TestIssueService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = MagicMock()
        cls.issue_factory = IssueFactory()
        cls.issue_service = IssueService(cls.api, cls.issue_factory)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_create(self):
        user_id = 1
        self.api.create_issue = MagicMock(return_value=2)

        issue = self.issue_service.create(user_id)

        self.assertEqual(issue.user_id, 1, 'Should have id 1')
        self.assertEqual(issue.id, 2, 'Should have id 2')
        self.assertIsInstance(issue, Issue)


if __name__ == '__main__':
    unittest.main()
