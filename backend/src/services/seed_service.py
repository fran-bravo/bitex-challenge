class SeedService:

    def __init__(self, api, seed_factory):
        self.api = api
        self.seed_factory = seed_factory

    def create_natural_docket(self, user, issue_id):
        seed = self.seed_factory.create_natural_docket(user, issue_id)
        seed.id = self.api.create_natural_docket_seed(seed)
        return seed

    def create_identification(self, seed_data, issue_id):
        seed = self.seed_factory.create_identification(seed_data, issue_id)
        seed.id = self.api.create_identification_seed(seed)
        return seed

    def create_domicile(self, seed_data, issue_id):
        seed = self.seed_factory.create_domicile(seed_data, issue_id)
        seed.id = self.api.create_domicile_seed(seed)
        return seed

    def create_attachments(self, file, included_seeds, issue_id):
        seed = self.seed_factory.create_attachments(file, included_seeds, issue_id)
        seed.id = self.api.create_attachments(seed)
        return seed
