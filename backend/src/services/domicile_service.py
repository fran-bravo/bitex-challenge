class DomicileService:

    def __init__(self, seed_service):
        self.seed_service = seed_service

    def create(self, domicile_data, file, issue):
        domicile_seed = self.seed_service.create_domicile(domicile_data, issue.id)
        attachments_seed = self.seed_service.create_attachments(file, [domicile_seed], issue.id)
        return domicile_seed, attachments_seed
