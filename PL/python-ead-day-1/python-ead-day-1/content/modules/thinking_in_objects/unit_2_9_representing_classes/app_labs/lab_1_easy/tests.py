import unittest
import starter_code

class TestPatientClass(unittest.TestCase):
    def test_initialization(self):
        p = starter_code.Patient("P-99", "Test User")
        self.assertEqual(p.patient_id, "P-99")
        self.assertEqual(p.full_name, "Test User")

    def test_naming_convention(self):
        self.assertEqual(starter_code.Patient.__name__, "Patient")

if __name__ == "__main__":
    unittest.main()
