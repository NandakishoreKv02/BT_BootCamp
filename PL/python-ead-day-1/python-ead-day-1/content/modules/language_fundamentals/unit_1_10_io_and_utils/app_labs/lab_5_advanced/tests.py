import unittest
import importlib.util
import sys
import os

try:
    import starter_code
except ImportError:
    pass

class TestPatientArchiver(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
        self.mrn = "MRN_TEST"
        self.fname = f"{self.mrn}.txt"

    def tearDown(self):
        if os.path.exists(self.fname):
            os.remove(self.fname)

    def test_file_writing(self):
        starter_code.write_record_to_disk(self.mrn, "John Doe", "Fever")
        
        self.assertTrue(os.path.exists(self.fname))
        
        with open(self.fname, "r") as f:
            lines = f.readlines()
            
        self.assertIn("MRN: MRN_TEST", lines[0])
        self.assertIn("NAME: John Doe", lines[1])
        self.assertIn("DIAGNOSIS: Fever", lines[2])

if __name__ == '__main__':
    unittest.main()
