import os
from configparser import ConfigParser
from src.api.bitex import Bitex

from src.api.factories.user_factory import UserFactory
from src.api.factories.issue_factory import IssueFactory
from src.api.factories.seed_factory import SeedFactory

from src.api.serializers.serializer_selector import SerializerSelector
from src.api.serializers.user_serializer import UserSerializer
from src.api.serializers.issue_serializer import IssueSerializer
from src.api.serializers.seeds.natural_docket_serializer import NaturalDocketSerializer
from src.api.serializers.seeds.identification_serializer import IdentificationSerializer
from src.api.serializers.seeds.domicile_serializer import DomicileSerializer
from src.api.serializers.seeds.attachment_serializer import AttachmentSerializer

from src.services.user_service import UserService
from src.services.issue_service import IssueService
from src.services.seed_service import SeedService
from src.services.registration_service import RegistrationService
from src.services.identification_service import IdentificationService
from src.services.domicile_service import DomicileService

from src.parsers.registration_parser import RegistrationParser
from src.parsers.identification_parser import IdentificationParser
from src.validators.registration_validator import RegistrationValidator
from src.validators.identification_validator import IdentificationValidator

registration_validator = RegistrationValidator()
identification_validator = IdentificationValidator()
registration_parser = RegistrationParser()
identification_parser = IdentificationParser()

serializer_selector = SerializerSelector(
    users=UserSerializer(),
    issues=IssueSerializer(),
    natural_docket_seeds=NaturalDocketSerializer(),
    identification_seeds=IdentificationSerializer(),
    domicile_seeds=DomicileSerializer(),
    attachments=AttachmentSerializer()
)

config_parser = ConfigParser()
config_parser.read('app_config.txt')
bitex_config = {
    'base_url': config_parser.get('bitex', 'base_url'),
    'users_endpoint': config_parser.get('bitex', 'users_endpoint'),
    'issues_endpoint': config_parser.get('bitex', 'issues_endpoint'),
    'natural_docket_seed_endpoint': config_parser.get('bitex', 'natural_docket_seed_endpoint'),
    'identification_seed_endpoint': config_parser.get('bitex', 'identification_seed_endpoint'),
    'domicile_seed_endpoint': config_parser.get('bitex', 'domicile_seed_endpoint'),
    'attachments_endpoint': config_parser.get('bitex', 'attachments_endpoint'),
    'version': config_parser.get('bitex', 'version')
}
BITEX_API_KEY = os.environ['BITEX_API_KEY']
bitex = Bitex(BITEX_API_KEY, bitex_config, serializer_selector)


user_factory = UserFactory()
issue_factory = IssueFactory()
seed_factory = SeedFactory()
user_service = UserService(bitex, user_factory)
issue_service = IssueService(bitex, issue_factory)
seed_service = SeedService(bitex, seed_factory)
registration_service = RegistrationService(user_service, issue_service, seed_service)
identification_service = IdentificationService(seed_service)
domicile_service = DomicileService(seed_service)
