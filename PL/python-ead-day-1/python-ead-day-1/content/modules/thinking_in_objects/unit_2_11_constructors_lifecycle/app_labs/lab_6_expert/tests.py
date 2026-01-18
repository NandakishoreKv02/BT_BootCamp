import unittest
import starter_code

class TestConditionalInitialization(unittest.TestCase):
    def test_manual_success(self):
        p = starter_code.PatientProfile("Bob", "Manual")
        self.assertEqual(p.data_source, "Manual")
        
    def test_ehr_success(self):
        p = starter_code.PatientProfile("Alice", "EHR", 999)
        self.assertEqual(p.ehr_id, 999)
        
    def test_ehr_failure(self):
        with self.assertRaises(ValueError):
            starter_code.PatientProfile("Charlie", "EHR")

if __name__ == "__main__":
    unittest.main()
