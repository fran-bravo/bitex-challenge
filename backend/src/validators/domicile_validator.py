from src.validators.validator import Validator


class DomicileValidator(Validator):
    REQUIRED_ARGUMENTS = ['domicile', 'files', 'issue']

    def validate(self, domicile_data):
        self._validate_arguments(domicile_data)
