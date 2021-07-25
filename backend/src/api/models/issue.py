class Issue:

    def __init__(self, user_id, reason_code='new_client'):
        self.id = None
        self.user_id = user_id
        self.reason_code = reason_code

    def type(self):
        return 'issues'

    def __str__(self):
        return f"Issue<id={self.id}, user_id={self.user_id}, reason_code={self.reason_code}>"

    def __repr__(self):
        return f"Issue<id={self.id}, user_id={self.user_id}, reason_code={self.reason_code}>"
