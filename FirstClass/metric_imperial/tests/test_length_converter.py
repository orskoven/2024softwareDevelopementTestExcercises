import unittest
from length_converter import LengthConverter

class TestLengthConverter(unittest.TestCase):

    def test_metric_to_imperial(self):
        converter = LengthConverter(10.00, 'metric')
        result = converter.convert()
        expected = round(10.00 / 2.54, 2)
        self.assertEqual(result, expected)

    def test_imperial_to_metric(self):
        converter = LengthConverter(10.00, 'imperial')
        result = converter.convert()
        expected = round(10.00 * 2.54, 2)
        self.assertEqual(result, expected)

    def test_invalid_system(self):
        with self.assertRaises(ValueError):
            converter = LengthConverter(10.00, 'unknown')
            converter.convert()

    def test_zero_value(self):
        converter = LengthConverter(0.00, 'metric')
        result = converter.convert()
        expected = 0.00
        self.assertEqual(result, expected)

    def test_negative_value(self):
        converter = LengthConverter(-10.00, 'metric')
        result = converter.convert()
        expected = round(-10.00 / 2.54, 2)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()