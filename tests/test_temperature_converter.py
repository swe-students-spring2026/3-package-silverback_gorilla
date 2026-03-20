import pytest
from unit_convert import temperature_converter

EPSILON = 0.000001

class TestTemperatureConvert:

    def test_fahrenheit_to_celsius(self):
        assert abs(temperature_converter.fahrenheit_to_celsius(32) - 0) < EPSILON
        assert abs(temperature_converter.fahrenheit_to_celsius(0) + 17.7778) < EPSILON
        assert abs(temperature_converter.fahrenheit_to_celsius(-50) + 45.5556) < EPSILON
        with pytest.raises(TypeError):
            temperature_converter.fahrenheit_to_celsius("A")

    def test_kelvin_to_celsius(self):
        assert abs(temperature_converter.kelvin_to_celsius(273.15) - 0) < EPSILON
        assert abs(temperature_converter.kelvin_to_celsius(0) + 273.15) < EPSILON
        assert abs(temperature_converter.kelvin_to_celsius(-500) + 773.15) < EPSILON
        with pytest.raises(TypeError):
            temperature_converter.kelvin_to_celsius("A")

    def test_celsius_to_kelvin(self):
        assert abs(temperature_converter.celsius_to_kelvin(100) - 373.15) < EPSILON
        assert abs(temperature_converter.celsius_to_kelvin(0) - 273.15) < EPSILON
        assert abs(temperature_converter.celsius_to_kelvin(-273.15) - 0 ) < EPSILON
        with pytest.raises(TypeError):
            temperature_converter.celsius_to_kelvin("A")

    def test_celsius_to_fahrenheit(self):
        assert abs(temperature_converter.celsius_to_fahrenheit(100) - 212) < EPSILON
        assert abs(temperature_converter.celsius_to_fahrenheit(0) - 32) < EPSILON
        assert abs(temperature_converter.celsius_to_fahrenheit(-100) + 148 ) < EPSILON
        with pytest.raises(TypeError):
            temperature_converter.celsius_to_fahrenheit("A")
        


    def test_convert_temperature(self):
        assert abs(temperature_converter.convert_temperature(0, temperature_converter.UnitTemperature.C, temperature_converter.UnitTemperature.C) - 0) < EPSILON
        assert abs(temperature_converter.convert_temperature(0, temperature_converter.UnitTemperature.C, temperature_converter.UnitTemperature.F) - 32) < EPSILON
        assert abs(temperature_converter.convert_temperature(0, temperature_converter.UnitTemperature.C, temperature_converter.UnitTemperature.K) - 273.15) < EPSILON

        assert abs(temperature_converter.convert_temperature(0, temperature_converter.UnitTemperature.F, temperature_converter.UnitTemperature.C) + 17.7778) < EPSILON
        assert abs(temperature_converter.convert_temperature(0, temperature_converter.UnitTemperature.F, temperature_converter.UnitTemperature.F) - 0) < EPSILON
        assert abs(temperature_converter.convert_temperature(0, temperature_converter.UnitTemperature.F, temperature_converter.UnitTemperature.K) - 255.3722) < EPSILON

        assert abs(temperature_converter.convert_temperature(0, temperature_converter.UnitTemperature.K, temperature_converter.UnitTemperature.C) + 273.15) < EPSILON
        assert abs(temperature_converter.convert_temperature(0, temperature_converter.UnitTemperature.K, temperature_converter.UnitTemperature.F) + 459.67) < EPSILON
        assert abs(temperature_converter.convert_temperature(0, temperature_converter.UnitTemperature.K, temperature_converter.UnitTemperature.K) - 0) < EPSILON

        with pytest.raises(temperature_converter.InvalidUnitError):
            temperature_converter.convert_temperature(0, "celsius", temperature_converter.UnitTemperature.C)
            temperature_converter.convert_temperature(0, temperature_converter.UnitTemperature.C, "celsius")
            
        with pytest.raises(TypeError):
            temperature_converter.convert_temperature(temperature_converter.convert_temperature("A", temperature_converter.UnitTemperature.K, temperature_converter.UnitTemperature.K))