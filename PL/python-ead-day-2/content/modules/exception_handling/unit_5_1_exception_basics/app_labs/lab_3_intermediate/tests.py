import unittest
from starter_code import calculate_dose_per_intake

class TestLab3(unittest.TestCase):
    def test_success(self):
        self.assertEqual(calculate_dose_per_intake(100, 3), 33.33)

    def test_zero_division(self):
        self.assertIsNone(calculate_dose_per_intake(100, 0))

    def test_invalid_types(self):
        self.assertIsNone(calculate_dose_per_intake("100", 2))
        self.assertIsNone(calculate_dose_per_intake(100, "2"))

if __name__ == "__main__":
    unittest.main()
