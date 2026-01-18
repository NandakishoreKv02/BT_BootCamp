import unittest
import importlib.util
import sys
from io import StringIO

try:
    import starter_code
except ImportError:
    pass

class TestInsuranceLookup(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_found_id(self):
        self.assertEqual(starter_code.fetch_provider_id({"provider_id": "X"}), "X")

    def test_missing_id_return(self):
        res = starter_code.fetch_provider_id({"name": "Test"})
        self.assertEqual(res, "PENDING_VERIFICATION")

    def test_logging_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        starter_code.fetch_provider_id({"name": "John Doe"})
        sys.stdout = sys.__stdout__
        self.assertIn("LOG: Missing provider ID for patient John Doe", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
