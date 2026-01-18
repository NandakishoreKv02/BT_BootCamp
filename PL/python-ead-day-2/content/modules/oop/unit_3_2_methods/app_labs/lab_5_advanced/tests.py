import unittest
from starter_code import Patient

class TestBMI(unittest.TestCase):
    def test_calculation(self):
        # 70 / (1.75 * 1.75) = 22.857...
        self.assertEqual(Patient.calculate_bmi(70, 1.75), 22.86)

    def test_zero_division(self):
        self.assertEqual(Patient.calculate_bmi(70, 0), 0.0)

    def test_instance_usage(self):
        p = Patient("Test", 80, 1.8)
        # 80 / (1.8 * 1.8) = 24.6913...
        self.assertEqual(p.get_my_bmi(), 24.69)

if __name__ == "__main__":
    unittest.main()
