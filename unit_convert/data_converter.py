from enum import Enum

class InvalidUnitError(Exception):
    pass

class DataUnit(Enum):
    # Bytes (binary, base = bytes)
    B  = 1
    KB = 1024
    MB = 1024 ** 2
    GB = 1024 ** 3
    TB = 1024 ** 4
    PB = 1024 ** 5
    EB = 1024 ** 6

    # Bits (1 byte = 8 bits)
    b  = 1 / 8
    Kb = 1024 / 8
    Mb = (1024 ** 2) / 8
    Gb = (1024 ** 3) / 8
    Tb = (1024 ** 4) / 8

NDIGITS = 4

def convert_data(x: float, unit_from: DataUnit, unit_to: DataUnit) -> float:
    if unit_from == unit_to:
        return round(x, NDIGITS)

    try:
        # convert to base unit (bytes)
        bytes_value = x * unit_from.value

        # convert to target unit
        result = bytes_value / unit_to.value

        return round(result, NDIGITS)

    except Exception:
        raise InvalidUnitError("Invalid data unit provided")