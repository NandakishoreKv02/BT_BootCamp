import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestRiskScore(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_high_risk(self):
        # Age 65: 6
        # BP 140: (140-120)*0.5 = 10.0
        # Diabetes: 2.0
        # Total: 18.0
        self.assertEqual(starter_code.calculate_risk_score(65, 140, True), 18.0)

    def test_low_risk(self):
        # Age 25: 2
        # BP 110: (110-120)*0.5 = -5.0
        # Diabetes: 0.0
        # Total: -3.0
        self.assertEqual(starter_code.calculate_risk_score(25, 110, False), -3.0)

    def test_edge_diabetes_only(self):
        # Age 0: 0
        # BP 120: 0.0
        # Diabetes: 2.0
        self.assertEqual(starter_code.calculate_risk_score(0, 120, True), 2.0)

if __name__ == '__main__':
    unittest.main()
