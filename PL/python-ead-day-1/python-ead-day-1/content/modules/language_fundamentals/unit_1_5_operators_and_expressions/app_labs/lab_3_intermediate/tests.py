import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestMultiVitalAlert(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_temp_spo2_trigger(self):
        # (39.5 > 39.0) AND (90 < 92) -> True
        self.assertTrue(starter_code.should_trigger_critical_alert(39.5, 90, True))

    def test_unconscious_trigger(self):
        # is_conscious == False -> True
        self.assertTrue(starter_code.should_trigger_critical_alert(37.0, 98, False))

    def test_normal_no_trigger(self):
        # Neither condition met
        self.assertFalse(starter_code.should_trigger_critical_alert(38.5, 98, True))
        
    def test_high_temp_safe_spo2(self):
        # 40 > 39 but 95 > 92 -> False (for first condition)
        self.assertFalse(starter_code.should_trigger_critical_alert(40.0, 95, True))

if __name__ == '__main__':
    unittest.main()
