import unittest
import starter_code

class TestTriageInitialization(unittest.TestCase):
    def test_parameter_mapping(self):
        rec = starter_code.TriageRecord("John", "Cough")
        self.assertEqual(rec.patient_name, "John")
        self.assertEqual(rec.symptom, "Cough")

if __name__ == "__main__":
    unittest.main()
