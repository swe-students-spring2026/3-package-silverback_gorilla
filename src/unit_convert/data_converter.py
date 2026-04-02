from .converter_types import InvalidUnitError, UnitData

NDIGITS = 8
SAME_UNIT_NDIGITS = 4


def convert_data(x: float, unit_from: UnitData, unit_to: UnitData) -> float:
    byte_to_unit_ratios = {
        # Bytes
        "byte": 1,
        "kilobyte": 1 / 1024,
        "megabyte": 1 / (1024 ** 2),
        "gigabyte": 1 / (1024 ** 3),
        "terabyte": 1 / (1024 ** 4),
        "petabyte": 1 / (1024 ** 5),
        "exabyte": 1 / (1024 ** 6),
        # Bits
        "bit": 8,
        "kilobit": 8 / 1024,
        "megabit": 8 / (1024 ** 2),
        "gigabit": 8 / (1024 ** 3),
        "terabit": 8 / (1024 ** 4),
    }

    if unit_from == unit_to:
        return round(x, SAME_UNIT_NDIGITS)
    try:
        if(unit_from.value not in byte_to_unit_ratios):
            raise InvalidUnitError("`unit_from` is not an accepted data unit")
        if(unit_to.value not in byte_to_unit_ratios):
            raise InvalidUnitError("`unit_to` is not an accepted data unit")

        result = x / byte_to_unit_ratios[unit_from.value] * byte_to_unit_ratios[unit_to.value]

        return round(result, NDIGITS)

    except (AttributeError, TypeError):
        raise InvalidUnitError("Invalid data unit provided")