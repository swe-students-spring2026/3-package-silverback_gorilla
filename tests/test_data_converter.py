import pytest

from src.unit_convert.converter_types import InvalidUnitError, UnitData
from src.unit_convert.data_converter import convert_data


EPSILON = 0.000001


def _is_close_enough(v1: float, v2: float) -> bool:
    return abs(v1 - v2) < EPSILON


class TestDataConvert:
    def test_convert_data_same_unit(self):
        assert _is_close_enough(convert_data(10, UnitData.MB, UnitData.MB), 10)
        assert _is_close_enough(convert_data(1.23456, UnitData.GB, UnitData.GB), 1.2346)

    def test_convert_data_bytes_to_bits_and_back(self):
        assert _is_close_enough(convert_data(1, UnitData.B, UnitData.b), 8)
        assert _is_close_enough(convert_data(1024, UnitData.B, UnitData.KB), 1)
        assert _is_close_enough(convert_data(1, UnitData.MB, UnitData.Kb), 8192)
        assert _is_close_enough(convert_data(1, UnitData.Gb, UnitData.MB), 128)

    def test_convert_data_large_units(self):
        assert _is_close_enough(convert_data(2, UnitData.TB, UnitData.GB), 2048)
        assert _is_close_enough(convert_data(3, UnitData.PB, UnitData.TB), 3072)
        assert _is_close_enough(convert_data(1.5, UnitData.EB, UnitData.PB), 1536)

    def test_convert_data_invalid_units(self):
        with pytest.raises(InvalidUnitError):
            convert_data(10, "MB", UnitData.GB)

        with pytest.raises(InvalidUnitError):
            convert_data(10, UnitData.MB, "GB")

    def test_convert_data_invalid_value_types(self):
        with pytest.raises(InvalidUnitError):
            convert_data("A", UnitData.B, UnitData.b)

        with pytest.raises(InvalidUnitError):
            convert_data(None, UnitData.B, UnitData.b)
