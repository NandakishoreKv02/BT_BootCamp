import unittest
import starter_code

class TestVitalsRefinement(unittest.TestCase):
    def test_vitals_object(self):
        v = starter_code.Vitals(120, 80, 102.0)
        self.assertTrue(v.is_fever())
        self.assertEqual(v.temp, 102.0)

    def test_patient_composition(self):
        p = starter_code.Patient("Alex")
        v = starter_code.Vitals(110, 70, 98.6)
        p.update_vitals(v)
        self.assertEqual(p.vitals.temp, 98.6)

if __name__ == "__main__":
    unittest.main()
