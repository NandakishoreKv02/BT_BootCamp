import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestBMICalculator(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_calculate_bmi(self):
        bmi = starter_code.calculate_bmi(70, 1.75)
        self.assertAlmostEqual(bmi, 22.86, places=2)

    def test_categorize_underweight(self):
        self.assertEqual(starter_code.categorize_bmi(17.5), "Underweight")

    def test_categorize_normal(self):
        self.assertEqual(starter_code.categorize_bmi(22.0), "Normal Weight")

    def test_categorize_overweight(self):
        self.assertEqual(starter_code.categorize_bmi(27.0), "Overweight")

    def test_categorize_obese(self):
        self.assertEqual(starter_code.categorize_bmi(32.0), "Obese")

    def test_recommendation_exists(self):
        rec = starter_code.generate_recommendation("Normal Weight")
        self.assertIsInstance(rec, str)
        self.assertTrue(len(rec) > 0)

if __name__ == '__main__':
    unittest.main()
