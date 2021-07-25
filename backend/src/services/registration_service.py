class RegistrationService:

    def __init__(self, user_service, issue_service, seed_service):
        self.user_service = user_service
        self.issue_service = issue_service
        self.seed_service = seed_service

    def create(self, user_data):
        user = self.user_service.create(user_data)
        issue = self.issue_service.create(user.id)
        seed = self.seed_service.create_natural_docket(user, issue.id)
        return user, issue, seed
