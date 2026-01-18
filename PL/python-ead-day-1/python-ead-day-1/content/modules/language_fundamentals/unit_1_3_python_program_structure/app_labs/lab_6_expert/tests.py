import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

SINGLE_MSG = "MSH|^~\&|HIS|... \nPID|1||12345^^^MRN||DOE^JOHN"
MULTIPLE_OBX_MSG = "MSH|... \nOBX|1|NM|GLU||100\nOBX|2|NM|HGB||14"

class TestHL7Parser(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
    
    def test_parse_segment(self):
        """Test splitting logic."""
        seg = "PID|1||DOE^JOHN"
        # We assume starter_code usually splits by '|'
        # Adjust expectation based on likely implementation or requirement
        if hasattr(starter_code, 'parse_segment'):
            res = starter_code.parse_segment(seg)
            self.assertIn("PID", res)
            self.assertIn("DOE^JOHN", res)

    def test_extract_name(self):
        """Test name extraction."""
        # Mock parsed data structure roughly expected
        # PID field 5 is Name. (Index 5 if PID index is 0)
        # Usually: PID|Seq|ID|ID_List|AltID|Name
        # Indices: 0   1   2   3       4     5
        
        # NOTE: HL7 is 1-based usually, but array is 0-based. 
        # PID|1 means "PID" is index 0. "1" is index 1.
        # "DOE^JOHN" would be index 5.
        
        parsed = {
            "PID": ["PID", "1", "", "", "", "DOE^JOHN"]
        }
        name = starter_code.extract_patient_name(parsed)
        self.assertEqual(name['family'], "DOE")
        self.assertEqual(name['given'], "JOHN")

    def test_docstrings(self):
        """Expert lab requires docstrings."""
        self.assertIsNotNone(starter_code.parse_message.__doc__)

if __name__ == '__main__':
    unittest.main()
