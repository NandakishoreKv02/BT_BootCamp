import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestPatientProfile(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_record_structure(self):
        res = starter_code.create_patient_record("Jane", "Smith", 30, "London")
        self.assertEqual(res["full_name"], "SMITH, JANE")
        self.assertEqual(res["age_years"], 30)
        self.assertEqual(res["location"], "London")

    def test_default_city(self):
        res = starter_code.create_patient_record("a", "b", 1)
        self.assertEqual(res["location"], "Unknown")

    def test_docstring_exists(self):
        self.assertIsNotNone(starter_code.create_patient_record.__doc__)

if __name__ == '__main__':
    unittest.main()
