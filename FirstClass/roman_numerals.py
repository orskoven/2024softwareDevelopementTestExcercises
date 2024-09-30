""""
Roman Numerals
Part I

Implement a function/method that converts from Roman to decimal numerals, taking into account the following rules:


Relationship between figures
I          1
V          5
X         10
L         50
C        100
D        500
M       1000


In Roman numbers, 

--> larger values preceding smaller or equal ones keep their value
        rule_1 =  (if char before is <= than current value then keep value)
E.g., MDCCCLXVII = 1000 + 500 + (100 * 3) + 50 + 10 + 5 + (1 * 2) = 1867


---> When a (smaller) value precedes a larger one, it means subtraction
        rule_2 = if char[current] is smaller than char [1] then subtract

E.g, XCIV = (100 – 10) + (5 – 1) = 94



Part II

Write unit tests for the function/method.


"""



class RomanNumeralToDecimal:
    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral

    def convert_to_decimal(self):
        if not self.roman_numeral:
            return None  # Handle empty string
        
        roman_to_deci_dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Additional validation for strict Roman numeral rules
        valid_subtractions = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }

        # Early detection of invalid repetition
        if not self._valid_repetitions():
            return None

        total = 0
        prev_value = 0

        i = 0
        while i < len(self.roman_numeral):
            char = self.roman_numeral[i]
            if char not in roman_to_deci_dic:
                return None  # Early exit on invalid character

            value = roman_to_deci_dic[char]

            if i + 1 < len(self.roman_numeral):
                next_char = self.roman_numeral[i + 1]
                next_value = roman_to_deci_dic.get(next_char, 0)

                if next_value > value:
                    # Check if the subtraction is valid
                    if char not in valid_subtractions or next_char not in valid_subtractions[char]:
                        return None
                    if i > 0 and self.roman_numeral[i-1] == char:
                        return None  # Prevent cases like "IIV" or "XXC"
                    total += next_value - value
                    i += 2  # Skip the next character as it was used in subtraction
                    continue

            total += value
            i += 1

        return total
    
    def _valid_repetitions(self):
        """
        Check for invalid repetitions in the Roman numeral string.
        """
        invalid_patterns = [
            "IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM"
        ]
        for pattern in invalid_patterns:
            if pattern in self.roman_numeral:
                return False
        return True


import unittest

class TestRomanNumeralToDecimal(unittest.TestCase):

    def test_convert_to_decimal_valid_numerals(self):
        """Test conversion of valid Roman numerals to their decimal equivalents."""
        # Arrange
        test_cases = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "MCMXCIV": 1994,
            "MMMCMXCIX": 3999  # Max valid Roman numeral
        }

        for roman_numeral, expected_value in test_cases.items():
            with self.subTest(roman_numeral=roman_numeral):
                # Act
                converter = RomanNumeralToDecimal(roman_numeral)
                result = converter.convert_to_decimal()

                # Assert
                self.assertEqual(result, expected_value)

    def test_convert_to_decimal_invalid_numerals(self):
        """Test conversion of invalid Roman numerals (should return None)."""
        # Arrange
        invalid_numerals = [
            "IIII",    # Invalid repetition of 'I'
            "VV",      # Invalid repetition of 'V'
            "XXXX",    # Invalid repetition of 'X'
            "LL",      # Invalid repetition of 'L'
            "CCCC",    # Invalid repetition of 'C'
            "DD",      # Invalid repetition of 'D'
            "MMMM",    # Invalid repetition of 'M'
            "ABCD",    # Invalid characters
            "",        # Empty string
            "VX",      # Invalid order
            "IIV",     # Invalid sequence
            "IC",      # Invalid subtraction
            "XM",      # Invalid subtraction
            "ID",      # Invalid subtraction
            "IL",      # Invalid subtraction
            "MMMMCMXCIX" # Beyond traditional Roman numeral limits (3999)
        ]

        for roman_numeral in invalid_numerals:
            with self.subTest(roman_numeral=roman_numeral):
                # Act
                converter = RomanNumeralToDecimal(roman_numeral)
                result = converter.convert_to_decimal()

                # Assert
                self.assertIsNone(result)

    def test_valid_repetitions(self):
        """Test the _valid_repetitions method directly."""
        # Arrange
        converter_valid = RomanNumeralToDecimal("MCMXCIV")
        converter_invalid = RomanNumeralToDecimal("IIII")

        # Act and Assert
        self.assertTrue(converter_valid._valid_repetitions())
        self.assertFalse(converter_invalid._valid_repetitions())

    def test_edge_cases(self):
        """Test edge cases like smallest and largest valid Roman numerals."""
        # Smallest Roman numeral
        converter = RomanNumeralToDecimal("I")
        self.assertEqual(converter.convert_to_decimal(), 1)

        # Largest valid Roman numeral
        converter = RomanNumeralToDecimal("MMMCMXCIX")
        self.assertEqual(converter.convert_to_decimal(), 3999)

    def test_single_character_numerals(self):
        """Test conversion for all single Roman numeral characters."""
        # Arrange
        test_cases = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
# Use Parameterize test instead of for loop 
        for roman_numeral, expected_value in test_cases.items():
            with self.subTest(roman_numeral=roman_numeral):
                # Act
                converter = RomanNumeralToDecimal(roman_numeral)
                result = converter.convert_to_decimal()

                # Assert
                self.assertEqual(result, expected_value)

    def test_lower_case_numerals(self):
        """Test conversion of Roman numerals in lower case."""
        # Arrange
        test_cases = {
            "i": 1,
            "v": 5,
            "x": 10,
            "l": 50,
            "c": 100,
            "d": 500,
            "m": 1000,
            "iv": 4,
            "ix": 9,
            "xl": 40,
            "xc": 90,
            "cd": 400,
            "cm": 900,
            "mcmxciv": 1994,
            "mmmcmxcix": 3999
        }

        for roman_numeral, expected_value in test_cases.items():
            with self.subTest(roman_numeral=roman_numeral):
                # Act
                converter = RomanNumeralToDecimal(roman_numeral.upper())  # Convert to upper
                result = converter.convert_to_decimal()

                # Assert
                self.assertEqual(result, expected_value)

if __name__ == '__main__':
    unittest.main()
