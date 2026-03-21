from enum import Enum

class InvalidUnitError(Exception):
    pass

class UnitMass(Enum):
    G = "gram"
    P = "pound"
    K = "kilogram"

NDIGITS = 8

def convert_mass(x: float, unit_from: UnitMass, unit_to: UnitMass) -> float:

    if unit_from == unit_to: return x

    #Convert to grams first
    match unit_from.name:
        case "G":
            pass
        case "P":
            x = pounds_to_grams(x)
        case "K":
            x = kilograms_to_grams(x)
        case _:
            raise InvalidUnitError("`unit_from` is not an accepted mass unit")

    match unit_to.name:
        case "G":
            return x
        case "P":
            return grams_to_pounds(x)
        case "K":
            return grams_to_kilograms(x)
        case _:
            raise InvalidUnitError("`unit_to is not an accepted mass unit")

def pounds_to_grams(x: float) -> float:
    return round(x * 453.592, NDIGITS)

def kilograms_to_grams(x: float) -> float:
    return round(x / 1000, NDIGITS)

def grams_to_pounds(x: float) -> float:
    return round(x / 453.592, NDIGITS)

def grams_to_kilograms(x: float) -> float:
    return round(x * 1000, NDIGITS)
