from unit_convert.converter_types import InvalidUnitError, UnitData

NDIGITS = 4


def convert_data(x: float, unit_from: UnitData, unit_to: UnitData) -> float:
    if unit_from == unit_to:
        return round(x, NDIGITS)

    try:
        # Convert to base unit (bytes).
        bytes_value = x * unit_from.value

        # Convert to target unit.
        result = bytes_value / unit_to.value

        return round(result, NDIGITS)

    except (AttributeError, TypeError):
        raise InvalidUnitError("Invalid data unit provided")


# Backward compatible alias.
DataUnit = UnitData