class IdentificationSerializer:

    def serialize(self, seed):
        return {
            'data': {
                'type': seed.type(),
                'attributes': {
                    'identification_kind_code': seed.kind_code,
                    'issuer': seed.issuer,
                    'number': seed.number
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
