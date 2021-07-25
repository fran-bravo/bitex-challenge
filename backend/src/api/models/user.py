class User:

    def __init__(self, first_name, last_name, date_of_birth, country):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.country = country

    def type(self):
        return 'users'

    def __str__(self):
        return f"User<id={self.id}, first_name={self.first_name}, last_name={self.last_name}, " \
               f"date_of_birth={self.date_of_birth}, country={self.country}>"

    def __repr__(self):
        return f"User<id={self.id}, first_name={self.first_name}, last_name={self.last_name}, " \
               f"date_of_birth={self.date_of_birth}, country={self.country}>"
