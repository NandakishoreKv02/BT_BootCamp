"""Lab 5: Tests - Validation Engine"""
import unittest
from starter_code import RangeValidator, PatternValidator, ValidatorChain


class TestRangeValidator(unittest.TestCase):
    def test_valid_value(self):
        v = RangeValidator(0, 100, "score")
        self.assertTrue(v(50))
    
    def test_invalid_value(self):
        v = RangeValidator(0, 100, "score")
        with self.assertRaises(ValueError):
            v(150)
    
    def test_error_message(self):
        v = RangeValidator(0, 100, "score")
        try:
            v(150)
        except ValueError as e:
            self.assertIn("score", str(e))
            self.assertIn("150", str(e))


class TestPatternValidator(unittest.TestCase):
    def test_valid_pattern(self):
        v = PatternValidator(r"P\d{3}", "patient_id")
        self.assertTrue(v("P001"))
    
    def test_invalid_pattern(self):
        v = PatternValidator(r"P\d{3}", "patient_id")
        with self.assertRaises(ValueError):
            v("X001")


class TestValidatorChain(unittest.TestCase):
    def test_chain_passes(self):
        chain = ValidatorChain([
            RangeValidator(0, 100, "value"),
        ])
        self.assertTrue(chain(50))
    
    def test_chain_fails(self):
        chain = ValidatorChain([
            RangeValidator(0, 100, "value"),
        ])
        with self.assertRaises(ValueError):
            chain(150)


if __name__ == "__main__":
    unittest.main()
