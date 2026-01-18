import unittest
import importlib.util
import sys
from io import StringIO

try:
    import starter_code
except ImportError:
    pass

class TestWeightGuard(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_valid_input(self):
        self.assertEqual(starter_code.parse_weight("75.5"), 75.5)

    def test_invalid_input_return(self):
        self.assertEqual(starter_code.parse_weight("abc"), 0.0)

    def test_error_message(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        starter_code.parse_weight("WRONG")
        sys.stdout = sys.__stdout__
        self.assertIn("Invalid weight input: WRONG", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
