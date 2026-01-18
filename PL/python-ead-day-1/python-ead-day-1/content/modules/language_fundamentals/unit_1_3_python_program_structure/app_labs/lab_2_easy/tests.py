import unittest
import importlib.util
import sys

# Import the student's code
try:
    import starter_code
except ImportError:
    pass

class TestVitalSigns(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_constants_exist(self):
        """Check if constants are defined (basic check for variable naming or presence)."""
        # It's hard to strictly check constants without parsing code, but we check logic functionality.
        pass

    def test_critical_condition(self):
        """Test Critical conditions."""
        # SpO2 < 90
        self.assertEqual(starter_code.check_vitals(80, 89), "Critical")
        # HR > 120 AND SpO2 < 95
        self.assertEqual(starter_code.check_vitals(121, 94), "Critical")

    def test_warning_condition(self):
        """Test Warning conditions."""
        # SpO2 < 95 (but >= 90)
        self.assertEqual(starter_code.check_vitals(80, 94), "Warning")
        self.assertEqual(starter_code.check_vitals(80, 90), "Warning")
        # HR > 100
        self.assertEqual(starter_code.check_vitals(110, 98), "Warning")

    def test_stable_condition(self):
        """Test Stable conditions."""
        self.assertEqual(starter_code.check_vitals(80, 98), "Stable")
        self.assertEqual(starter_code.check_vitals(60, 95), "Stable")
        self.assertEqual(starter_code.check_vitals(100, 95), "Stable")

    def test_input_validation(self):
        """Test validation for invalid inputs."""
        self.assertEqual(starter_code.check_vitals(80, 101), "Invalid Input")
        self.assertEqual(starter_code.check_vitals(80, -5), "Invalid Input")
        self.assertEqual(starter_code.check_vitals(-10, 98), "Invalid Input")

if __name__ == '__main__':
    unittest.main()
