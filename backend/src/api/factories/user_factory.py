from src.api.models.user import User


class UserFactory:

    @staticmethod
    def create(user_data):
        return User(
            user_data['firstName'],
            user_data['lastName'],
            user_data['birthDate'],
            user_data['country']
        )
