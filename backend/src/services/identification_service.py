class IdentificationService:

    def __init__(self, seed_service):
        self.seed_service = seed_service

    def create(self, identification_data, files, issue_id):
        identification_seed = self.seed_service.create_identification(identification_data, issue_id)
        attachments_seeds = [
            self.seed_service.create_attachments(file, [identification_seed], issue_id) for file in files
        ]
        return identification_seed, attachments_seeds
