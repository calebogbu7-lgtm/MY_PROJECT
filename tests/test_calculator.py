import unittest
from src.calculator import calculate
from src.calculator import calculate, format_result

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate("4 + 5"), 9)

    def test_subtraction(self):
        self.assertEqual(calculate("10 - 3"), 7)

    def test_multiplication(self):
        self.assertEqual(calculate("6 * 7"), 42)

    def test_multiplication_with_x_symbol(self):
        self.assertEqual(calculate("6 x 7"), 42)
        self.assertEqual(calculate("6 X 7"), 42)

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
    
    def test_exponent_greater_than_100(self):
        self.assertEqual(calculate("2 ** 101"), 2 ** 101)

    def test_large_integer_calculation(self):
        self.assertEqual(calculate("2 ** 1000"), 2 ** 1000)

    
    def test_large_integer_formatting(self):
        result = calculate("2 ** 1000")
        formatted = format_result(result)

        self.assertIn("e+", formatted)


    def test_normal_result_formatting(self):
        self.assertEqual(format_result(25), "25")

 
    
    
    def test_exponent_within_limit(self):
        self.assertEqual(calculate("2 ** 100"), 2 ** 100)


    def test_exponent_over_limit(self):
        self.assertEqual(
        calculate("2 ** 10001"),
        "Calculation overflow"
    )


    def test_extremely_large_exponent(self):
        self.assertEqual(
        calculate("6767677 ** 4554554555"),
        "Calculation overflow"
    )


if __name__ == "__main__":
    unittest.main()