from .converter_types import InvalidUnitError, UnitDistance

def convert_distance(x: float, unit_from: UnitDistance, unit_to: UnitDistance) -> float:
    if(unit_from == unit_to): return x
    
    meter_to_unit_ratios = {
        "femtometer": 1_000_000_000_000_000,
        "picometer":  1_000_000_000_000,
        "nanometer":  1_000_000_000,
        "micrometer": 1_000_000,
        "millimeter": 1000,
        "centimeter": 100,
        "meter":      1,
        "kilometer":  0.001,
        "inch":       39.3700787, # 39.37,
        "feet":       3.2808399, # 3.281,
        "yard":       1.0936133, # 1.094,
        "mile":       1/1609.344 # 1/1609,
    }

    if(unit_from.value not in meter_to_unit_ratios):
        raise InvalidUnitError("`unit_from` is not an accepted distance unit")
    if(unit_to.value not in meter_to_unit_ratios):
        raise InvalidUnitError("`unit_to` is not an accepted distance unit")

    return x / meter_to_unit_ratios[unit_from.value] * meter_to_unit_ratios[unit_to.value]
