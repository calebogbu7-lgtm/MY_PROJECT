import unittest
from src.calculator import calculate


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate("4 + 5"), 9)

    def test_subtraction(self):
        self.assertEqual(calculate("10 - 3"), 7)

    def test_multiplication(self):
        self.assertEqual(calculate("6 * 7"), 42)

    def test_division(self):
        self.assertEqual(calculate("20 / 4"), 5)

    def test_modulus(self):
        self.assertEqual(calculate("10 % 3"), 1)

    def test_exponentiation(self):
        self.assertEqual(calculate("2 ** 3"), 8)

    def test_operator_precedence(self):
        self.assertEqual(calculate("4 * 7 + 5 - 4"), 29)

    def test_brackets(self):
        self.assertEqual(calculate("(2 + 3) * 4"), 20)

    def test_negative_numbers(self):
        self.assertEqual(calculate("-5 + 2"), -3)

    def test_decimal_numbers(self):
        self.assertEqual(calculate("2.5 + 1.5"), 4.0)

    def test_division_by_zero(self):
        self.assertEqual(
            calculate("10 / 0"),
            "Cannot divide by zero"
        )

    def test_invalid_expression(self):
        self.assertEqual(calculate("4 +"), "Invalid expression")


if __name__ == "__main__":
    unittest.main()