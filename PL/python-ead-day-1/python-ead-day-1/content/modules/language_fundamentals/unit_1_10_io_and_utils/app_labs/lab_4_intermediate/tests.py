import unittest
import importlib.util
import sys
import os

try:
    import starter_code
except ImportError:
    pass

class TestProtocolLoader(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
        self.fname = "temp_protocol.txt"
        with open(self.fname, "w") as f:
            f.write("Line 1\nLine 2 \n Line 3\n")

    def tearDown(self):
        if os.path.exists(self.fname):
            os.remove(self.fname)

    def test_load_and_strip(self):
        res = starter_code.load_protocol(self.fname)
        self.assertEqual(res, ["Line 1", "Line 2", "Line 3"])

    def test_missing_file_returns_empty(self):
        res = starter_code.load_protocol("completely_missing.txt")
        self.assertEqual(res, [])

if __name__ == '__main__':
    unittest.main()
