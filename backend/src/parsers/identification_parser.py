import json


class IdentificationParser:

    def parse(self, request):
        return {
            'data': {
                'kind_code': 'national_id',
                'issuer': 'AR',
                'number': request.form['dni']
            },
            'files': [request.files['dniFront'], request.files['dniBack']],
            'issue': json.loads(request.form['issue'])
        }
