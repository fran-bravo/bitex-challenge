from datetime import datetime
from src.validators.validator import Validator
from src.exceptions.wrong_date_format_exception import WrongDateFormatException


class RegistrationValidator(Validator):
    REQUIRED_ARGUMENTS = ['firstName', 'lastName', 'birthDate', 'country']

    def validate(self, registration_data):
        self._validate_arguments(registration_data)
        self._validate_date(registration_data['birthDate'])

    def validate_user_id(self, user_id_data):
        pass

    @staticmethod
    def _validate_date(date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise WrongDateFormatException('Incorrect data format, should be YYYY-MM-DD')
