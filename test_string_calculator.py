import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3,4"), 10)

    def test_newline_as_delimiter(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_negative_numbers_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3")
        self.assertIn("Negative numbers not allowed: -2", str(context.exception))

    def test_multiple_negative_numbers_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1,-2,3")
        self.assertIn("Negative numbers not allowed: -1, -2", str(context.exception))


if __name__ == "__main__":
    # Run tests with verbosity to show passed and failed test cases
    unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().loadTestsFromTestCase(TestStringCalculator))
