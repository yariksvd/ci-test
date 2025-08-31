import unittest
from calc import add, subtract, multiply, divide


class TestCalcFunctions(unittest.TestCase):

    def test_add(self):
        """Test the add function with various inputs"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)

    def test_subtract(self):
        """Test the subtract function with various inputs"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(10, 15), -5)
        self.assertEqual(subtract(2.5, 1.5), 1.0)

    def test_multiply(self):
        """Test the multiply function with various inputs"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(2.5, 4), 10.0)

    def test_divide(self):
        """Test the divide function with various inputs"""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(15, 3), 5.0)
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(0, 5), 0.0)

    def test_divide_by_zero(self):
        """Test that divide function raises AssertionError when dividing by zero"""
        with self.assertRaises(AssertionError):
            divide(10, 0)
        with self.assertRaises(AssertionError):
            divide(-5, 0)
        with self.assertRaises(AssertionError):
            divide(0, 0)


if __name__ == '__main__':
    unittest.main()