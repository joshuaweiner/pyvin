"""
NHTSA API URLMixin Class
"""


class UrlMixin:

    def __init__(self):
        self._base_url = 'https://vpic.nhtsa.dot.gov/api'
        self._decode_vin = '/vehicles/decodevinvalues'

    @property
    def base_url(self):
        return self._base_url

    @property
    def decode_vin_url(self):
        return self._base_url + self._decode_vin

    def request_url(self, vin, packet_format):
        return self.decode_vin_url + '/' + vin + '?format=' + packet_format
