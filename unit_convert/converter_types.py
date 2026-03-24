
class InvalidUnitError(Exception):
    pass

from enum import Enum

class UnitTemperature(Enum):
    C = "celsius"
    F = "fahrenheit"
    K = "kelvin"

class UnitDistance(Enum):
    FM = "femtometer"
    PM = "picometer"
    NM = "nanometer"
    UM = "micrometer"
    MM = "millimeter"
    CM = "centimeter"
    M  = "meter"
    KM = "kilometer"
    IN = "inch"
    FT = "feet"
    YD = "yard"
    MI = "mile"
