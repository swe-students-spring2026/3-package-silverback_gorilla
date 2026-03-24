from enum import Enum

class InvalidUnitError(Exception):
    pass

class DataUnit(Enum):
    B  = 1 
    KB = 1024
    MB = 1024 ** 2
    GB = 1024 ** 3
    TB = 1024 ** 4

NDIGITS = 4

def convert_data(x: float, unit_from: DataUnit, unit_to: DataUnit) -> float:
    if unit_from == unit_to:
        return round(x, NDIGITS)

    try:
        bytes_value = x * unit_from.value
    
        result = bytes_value / unit_to.value
        
        return round(result, NDIGITS)

    except Exception:
        raise InvalidUnitError("Invalid data unit provided")