import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestThresholds(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_constants_exist(self):
        # Check if they defined constants (by name or usage logic)
        # We test usage logic
        pass

    def test_fever(self):
        self.assertTrue(starter_code.is_fever(38.0))
        self.assertTrue(starter_code.is_fever(39.5))
        self.assertFalse(starter_code.is_fever(37.9))

    def test_hypertension(self):
        # Systolic trigger
        self.assertTrue(starter_code.is_hypertensive(145, 80))
        # Diastolic trigger
        self.assertTrue(starter_code.is_hypertensive(120, 95))
        # Both
        self.assertTrue(starter_code.is_hypertensive(160, 100))
        # Fine
        self.assertFalse(starter_code.is_hypertensive(120, 80))

if __name__ == '__main__':
    unittest.main()
