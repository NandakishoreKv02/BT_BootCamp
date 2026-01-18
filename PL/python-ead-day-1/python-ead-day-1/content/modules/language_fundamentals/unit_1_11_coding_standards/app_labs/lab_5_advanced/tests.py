import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestSRPRefactor(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_clean_data(self):
        self.assertEqual(starter_code.clean_data(["10", "A", "20"]), [10.0, 20.0])

    def test_analyze_risk(self):
        self.assertEqual(starter_code.analyze_risk([150.0]), "HIGH")
        self.assertEqual(starter_code.analyze_risk([100.0]), "NORMAL")

    def test_full_pipeline(self):
        res = starter_code.process_labs(["155", "100"])
        self.assertIn("HIGH", res)
        self.assertIn("SYSTEM REPORT", res)

if __name__ == '__main__':
    unittest.main()
