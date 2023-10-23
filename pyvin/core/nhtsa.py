"""
Core Functionality
"""

import requests

from pyvin.core.url import UrlMixin
from pyvin.core.utils import validate_vin, camel_to_snake


class InvalidVINError(ValueError):
    pass


class Vin:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if not validate_vin(value):
            raise InvalidVINError(f'InvalidVINError, InvalidVin: {value}')
        self.value = value


class NHTSA(UrlMixin):

    PACKET_FORMAT_JSON = 'json'

    def __init__(self, vin):
        self.vin = vin
        self.packet_format = NHTSA.PACKET_FORMAT_JSON

        super().__init__()

    def get_vehicle_details(self):
        try:
            response = requests.get(url=self.request_url(self.vin, self.packet_format))

        except requests.exceptions.Timeout:
            raise Exception("NHTSA: Connection Timed Out.")

        except requests.exceptions.ConnectionError:
            raise Exception("NHTSA: Connection Failed.")

        try:
            response = response.json()
            response = response.get('Results', [])[0]

        except ValueError:
            raise Exception("NHTSA: Could Not Parse Result.")

        self.response = response

        return 0 
