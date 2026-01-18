import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestHL7Extractor(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
        self.segment = "PID|1||12345^^^MRN||DOE^JOHN||19800101|M"

    def test_extraction(self):
        res = starter_code.extract_pid_fields(self.segment)
        self.assertEqual(res['name'], "DOE^JOHN")
        self.assertEqual(res['dob'], "19800101")

    def test_validation(self):
        with self.assertRaises(ValueError):
            starter_code.extract_pid_fields("MSH|^~\&|...")

    def test_masking(self):
        masked = starter_code.mask_patient_name(self.segment)
        expected = "PID|1||12345^^^MRN||***||19800101|M"
        self.assertEqual(masked, expected)
        
    def test_immutability(self):
        # Ensure original string is untouched
        original = self.segment
        _ = starter_code.mask_patient_name(original)
        self.assertEqual(original, self.segment)

if __name__ == '__main__':
    unittest.main()
