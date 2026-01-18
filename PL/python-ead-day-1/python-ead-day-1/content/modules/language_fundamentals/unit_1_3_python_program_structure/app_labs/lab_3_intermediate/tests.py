import unittest
import importlib.util
import sys
from datetime import datetime

try:
    import starter_code
except ImportError:
    pass

class TestMedScheduler(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_same_day(self):
        """Test calculation within the same day."""
        res = starter_code.calculate_next_dose("08:00", 4)
        self.assertEqual(res, "12:00")

    def test_next_day(self):
        """Test calculation crossing midnight."""
        res = starter_code.calculate_next_dose("22:00", 4)
        self.assertEqual(res, "02:00 (+1 day)")

    def test_exact_midnight(self):
        """Test calculation landing exactly on midnight."""
        res = starter_code.calculate_next_dose("20:00", 4)
        self.assertEqual(res, "00:00 (+1 day)")

if __name__ == '__main__':
    unittest.main()
