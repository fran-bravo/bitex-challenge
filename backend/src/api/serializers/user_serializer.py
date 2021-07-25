class UserSerializer:

    def serialize(self, user):
        return {
            'data': {
                'type': 'users',
                'attributes': {}
            }
        }
