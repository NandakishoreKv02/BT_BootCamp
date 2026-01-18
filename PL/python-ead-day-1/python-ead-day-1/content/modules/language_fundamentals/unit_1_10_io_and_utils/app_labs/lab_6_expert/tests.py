import unittest
import importlib.util
import sys
import os
from io import StringIO

try:
    import starter_code
except ImportError:
    pass

class TestIngestionEngine(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)
        self.fname = "test_vitals.txt"
        with open(self.fname, "w") as f:
            f.write("0800|P01|70\n0900|P02|130\n")

    def tearDown(self):
        if os.path.exists(self.fname):
            os.remove(self.fname)

    def test_average_calculation(self):
        res = starter_code.generate_vitals_summary(self.fname)
        # (70 + 130) / 2 = 100.0
        self.assertEqual(res, 100.0)

    def test_formatted_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        starter_code.generate_vitals_summary(self.fname)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("0800", output)
        self.assertIn("P01", output)
        self.assertIn("70", output)

    def test_empty_file_handling(self):
        empty_fname = "empty.txt"
        with open(empty_fname, "w") as f: pass
        res = starter_code.generate_vitals_summary(empty_fname)
        self.assertEqual(res, 0.0)
        os.remove(empty_fname)

if __name__ == '__main__':
    unittest.main()
