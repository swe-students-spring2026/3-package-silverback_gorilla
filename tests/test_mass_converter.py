import pytest
from unit_convert import mass_converter

EPSILON = 0.00000001

class TestTemperatureConvert:

    def test_pounds_to_grams(self):
        assert abs(mass_converter.pounds_to_grams(0)) < EPSILON
        assert abs(mass_converter.pounds_to_grams(3) - 1360.78) < EPSILON
        assert abs(mass_converter.pounds_to_grams(0.220462) - 100) < EPSILON
        assert abs(mass_converter.pounds_to_grams(-5) + -2267.96) < EPSILON
        with pytest.raises(TypeError):
            mass_converter.pounds_to_grams("A")

    def test_kilograms_to_grams(self):
        assert abs(mass_converter.kilograms_to_grams(0)) < EPSILON
        assert abs(mass_converter.kilograms_to_grams(10) - 10000) < EPSILON
        assert abs(mass_converter.kilograms_to_grams(0.2) - 200) < EPSILON
        assert abs(mass_converter.kilograms_to_grams(-3) + 3000) < EPSILON
        with pytest.raises(TypeError):
            mass_converter.kilograms_to_grams("A")

    def test_grams_to_pounds(self):
        assert abs(mass_converter.grams_to_pounds(0)) < EPSILON
        assert abs(mass_converter.grams_to_pounds(12) - 0.0264555) < EPSILON
        assert abs(mass_converter.grams_to_pounds(2000) - 4.409245) < EPSILON
        assert abs(mass_converter.grams_to_pounds(-500) + 1.10231) < EPSILON
        with pytest.raises(TypeError):
            mass_converter.grams_to_pounds("A")

    def test_grams_to_kilograms(self):
        assert abs(mass_converter.grams_to_kilograms(0)) < EPSILON
        assert abs(mass_converter.grams_to_kilograms(40) - 0.04) < EPSILON
        assert abs(mass_converter.grams_to_kilograms(2532) - 2.532) < EPSILON
        assert abs(mass_converter.grams_to_kilograms(-100) + 0.1) < EPSILON
        with pytest.raises(TypeError):
            mass_converter.grams_to_kilograms("A")
        
    #Converting back and forth should have no change
    def test_convert_temperature(self):
        assert abs(mass_converter.convert_mass(0, mass_converter.UnitMass.G, mass_converter.UnitMass.G)) < EPSILON
        assert abs(mass_converter.convert_mass(0, mass_converter.UnitMass.G, mass_converter.UnitMass.P)) < EPSILON
        assert abs(mass_converter.convert_mass(0, mass_converter.UnitMass.G, mass_converter.UnitMass.K)) < EPSILON

        assert abs(mass_converter.convert_mass(0, mass_converter.UnitMass.P, mass_converter.UnitMass.G)) < EPSILON
        assert abs(mass_converter.convert_mass(0, mass_converter.UnitMass.P, mass_converter.UnitMass.P)) < EPSILON
        assert abs(mass_converter.convert_mass(0, mass_converter.UnitMass.P, mass_converter.UnitMass.K)) < EPSILON

        assert abs(mass_converter.convert_mass(0, mass_converter.UnitMass.K, mass_converter.UnitMass.G)) < EPSILON
        assert abs(mass_converter.convert_mass(0, mass_converter.UnitMass.K, mass_converter.UnitMass.P)) < EPSILON
        assert abs(mass_converter.convert_mass(0, mass_converter.UnitMass.K, mass_converter.UnitMass.K)) < EPSILON

        with pytest.raises(mass_converter.InvalidUnitError):
            mass_converter.convert_mass(0, "gram", mass_converter.UnitMass.G)
            mass_converter.convert_mass(0, mass_converter.UnitMass.G, "gram")
            
        with pytest.raises(TypeError):
            mass_converter.convert_mass(mass_converter.convert_mass("A", mass_converter.UnitMass.G, mass_converter.UnitMass.G))