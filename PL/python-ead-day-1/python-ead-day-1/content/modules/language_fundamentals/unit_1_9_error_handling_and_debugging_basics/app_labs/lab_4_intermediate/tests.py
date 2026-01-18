import unittest
import importlib.util
import sys
from io import StringIO

try:
    import starter_code
except ImportError:
    pass

class TestBatchResilience(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_clean_processing(self):
        res = starter_code.clean_signals(["1", "2"])
        self.assertEqual(res, [1, 2])

    def test_mixed_processing(self):
        res = starter_code.clean_signals(["10", "ERR", "20"])
        self.assertEqual(res, [10, 20])

    def test_skipping_log(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        starter_code.clean_signals(["FAIL"])
        sys.stdout = sys.__stdout__
        self.assertIn("Skipping corrupt signal: FAIL", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
