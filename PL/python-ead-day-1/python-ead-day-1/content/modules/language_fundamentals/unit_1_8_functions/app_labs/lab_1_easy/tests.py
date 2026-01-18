import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestVitalFormatter(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_standard_format(self):
        res = starter_code.format_vital("HR", 75, "BPM")
        self.assertEqual(res, "HR: 75 BPM")

    def test_float_format(self):
        res = starter_code.format_vital("Temp", 36.8, "C")
        self.assertEqual(res, "Temp: 36.8 C")

if __name__ == '__main__':
    unittest.main()
