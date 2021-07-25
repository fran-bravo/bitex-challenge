import unittest
from src.api.factories.issue_factory import IssueFactory


class TestIssueFactory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.issue_factory = IssueFactory()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_creation(self):
        user_id = 1
        issue = self.issue_factory.create(user_id)
        self.assertEqual(issue.user_id, user_id, 'Should be user_id')
        self.assertEqual(issue.reason_code, 'new_client', 'Should be new_client')


if __name__ == '__main__':
    unittest.main()
