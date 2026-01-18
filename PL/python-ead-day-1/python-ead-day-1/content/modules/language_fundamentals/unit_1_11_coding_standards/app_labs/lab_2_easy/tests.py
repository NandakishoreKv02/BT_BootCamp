import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestCriticalConstants(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_alert_low(self):
        self.assertEqual(starter_code.check_vital_alert(40), "ALERT")

    def test_alert_high(self):
        self.assertEqual(starter_code.check_vital_alert(120), "ALERT")

    def test_normal(self):
        self.assertEqual(starter_code.check_vital_alert(80), "NORMAL")

    def test_constant_presence(self):
        self.assertTrue(hasattr(starter_code, "MAX_NORMAL_HR"))

if __name__ == '__main__':
    unittest.main()
