import unittest
from src.test_project.test import add_numbers, subtract_numbers

class TestMathOperations(unittest.TestCase):
    def test_add_numbers(self):
        # Test addition of positive numbers
        self.assertEqual(add_numbers(3, 5), 8)
        # Test addition of negative numbers
        self.assertEqual(add_numbers(-3, -5), -8)
        # Test addition of a positive and a negative number
        self.assertEqual(add_numbers(3, -5), -2)
        # Test addition of floats
        self.assertAlmostEqual(add_numbers(2.5, 3.1), 5.6)

    def test_subtract_numbers(self):
        # Test subtraction of positive numbers
        self.assertEqual(subtract_numbers(10, 5), 5)
        # Test subtraction of negative numbers
        self.assertEqual(subtract_numbers(-10, -5), -5)
        # Test subtraction of a positive and a negative number
        self.assertEqual(subtract_numbers(10, -5), 15)
        # Test subtraction of floats
        self.assertAlmostEqual(subtract_numbers(5.5, 2.2), 3.3)

if __name__ == "__main__":
    unittest.main()