import unittest
import importlib.util
import sys
import os

try:
    import starter_code
except ImportError:
    pass

class TestLogAppend(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
        self.fname = "test_audit.txt"

    def tearDown(self):
        if os.path.exists(self.fname):
            os.remove(self.fname)

    def test_append_writes(self):
        starter_code.log_access(self.fname, "U1", "P1")
        starter_code.log_access(self.fname, "U2", "P2")
        
        with open(self.fname, "r") as f:
            lines = f.readlines()
        
        self.assertEqual(len(lines), 2)
        self.assertIn("U1 accessed P1", lines[0])
        self.assertIn("U2 accessed P2", lines[1])

if __name__ == '__main__':
    unittest.main()
