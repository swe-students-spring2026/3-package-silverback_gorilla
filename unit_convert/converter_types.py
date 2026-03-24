
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
    # Bytes (binary, base = byte)
    B = 1
    KB = 1024
    MB = 1024 ** 2
    GB = 1024 ** 3
    TB = 1024 ** 4
    PB = 1024 ** 5
    EB = 1024 ** 6

    # Bits (1 byte = 8 bits)
    b = 1 / 8
    Kb = 1024 / 8
    Mb = (1024 ** 2) / 8
    Gb = (1024 ** 3) / 8
    Tb = (1024 ** 4) / 8
