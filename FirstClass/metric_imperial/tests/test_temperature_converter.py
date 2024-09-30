import unittest
from temperature_converter import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        converter = TemperatureConverter(0.00, 'C')
        result = converter.convert('F')
        expected = 32.00
        self.assertEqual(result, expected)

    def test_celsius_to_kelvin(self):
        converter = TemperatureConverter(0.00, 'C')
        result = converter.convert('K')
        expected = 273.15
        self.assertEqual(result, expected)

    def test_fahrenheit_to_celsius(self):
        converter = TemperatureConverter(32.00, 'F')
        result = converter.convert('C')
        expected = 0.00
        self.assertEqual(result, expected)

    def test_fahrenheit_to_kelvin(self):
        converter = TemperatureConverter(32.00, 'F')
        result = converter.convert('K')
        expected = 273.15
        self.assertEqual(result, expected)

    def test_kelvin_to_celsius(self):
        converter = TemperatureConverter(273.15, 'K')
        result = converter.convert('C')
        expected = 0.00
        self.assertEqual(result, expected)

    def test_kelvin_to_fahrenheit(self):
        converter = TemperatureConverter(273.15, 'K')
        result = converter.convert('F')
        expected = 32.00
        self.assertEqual(result, expected)

    def test_invalid_conversion(self):
        converter = TemperatureConverter(0.00, 'C')
        with self.assertRaises(ValueError):
            converter.convert('X')

if __name__ == '__main__':
    unittest.main()