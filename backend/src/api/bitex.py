import json
import requests
from src.api.exceptions.bitex_api_exception import BitexAPIException


class Bitex:

    def __init__(self, api_key, config, serializer_selector):
        self.api_key = api_key
        self.config = config
        self.serializer_selector = serializer_selector

    def list_users(self):
        params = {
            'page': {
                'page': 0,
                'per_page': 10
            }
        }
        response = requests.get(self._users_url(), headers=self._headers(), json=params)
        return self._validate_response(response)

    def create_user(self, user):
        return self._post(self._users_url(), user.type(), user)

    def create_issue(self, issue):
        return self._post(self._issues_url(), issue.type(), issue)

    def create_natural_docket_seed(self, seed):
        return self._post(self._natural_docket_seed_url(), seed.type(), seed)

    def create_identification_seed(self, seed):
        return self._post(self._identification_seed_url(), seed.type(), seed)

    def create_domicile_seed(self, seed):
        return self._post(self._domicile_seed_url(), seed.type(), seed)

    def create_attachments(self, seed):
        return self._post(self._attachments_url(), seed.type(), seed)

    def _post(self, url, serializer_type, entity):
        seed_serializer = self.serializer_selector[serializer_type]
        serialized_seed = seed_serializer.serialize(entity)
        response = requests.post(url, headers=self._headers(), json=serialized_seed)
        return self._parse(response)

    @staticmethod
    def _validate_response(response):
        if response.ok:
            return response
        else:
            raise BitexAPIException('There was an issue when requesting from Bitex')

    def _parse(self, response):
        self._validate_response(response)
        parsed_response = json.loads(response.text)
        return parsed_response['data']['id']

    def _headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': self.api_key,
            'Version': self.config['version']
        }

    def _users_url(self):
        return self._url('users_endpoint')

    def _issues_url(self):
        return self._url('issues_endpoint')

    def _natural_docket_seed_url(self):
        return self._url('natural_docket_seed_endpoint')

    def _identification_seed_url(self):
        return self._url('identification_seed_endpoint')

    def _domicile_seed_url(self):
        return self._url('domicile_seed_endpoint')

    def _attachments_url(self):
        return self._url('attachments_endpoint')

    def _url(self, endpoint):
        return f"{self.config['base_url']}/{self.config[endpoint]}"
