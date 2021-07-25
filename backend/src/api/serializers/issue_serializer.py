class IssueSerializer:

    def serialize(self, issue):
        return {
            'data': {
                'type': 'issues',
                'attributes': {
                    'reason_code': issue.reason_code
                },
                'relationships': {
                    'issue': {
                        'data': {
                            'type': 'User',
                            'id': issue.user_id
                        }
                    }
                }
            }
        }
