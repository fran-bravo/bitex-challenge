import unittest
from src.api.exceptions.unknown_serializer_exception import UnknownSerializerException
from src.api.serializers.issue_serializer import IssueSerializer
from src.api.serializers.user_serializer import UserSerializer
from src.api.serializers.seeds.natural_docket_serializer import NaturalDocketSerializer
from src.api.serializers.seeds.domicile_serializer import DomicileSerializer
from src.api.serializers.seeds.identification_serializer import IdentificationSerializer
from src.api.serializers.seeds.attachment_serializer import AttachmentSerializer
from src.api.serializers.serializer_selector import SerializerSelector


class TestSerializerSelector(unittest.TestCase):

    def test_serialization_ok(self):
        issue_serializer = IssueSerializer()
        user_serializer = UserSerializer()
        natural_docket_serializer = NaturalDocketSerializer()
        domicile_serializer = DomicileSerializer()
        identification_serializer = IdentificationSerializer()
        attachment_serializer = AttachmentSerializer()
        serializer_selector = SerializerSelector(
            issues=issue_serializer,
            users=user_serializer,
            natural_docket_seed=natural_docket_serializer,
            domicile_seed=domicile_serializer,
            identification_seed=identification_serializer,
            attachment_seed=attachment_serializer
        )
        self.assertEqual(serializer_selector['issues'], issue_serializer, 'Should be expected issue serializer')
        self.assertEqual(serializer_selector['users'], user_serializer, 'Should be expected user serializer')
        self.assertEqual(
            serializer_selector['natural_docket_seed'],
            natural_docket_serializer,
            'Should be expected natural docket seedd serializer'
        )
        self.assertEqual(
            serializer_selector['domicile_seed'],
            domicile_serializer,
            'Should be expected domicile seed serializer'
        )
        self.assertEqual(
            serializer_selector['identification_seed'],
            identification_serializer,
            'Should be expected identification seed serializer'
        )
        self.assertEqual(
            serializer_selector['attachment_seed'],
            attachment_serializer,
            'Should be expected attachment seed serializer'
        )

    def test_serialization_error(self):
        serializer_selector = SerializerSelector()
        self.assertRaises(UnknownSerializerException, serializer_selector.__getitem__, 'serializer')


if __name__ == '__main__':
    unittest.main()
