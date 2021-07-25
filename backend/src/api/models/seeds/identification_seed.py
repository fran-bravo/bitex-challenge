from src.api.models.seeds.seed import Seed


class IdentificationSeed(Seed):

    def __init__(self, kind_code, issuer, number, issue_id):
        self.id = None
        self.kind_code = kind_code
        self.issuer = issuer
        self.number = number
        self.issue_id = issue_id

    def attributes(self):
        return {
            'identification_kind_code': self.kind_code,
            'issuer': self.issuer,
            'number': self.number
        }

    def type(self):
        return 'identification_seeds'

    def __str__(self):
        return f"IdentificationSeed<id={self.id}, kind_code={self.kind_code}, issuer={self.issuer}, " \
               f"number={self.number}, issue_id={self.issue_id}>"

    def __repr__(self):
        return f"IdentificationSeed<id={self.id}, kind_code={self.kind_code}, issuer={self.issuer}, " \
               f"number={self.number}, issue_id={self.issue_id}>"
