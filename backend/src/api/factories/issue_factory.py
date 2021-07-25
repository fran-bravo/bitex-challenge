from src.api.models.issue import Issue


class IssueFactory:

    @staticmethod
    def create(user_id, reason_code='new_client'):
        return Issue(
            user_id,
            reason_code=reason_code
        )
