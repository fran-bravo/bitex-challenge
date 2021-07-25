import json


class DomicileParser:

    def parse_domicile(self, request):
        domicile_data = request.form.to_dict()
        return json.loads(domicile_data['domicile'])

    def parse_domicile_proof(self, request):
        domicile_files = request.files.to_dict()
        return {
            'proof': self._parse_file(domicile_files['proof'])
        }

    @staticmethod
    def _parse_file(file):
        return 'files', (file.filename, file.stream, file.mimetype)
