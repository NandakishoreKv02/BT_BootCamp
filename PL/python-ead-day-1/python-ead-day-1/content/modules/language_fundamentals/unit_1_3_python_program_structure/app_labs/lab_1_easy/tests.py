import unittest
import importlib.util
import sys
import os

# Import the student's code
try:
    import starter_code
except ImportError:
    # If looking for solution path or different directory structure
    pass

class TestPatientFormatter(unittest.TestCase):
    def setUp(self):
        # Reload module to ensure fresh state if needed
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_format_patient_id(self):
        """Test if patient ID is formatted correctly with leading zeros."""
        if not hasattr(starter_code, 'format_patient_id'):
            self.fail("Function 'format_patient_id' not found.")
        
        self.assertEqual(starter_code.format_patient_id(42), "PAT-00042")
        self.assertEqual(starter_code.format_patient_id(12345), "PAT-12345")
        self.assertEqual(starter_code.format_patient_id(0), "PAT-00000")

    def test_format_patient_record(self):
        """Test if the full record string is formatted correctly."""
        if not hasattr(starter_code, 'format_patient_record'):
            self.fail("Function 'format_patient_record' not found.")

        expected = "Patient: John Doe (PAT-00042), Age: 35"
        result = starter_code.format_patient_record("John Doe", 42, 35)
        self.assertEqual(result, expected)

    def test_docstrings_exist(self):
        """Check if docstrings are present for all functions."""
        self.assertIsNotNone(starter_code.__doc__, "Module docstring is missing.")
        
        if hasattr(starter_code, 'format_patient_id'):
            self.assertIsNotNone(starter_code.format_patient_id.__doc__, "Docstring for 'format_patient_id' is missing.")
        
        if hasattr(starter_code, 'format_patient_record'):
            self.assertIsNotNone(starter_code.format_patient_record.__doc__, "Docstring for 'format_patient_record' is missing.")

if __name__ == '__main__':
    unittest.main()
