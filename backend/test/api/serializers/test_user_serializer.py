import unittest
from unittest.mock import MagicMock
from src.api.serializers.user_serializer import UserSerializer


class TestUserSerializer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_serializer = UserSerializer()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_serialization(self):
        mocked_user = MagicMock()
        expected_serialization = {
            'data': {
                'type': 'users',
                'attributes': {}
            }
        }
        serialized_user = self.user_serializer.serialize(mocked_user)
        self.assertEqual(serialized_user, expected_serialization, 'Should be expected serialization')


if __name__ == '__main__':
    unittest.main()
