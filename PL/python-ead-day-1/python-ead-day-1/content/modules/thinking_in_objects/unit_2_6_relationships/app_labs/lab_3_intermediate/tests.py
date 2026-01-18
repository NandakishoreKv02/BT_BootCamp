import unittest
from io import StringIO
import sys
import starter_code

class TestDependency(unittest.TestCase):
    def test_dispense_interaction(self):
        p = starter_code.Patient("Alex")
        rx = starter_code.Prescription("Aspirin")
        disp = starter_code.MedicationDispenser()
        
        # Test if method exists
        self.assertTrue(hasattr(disp, "dispense_to"))
        
        # Capture output to verify it's using the parameters
        captured_output = StringIO()
        sys.stdout = captured_output
        disp.dispense_to(p, rx)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("Alex", output)
        self.assertIn("Aspirin", output)

if __name__ == "__main__":
    unittest.main()
