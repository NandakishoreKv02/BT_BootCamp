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

    def test_calculation(self):
        # (10mg/kg * 15kg) / 3 doses = 50.0
        self.assertEqual(starter_code.calculate_dosage(10, 15, 3), 50.0)

    def test_precision(self):
        # (7mg/kg * 10kg) / 3 doses = 23.333... -> 23.3
        self.assertEqual(starter_code.calculate_dosage(7, 10, 3, precision=1), 23.3)

if __name__ == '__main__':
    unittest.main()
