import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestReportFormatter(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_standard_row(self):
        res = starter_code.generate_report_row("ABC", 5, "TESTING")
        # "ABC       |     5 |      TESTING"
        self.assertTrue(res.startswith("ABC "))
        self.assertIn("    5 |", res)
        self.assertTrue(res.endswith("TESTING"))

    def test_alignment_lengths(self):
        res = starter_code.generate_report_row("ID", 0, "S")
        self.assertEqual(len(res), 10 + 3 + 5 + 3 + 12)

if __name__ == '__main__':
    unittest.main()
