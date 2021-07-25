class NaturalDocketSerializer:

    def serialize(self, seed):
        return {
            'data': {
                'type': seed.type(),
                'attributes': {
                    'first_name': seed.first_name,
                    'last_name': seed.last_name,
                    'nationality': seed.nationality,
                    'birth_date': seed.birth_date
                },
                'relationships': {
                    'issue': {
                        'data': {
                            'type': 'issues',
                            'id': seed.issue_id
                        }
                    }
                }
            }
        }
