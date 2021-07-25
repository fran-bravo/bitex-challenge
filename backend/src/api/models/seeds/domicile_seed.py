from src.api.models.seeds.seed import Seed


class DomicileSeed(Seed):

    def __init__(self, city, country, postal_code, street_address, street_number, issue_id, floor=''):
        self.id = None
        self.city = city
        self.country = country
        self.postal_code = postal_code
        self.street_address = street_address
        self.street_number = street_number
        self.floor = floor
        self.issue_id = issue_id

    def attributes(self):
        return {
            'city': self.city,
            'country': self.country,
            'postal_code': self.postal_code,
            'street_address': self.street_address,
            'street_number': self.street_number,
            'floor': self.floor
        }

    def type(self):
        return 'domicile_seeds'

    def __str__(self):
        return f"DomicileSeed<id={self.id}, city={self.city}, country={self.country}, " \
               f"postal_code={self.postal_code}, street_address={self.street_address}, " \
               f"street_number={self.street_number}, floor={self.floor}, issue_id={self.issue_id}>"

    def __repr__(self):
        return f"DomicileSeed<id={self.id}, city={self.city}, country={self.country}, " \
               f"postal_code={self.postal_code}, street_address={self.street_address}, " \
               f"street_number={self.street_number}, floor={self.floor}, issue_id={self.issue_id}>"
