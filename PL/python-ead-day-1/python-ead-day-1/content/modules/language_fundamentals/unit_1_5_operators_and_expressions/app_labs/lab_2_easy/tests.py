import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestTriageAlert(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_high_hr(self):
        self.assertTrue(starter_code.is_alert_triggered(101))
        self.assertTrue(starter_code.is_alert_triggered(150))

    def test_low_hr(self):
        self.assertTrue(starter_code.is_alert_triggered(59))
        self.assertTrue(starter_code.is_alert_triggered(40))

    def test_normal_hr(self):
        self.assertFalse(starter_code.is_alert_triggered(60))
        self.assertFalse(starter_code.is_alert_triggered(85))
        self.assertFalse(starter_code.is_alert_triggered(100))

if __name__ == '__main__':
    unittest.main()
