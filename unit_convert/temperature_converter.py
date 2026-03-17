from enum import Enum

class InvalidUnitError(Exception):
    pass

class UnitTemperature(Enum):
    C = "celsius"
    F = "fahrenheit"
    K = "kelvin"

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
            return celsius_to_fahrenheit(x)
        case _:
            raise InvalidUnitError("`unit_to is not an accepted temperature unit")

def fahrenheit_to_celsius(x: float) -> float:
    return (x - 32) / 1.8

def kelvin_to_celsius(x: float) -> float:
    return x - 273.15

def celsius_to_kelvin(x: float) -> float:
    return x + 273.15

def celsius_to_fahrenheit(x: float) -> float:
    return x * 1.8 + 32



