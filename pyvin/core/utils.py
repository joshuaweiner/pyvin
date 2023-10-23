""" Utilities
"""

from string import capwords
import re


def camel_to_snake(word):
    # convert CamelCase to snake_case
    snake_case = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', word)
    snake_case = re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake_case)
    return snake_case.lower()


def remove_empty_response_values(vehicle_details):
    # remove empty or None values from a dictionary
    return {key: value for key, value in vehicle_details.items() if value is not None and value != ""}


def clean_response_values(vehicle_details):
    # clean and convert keys to snake_case
    cleaned_details = remove_empty_response_values(vehicle_details)
    return {camel_to_snake(key): value for key, value in cleaned_details.items()}


def validate_vin(vin):
    if len(vin) != 17:
        return False

    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]

    values = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
        'F': 6, 'G': 7, 'H': 8, 'J': 1, 'K': 2,
        'L': 3, 'M': 4, 'N': 5, 'P': 7, 'R': 9,
        'S': 2, 'T': 3, 'U': 4, 'V': 5, 'W': 6,
        'X': 7, 'Y': 8, 'Z': 9
    }

    checksum = 0
    for i, char in enumerate(vin):
        if char.isnumeric():
            value = int(char)
        elif char in values:
            value = values[char]
        else:
            return False

        checksum += value * weights[i]

    if checksum % 11 == 10:
        check_digit = 'X'
    else:
        check_digit = str(checksum % 11)

    return vin[8] == check_digit


def display_vehicle_details(vehicle_details):

    TITLE = 'Vehicle Information Report'

    print('-' * 78)
    print(TITLE)
    print('-' * 78)

    for key, value in vehicle_details.items():
        if value is not None and value != "":
            key = capwords(key.replace('_', ' '))
            print(f"{key}: {value}")

    print('-' * 78)
