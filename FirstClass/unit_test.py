# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """This method is called before each test. It creates a Calculator instance."""
        self.calc = Calculator(3, 9)
    
    def test_sum(self):
        # Arrange
        expected_result = 12
        
        # Act
        result = self.calc.add()
        
        # Assert
        self.assertEqual(result, expected_result)
        
    def test_subtract(self):
        # Arrange
        expected_result = -6
        
        # Act
        result = self.calc.subtract()
        
        # Assert
        self.assertEqual(result, expected_result)
        
    def test_divide(self):
        # Arrange
        expected_result = 1/3  # Expected result based on 3 / 9
        
        # Act
        result = self.calc.divide()
        
        # Assert
        self.assertEqual(result, expected_result)
        
    def test_multiply(self):
        # Arrange
        expected_result = 27
        
        # Act
        result = self.calc.multiply()
        
        # Assert
        self.assertEqual(result, expected_result)
        
    def test_divide_by_zero(self):
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            calc = Calculator(3, 0)  # Create a new calculator object with b = 0
            calc.divide()
        
        self.assertEqual(str(context.exception), "Cannot divide by zero") 
        
if __name__ == '__main__':
    unittest.main()
