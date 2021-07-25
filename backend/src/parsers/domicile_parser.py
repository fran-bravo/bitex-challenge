import json


class DomicileParser:

    def parse(self, request):
        return {
            'domicile': json.loads(request.form['domicile']),
            'files': [request.files['domicileProof']],
            'issue': json.loads(request.form['issue'])
        }
