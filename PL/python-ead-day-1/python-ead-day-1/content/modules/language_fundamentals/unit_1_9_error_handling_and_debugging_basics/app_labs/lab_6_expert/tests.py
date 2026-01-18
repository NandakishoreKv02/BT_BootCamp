import unittest
import importlib.util
import sys
from io import StringIO

try:
    import starter_code
except ImportError:
    pass

class TestDosageAuditor(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_complete_flow_success(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        res = starter_code.calculate_concentration(10, 2)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertEqual(res, 5.0)
        self.assertIn("AUDIT: Calculation Successful", output)
        self.assertIn("AUDIT: Transaction Completed", output)

    def test_complete_flow_failure(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        res = starter_code.calculate_concentration(10, 0)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertEqual(res, 0.0)
        self.assertIn("AUDIT: Calculation Failed", output)
        self.assertIn("AUDIT: Transaction Completed", output)

if __name__ == '__main__':
    unittest.main()
