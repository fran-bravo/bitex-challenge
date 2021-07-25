import unittest
from unittest.mock import MagicMock
from src.services.registration_service import RegistrationService
from src.services.user_service import UserService
from src.services.issue_service import IssueService
from src.services.seed_service import SeedService
from src.api.factories.user_factory import UserFactory
from src.api.factories.issue_factory import IssueFactory
from src.api.factories.seed_factory import SeedFactory


class TestRegistrationService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = MagicMock()
        user_factory = UserFactory()
        issue_factory = IssueFactory()
        seed_factory = SeedFactory()
        user_service = UserService(cls.api, user_factory)
        issue_service = IssueService(cls.api, issue_factory)
        seed_service = SeedService(cls.api, seed_factory)
        cls.registration_service = RegistrationService(user_service, issue_service, seed_service)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_create(self):
        user_data = {
            'firstName': 'Test',
            'lastName': 'User',
            'birthDate': '2003-07-02',
            'country': 'AR',
            'dni': '11111111',
        }

        self.api.create_user = MagicMock(return_value=1)
        self.api.create_issue = MagicMock(return_value=2)
        self.api.create_natural_docket_seed = MagicMock(return_value=3)

        user, issue, seed = self.registration_service.create(user_data)

        self.assertEqual(user.id, 1, 'Should have id 1')
        self.assertEqual(user.first_name, 'Test', 'Should have id 1')
        self.assertEqual(issue.id, 2, 'Should have id 2')
        self.assertEqual(issue.user_id, 1, 'Should have id 1')
        self.assertEqual(seed.id, 3, 'Should have id 3')
        self.assertEqual(seed.issue_id, 2, 'Should have id 2')
        self.assertEqual(seed.first_name, 'Test', 'Should have id Test')


if __name__ == '__main__':
    unittest.main()
