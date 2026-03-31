from .converter_types import InvalidUnitError, UnitMass
import numbers

NDIGITS = 8

def convert_mass(x: float, unit_from: UnitMass, unit_to: UnitMass) -> float:

    if not isinstance(x, numbers.Number):
        raise TypeError("`x` is not a valid number")

    if unit_from == unit_to: return x

    #Convert to grams first
    match unit_from:
        case UnitMass.G:
            pass
        case UnitMass.P:
            x = pounds_to_grams(x)
        case UnitMass.K:
            x = kilograms_to_grams(x)
        case _:
            raise InvalidUnitError("`unit_from` is not an accepted mass unit")

    match unit_to:
        case UnitMass.G:
            return x
        case UnitMass.P:
            return grams_to_pounds(x)
        case UnitMass.K:
            return grams_to_kilograms(x)
        case _:
            raise InvalidUnitError("`unit_to is not an accepted mass unit")

def pounds_to_grams(x: float) -> float:
    return round(x * 453.59237, NDIGITS)

def kilograms_to_grams(x: float) -> float:
    return round(x * 1000, NDIGITS)

def grams_to_pounds(x: float) -> float:
    return round(x / 453.59237, NDIGITS)

def grams_to_kilograms(x: float) -> float:
    return round(x / 1000, NDIGITS)
