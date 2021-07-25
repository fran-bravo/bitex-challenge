from datetime import datetime
from src.validators.validator import Validator
from src.exceptions.wrong_date_format_exception import WrongDateFormatException


class IdentificationValidator(Validator):
    REQUIRED_ARGUMENTS = ['data', 'files', 'issue']

    def validate(self, identification_data):
        self._validate_arguments(identification_data)
