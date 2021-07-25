import base64
import unittest
from unittest.mock import MagicMock
from src.api.exceptions.no_included_seed_exception import NoIncludedSeedException
from src.api.models.seeds.attachment_seed import AttachmentSeed
from src.api.models.seeds.identification_seed import IdentificationSeed
from src.api.models.seeds.domicile_seed import DomicileSeed
from src.api.models.seeds.natural_docket_seed import NaturalDocketSeed
from src.api.serializers.seeds.attachment_serializer import AttachmentSerializer
from src.api.serializers.seeds.domicile_serializer import DomicileSerializer
from src.api.serializers.seeds.identification_serializer import IdentificationSerializer
from src.api.serializers.seeds.natural_docket_serializer import NaturalDocketSerializer


class TestSeedSerializer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.attachment_serializer = AttachmentSerializer()
        cls.domicile_serializer = DomicileSerializer()
        cls.identification_serializer = IdentificationSerializer()
        cls.natural_docket_serializer = NaturalDocketSerializer()
        cls.issue_id = 1

    @classmethod
    def tearDownClass(cls):
        pass

    def test_attachment_serialization_ok(self):
        included_seed = IdentificationSeed('national_id', 'AR', '123456789', self.issue_id)
        mocked_stream = MagicMock()
        mocked_file = MagicMock(
            stream=mocked_stream,
            filename='attachment.png',
            mimetype='image/png',
            content_length=7
        )
        base64.b64encode = MagicMock(return_value='encoded')
        attachment_seed = AttachmentSeed(mocked_file, [included_seed], self.issue_id)
        expected_serialization = {
            'data': {
                'type': 'attachments',
                'attributes': {
                    'document': 'data:image/png;base64,encoded',
                    'document_file_name': mocked_file.filename,
                    'document_content_type': mocked_file.mimetype,
                    'document_size': mocked_file.content_length
                },
                'relationships': {
                    'attached_to_seed': {
                        'data': {
                            'type': included_seed.type(),
                            'id': included_seed.id
                        }
                    }
                }
            },
            'included': [
                {
                    'type': included_seed.type(),
                    'attributes': included_seed.attributes(),
                    'relationships': {
                        'attachments': {
                            'data': []
                        }
                    },
                    'id': included_seed.id
                }
            ]
        }
        serialized_seed = self.attachment_serializer.serialize(attachment_seed)
        self.assertEqual(serialized_seed, expected_serialization, 'Should be expected serialization')

    def test_attachment_serialization_error(self):
        mocked_stream = MagicMock()
        mocked_file = MagicMock(
            stream=mocked_stream,
            filename='attachment.png',
            mimetype='image/png',
            content_length=10
        )
        base64.b64encode = MagicMock(return_value='encoded')
        attachment_seed = AttachmentSeed(mocked_file, [], self.issue_id)
        self.assertRaises(NoIncludedSeedException, self.attachment_serializer.serialize, attachment_seed)

    def test_identification_serialization(self):
        identification_seed = IdentificationSeed('national_id', 'AR', '123456789', self.issue_id)
        expected_serialization = {
            'data': {
                'type': 'identification_seeds',
                'attributes': {
                    'identification_kind_code': 'national_id',
                    'issuer': 'AR',
                    'number': '123456789'
                },
                'relationships': {
                    'issue': {
                        'data': {
                            'type': 'issues',
                            'id': self.issue_id
                        }
                    }
                }
            }
        }
        serialized_seed = self.identification_serializer.serialize(identification_seed)
        self.assertEqual(serialized_seed, expected_serialization, 'Should be expected serialization')

    def test_domicile_serialization(self):
        domicile_seed = DomicileSeed('ciudad', 'AR', '1111', 'calle', '1234', self.issue_id, floor='4')
        expected_serialization = {
            'data': {
                'type': 'domicile_seeds',
                'attributes': {
                    'city': 'ciudad',
                    'country': 'AR',
                    'postal_code': '1111',
                    'street_address': 'calle',
                    'street_number': '1234',
                    'floor': '4'
                },
                'relationships': {
                    'issue': {
                        'data': {
                            'type': 'issues',
                            'id': self.issue_id
                        }
                    }
                }
            }
        }
        serialized_seed = self.domicile_serializer.serialize(domicile_seed)
        self.assertEqual(serialized_seed, expected_serialization, 'Should be expected serialization')

    def test_natural_docket_serialization(self):
        natural_doket_seed = NaturalDocketSeed('test', 'user', 'AR', '2020-07-03', self.issue_id)
        expected_serialization = {
            'data': {
                'type': 'natural_docket_seeds',
                'attributes': {
                    'first_name': 'test',
                    'last_name': 'user',
                    'nationality': 'AR',
                    'birth_date': '2020-07-03'
                },
                'relationships': {
                    'issue': {
                        'data': {
                            'type': 'issues',
                            'id': self.issue_id
                        }
                    }
                }
            }
        }
        serialized_seed = self.natural_docket_serializer.serialize(natural_doket_seed)
        self.assertEqual(serialized_seed, expected_serialization, 'Should be expected serialization')


if __name__ == '__main__':
    unittest.main()
