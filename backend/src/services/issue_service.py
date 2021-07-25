class IssueService:

    def __init__(self, api, issues_factory):
        self.api = api
        self.issues_factory = issues_factory

    def create(self, user_id):
        issue = self.issues_factory.create(user_id)
        issue.id = self.api.create_issue(issue)
        return issue
