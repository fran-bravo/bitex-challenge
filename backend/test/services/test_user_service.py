import unittest
from unittest.mock import MagicMock
from src.services.user_service import UserService
from src.api.factories.user_factory import UserFactory
from src.api.models.user import User


class TestUserService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = MagicMock()
        cls.user_factory = UserFactory()
        cls.user_service = UserService(cls.api, cls.user_factory)

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

        user = self.user_service.create(user_data)

        self.assertEqual(user.id, 1, 'Should have id 1')
        self.assertIsInstance(user, User)


if __name__ == '__main__':
    unittest.main()
