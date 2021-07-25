class Domicile:

    def __init__(self, street_address, street_number, city, floor, postal_code, country):
        self.street_address = street_address
        self.street_number = street_number
        self.city = city
        self.floor = floor
        self.postal_code = postal_code
        self.country = country

    def to_dict(self):
        return {
            'street_address': self.street_address,
            'street_number': self.street_number,
            'city': self.city,
            'floor': self.floor,
            'postal_code': self.postal_code,
            'country': self.country,
        }

    def __str__(self):
        return f"Domicile<street_address={self.street_address}, street_number={self.street_number}, " \
               f"city={self.city}, floor={self.floor}, postal_code={self.postal_code}, country={self.country}>"

    def __repr__(self):
        return f"Domicile<street_address={self.street_address}, street_number={self.street_number}, " \
               f"city={self.city}, floor={self.floor}, postal_code={self.postal_code}, country={self.country}>"
