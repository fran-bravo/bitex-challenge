from src.validators.validator import Validator


class DomicileValidator(Validator):
    REQUIRED_ARGUMENTS = ['streetAddress', 'streetNumber', 'city', 'postalCode', 'country']

    def validate(self, domicile_data):
        self._validate_arguments(domicile_data)
