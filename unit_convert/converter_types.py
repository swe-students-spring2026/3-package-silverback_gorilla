
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


class UnitData(Enum):
    # Bytes
    B = "byte"
    KB = "kilobyte"
    MB = "megabyte"
    GB = "gigabyte"
    TB = "terabyte"
    PB = "petabyte"
    EB = "exabyte"

    # Bits
    b = "bit"
    Kb = "kilobit"
    Mb = "megabit"
    Gb = "gigabit"
    Tb = "terabit"
