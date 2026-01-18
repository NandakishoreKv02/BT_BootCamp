import unittest
import starter_code

class TestEnterpriseEcosystem(unittest.TestCase):
    def test_full_hierarchy(self):
        clinic = starter_code.Clinic("C1")
        p = clinic.register_new_patient("John") # Composition
        
        # Test Tier 1 & 2 Composition
        self.assertIn(p, clinic.patients)
        p.add_med("Aspirin")
        self.assertEqual(len(p.meds), 1)
        self.assertEqual(p.meds[0].drug_name, "Aspirin")
        
        # Test Tier 3 Aggregation
        dr = starter_code.Doctor("Smith")
        dr.assign_to_patient(p)
        self.assertIn(p, dr.patients)
        self.assertIn(dr, p.doctors)

if __name__ == "__main__":
    unittest.main()
