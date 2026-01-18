import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestRiskOrchestrator(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_total_score(self):
        # Age 50 (5) + HR 80 (0) + Diab False (0) = 5
        self.assertEqual(starter_code.get_total_risk(50, 80, False), 5)
        # Age 25 (2) + HR 150 (5) + Diab True (10) = 17
        self.assertEqual(starter_code.get_total_risk(25, 150, True), 17)

    def test_helpers_logic(self):
        self.assertEqual(starter_code._calc_age_factor(49), 4)
        self.assertEqual(starter_code._calc_vital_factor(100), 0)
        self.assertEqual(starter_code._calc_lab_factor(True), 10)

if __name__ == '__main__':
    unittest.main()
