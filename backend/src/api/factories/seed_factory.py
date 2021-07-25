from src.api.models.seeds.natural_docket_seed import NaturalDocketSeed
from src.api.models.seeds.identification_seed import IdentificationSeed
from src.api.models.seeds.domicile_seed import DomicileSeed
from src.api.models.seeds.attachment_seed import AttachmentSeed


class SeedFactory:

    @staticmethod
    def create_natural_docket(user, issue_id):
        return NaturalDocketSeed(
            user.first_name,
            user.last_name,
            user.country,
            user.date_of_birth,
            issue_id
        )

    @staticmethod
    def create_identification(seed_data, issue_id):
        return IdentificationSeed(
            seed_data['kind_code'],
            seed_data['issuer'],
            seed_data['number'],
            issue_id
        )

    @staticmethod
    def create_domicile(seed_data, issue_id):
        return DomicileSeed(
            seed_data['city'],
            seed_data['country'],
            seed_data['postal_code'],
            seed_data['street_address'],
            seed_data['street_number'],
            issue_id,
            floor=seed_data['floor']
        )

    @staticmethod
    def create_attachments(file, included_seeds, issue_id):
        return AttachmentSeed(
            file,
            included_seeds,
            issue_id
        )
