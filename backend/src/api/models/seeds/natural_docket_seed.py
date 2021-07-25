from src.api.models.seeds.seed import Seed


class NaturalDocketSeed(Seed):

    def __init__(self, first_name, last_name, nationality, birth_date, issue_id):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.birth_date = birth_date
        self.issue_id = issue_id

    def attributes(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'nationality': self.nationality,
            'birth_date': self.birth_date
        }

    def type(self):
        return 'natural_docket_seeds'

    def __str__(self):
        return f"NaturalDocketSeed<id={self.id}, first_name={self.first_name}, last_name={self.last_name}, " \
               f"nationality={self.nationality}, birth_date={self.birth_date}, issue_id={self.issue_id}>"

    def __repr__(self):
        return f"NaturalDocketSeed<id={self.id}, first_name={self.first_name}, last_name={self.last_name}, " \
               f"nationality={self.nationality}, birth_date={self.birth_date}, issue_id={self.issue_id}>"
