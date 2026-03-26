import pytest
from unit_convert import mass_converter

EPSILON = 1e-6
POUNDS_TO_GRAMS = 453.59237

class TestMassConvert:

    def test_pounds_to_grams(self):
        assert abs(mass_converter.pounds_to_grams(0)) < EPSILON
        assert abs(mass_converter.pounds_to_grams(3) - (3 * POUNDS_TO_GRAMS)) < EPSILON
        assert abs(mass_converter.pounds_to_grams(0.220462) - (0.220462 * POUNDS_TO_GRAMS)) < EPSILON
        assert abs(mass_converter.pounds_to_grams(-5) - (-5 * POUNDS_TO_GRAMS)) < EPSILON

        with pytest.raises(TypeError):
            mass_converter.pounds_to_grams("A")

    def test_kilograms_to_grams(self):
        assert abs(mass_converter.kilograms_to_grams(0)) < EPSILON
        assert abs(mass_converter.kilograms_to_grams(10) - 10000) < EPSILON
        assert abs(mass_converter.kilograms_to_grams(0.2) - 200) < EPSILON
        assert abs(mass_converter.kilograms_to_grams(-3) - (-3000)) < EPSILON

        with pytest.raises(TypeError):
            mass_converter.kilograms_to_grams("A")

    def test_grams_to_pounds(self):
        assert abs(mass_converter.grams_to_pounds(0)) < EPSILON
        assert abs(mass_converter.grams_to_pounds(12) - (12 / POUNDS_TO_GRAMS)) < EPSILON
        assert abs(mass_converter.grams_to_pounds(2000) - (2000 / POUNDS_TO_GRAMS)) < EPSILON
        assert abs(mass_converter.grams_to_pounds(-500) - (-500 / POUNDS_TO_GRAMS)) < EPSILON

        with pytest.raises(TypeError):
            mass_converter.grams_to_pounds("A")

    def test_grams_to_kilograms(self):
        assert abs(mass_converter.grams_to_kilograms(0)) < EPSILON
        assert abs(mass_converter.grams_to_kilograms(40) - 0.04) < EPSILON
        assert abs(mass_converter.grams_to_kilograms(2532) - 2.532) < EPSILON
        assert abs(mass_converter.grams_to_kilograms(-100) - (-0.1)) < EPSILON

        with pytest.raises(TypeError):
            mass_converter.grams_to_kilograms("A")

    def test_convert_mass(self):
        # Zero should stay the same after any conversion
        for u1 in mass_converter.UnitMass:
            for u2 in mass_converter.UnitMass:
                assert abs(mass_converter.convert_mass(0, u1, u2)) < EPSILON

        # Invalid inputs
        with pytest.raises(mass_converter.InvalidUnitError):
            mass_converter.convert_mass(0, "gram", mass_converter.UnitMass.G)

        with pytest.raises(mass_converter.InvalidUnitError):
            mass_converter.convert_mass(0, mass_converter.UnitMass.G, "gram")

        with pytest.raises(TypeError):
            mass_converter.convert_mass("2", mass_converter.UnitMass.G, mass_converter.UnitMass.G)
