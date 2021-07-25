import unittest
from unittest.mock import MagicMock
from src.api.factories.user_factory import UserFactory
from src.api.factories.domicile_factory import DomicileFactory


class TestUserFactory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_factory = UserFactory()
        cls.mocked_domicile = MagicMock()
        cls.mocked_file = MagicMock()
        DomicileFactory.create_from_dict = MagicMock(return_value=cls.mocked_domicile)
        cls.mocked_user = {
            'firstName': 'Test',
            'lastName': 'User',
            'birthDate': '2003-07-02',
            'country': 'AR',
        }

    @classmethod
    def tearDownClass(cls):
        pass

    def test_creation(self):
        user = self.user_factory.create(self.mocked_user)
        self.assertEqual(user.first_name, 'Test', 'Should be Test')
        self.assertEqual(user.last_name, 'User', 'Should be User')
        self.assertEqual(user.date_of_birth, '2003-07-02', 'Should be 2003-07-02')
        self.assertEqual(user.country, 'AR', 'Should be AR')


if __name__ == '__main__':
    unittest.main()
