from abc import ABC
from src.exceptions.missing_argument_exception import MissingArgumentException


class Validator(ABC):

    def _validate_arguments(self, data):
        for argument in self.REQUIRED_ARGUMENTS:
            if argument not in data:
                raise MissingArgumentException(f"Argument {argument} is missing in request")
