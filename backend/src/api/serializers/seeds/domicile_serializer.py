class DomicileSerializer:

    def serialize(self, seed):
        return {
            'data': {
                'type': seed.type(),
                'attributes': {
                    'city': seed.city,
                    'country': seed.country,
                    'postal_code': seed.postal_code,
                    'street_address': seed.street_address,
                    'street_number': seed.street_number,
                    'floor': seed.floor
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
