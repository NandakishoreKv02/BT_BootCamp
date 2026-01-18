import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestDeepDiver(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_success(self):
        d = {"patient": {"observations": {"weight": 75.0}}}
        self.assertEqual(starter_code.extract_weight(d), 75.0)

    def test_key_error(self):
        d = {"patient": {}}
        self.assertEqual(starter_code.extract_weight(d), "DATA_MISSING")

    def test_value_error(self):
        d = {"patient": {"observations": {"weight": "INVALID"}}}
        self.assertEqual(starter_code.extract_weight(d), "INVALID_FORMAT")

    def test_type_error(self):
        d = {"patient": {"observations": {"weight": None}}}
        self.assertEqual(starter_code.extract_weight(d), "TECHNICAL_ERROR")

if __name__ == '__main__':
    unittest.main()
