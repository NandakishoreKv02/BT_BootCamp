import unittest
import starter_code

class TestEcosystem(unittest.TestCase):
    def test_inheritance(self):
        dr = starter_code.Physician("House", "MD")
        self.assertTrue(isinstance(dr, starter_code.Staff))

    def test_composition(self):
        h = starter_code.Hospital()
        self.assertEqual(len(h.wards), 2)
        self.assertEqual(h.wards[0].name, "ICU")

    def test_aggregation(self):
        nurse = starter_code.Staff("Nightingale", "Nurse")
        ward = starter_code.Ward("ER")
        ward.assign_nurse(nurse)
        self.assertEqual(ward.nurse, nurse)

    def test_dependency(self):
        dr = starter_code.Physician("House", "MD")
        analyzer = starter_code.Analyzer("Alpha")
        # Check if method exists and handles dependency
        self.assertTrue(hasattr(dr, "perform_analysis"))

if __name__ == "__main__":
    unittest.main()
