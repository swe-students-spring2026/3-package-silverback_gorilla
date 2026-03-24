from unit_convert.converter_types import InvalidUnitError, UnitTemperature

NDIGITS = 4

def convert_temperature(x: float, unit_from: UnitTemperature, unit_to: UnitTemperature) -> float:

    if unit_from == unit_to: return x

    match unit_from.name:
        case "C":
            pass
        case "F":
            x = fahrenheit_to_celsius(x)
        case "K":
            x = kelvin_to_celsius(x)
        case _:
            raise InvalidUnitError("`unit_from` is not an accepted temperature unit")

    match unit_to.name:
        case "C":
            return x
        case "F":
            return celsius_to_fahrenheit(x)
        case "K":
            return celsius_to_kelvin(x)
        case _:
            raise InvalidUnitError("`unit_to is not an accepted temperature unit")

def fahrenheit_to_celsius(x: float) -> float:
    return round((x - 32) / 1.8, NDIGITS)

def kelvin_to_celsius(x: float) -> float:
    return round(x - 273.15, NDIGITS)

def celsius_to_kelvin(x: float) -> float:
    return round(x + 273.15, NDIGITS)

def celsius_to_fahrenheit(x: float) -> float:
    return round(x * 1.8 + 32, NDIGITS)

