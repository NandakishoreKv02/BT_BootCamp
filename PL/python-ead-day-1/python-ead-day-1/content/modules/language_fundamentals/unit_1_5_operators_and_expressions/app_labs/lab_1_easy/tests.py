import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestPediatricDose(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_standard_dose(self):
        # 15.5 * 10 = 155.0
        self.assertEqual(starter_code.calculate_mg_dose(15.5, 10), 155.0)

    def test_rounding(self):
        # 12.33 * 5 = 61.65 -> 61.7 or 61.6 depending on round() behavior
        # Let's use 12.3 * 5.2 = 63.96 -> 64.0
        self.assertEqual(starter_code.calculate_mg_dose(12.3, 5.2), 64.0)

    def test_invalid_weight(self):
        self.assertEqual(starter_code.calculate_mg_dose(0, 10), 0.0)
        self.assertEqual(starter_code.calculate_mg_dose(-5, 10), 0.0)

if __name__ == '__main__':
    unittest.main()
