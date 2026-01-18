import unittest
from starter_code import Patient

class TestSystem(unittest.TestCase):
    def test_complex_init(self):
        p = Patient("Alice")
        self.assertEqual(p.name, "Alice")
        self.assertIsInstance(p.contacts, list)
        self.assertIsInstance(p.medications, list)
        self.assertIsInstance(p.vitals, dict)
        self.assertEqual(p.vitals["temp"], 0.0)
        self.assertEqual(Patient.facility_code, "GEN-HOSP")

    def test_mutation(self):
        p = Patient("Bob")
        p.medications.append("X")
        self.assertIn("X", p.medications)
        p.vitals["hr"] = 80
        self.assertEqual(p.vitals["hr"], 80)

if __name__ == "__main__":
    unittest.main()
