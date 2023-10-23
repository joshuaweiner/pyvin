"""
High-Level API
"""

from pyvin.core.nhtsa import NHTSA
from pyvin.core.vin import Vin, InvalidVINError
from pyvin.core.utils import display_vehicle_details, clean_response_values


class Vehicle:

    vin = Vin()

    def __init__(self, vin):
        try:
            self.vin = vin
            self.core = NHTSA(self.vin)
            self.core.get_vehicle_details()
            self.details = clean_response_values(self.core.response)
            self.set_vehicle_details()

        except InvalidVINError as e:
            raise e

    def __str__(self):
        return f'Vehicle Info: {self.vin}'

    def set_vehicle_details(self):
        for key, value in self.details.items():
            setattr(self, key.lower(), value)

    def display(self):
        display_vehicle_details(self.details)
        return self


class Vehicles:

    def __init__(self, vins):
        self.vins = [vin.strip() for vin in vins.split(',')]
        self.vehicles = [Vehicle(vin) for vin in self.vins]
        return

    def __iter__(self):
        return iter(self.vehicles)
