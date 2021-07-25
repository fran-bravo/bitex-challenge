class UserService:

    def __init__(self, api, users_factory):
        self.api = api
        self.users_factory = users_factory

    def create(self, user_data):
        user = self.users_factory.create(user_data)
        user.id = self.api.create_user(user)
        return user
