""" Vin
"""
from pyvin.core.utils import validate_vin


class InvalidVINError(ValueError):
    pass


class Vin:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if not validate_vin(value):
            raise InvalidVINError(f'InvalidVINError, InvalidVin: {value}')
        self.value = value


