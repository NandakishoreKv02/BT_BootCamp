import unittest
import starter_code

class TestBedCollections(unittest.TestCase):
    def test_ward_population(self):
        w = starter_code.Ward("ICU")
        d1 = starter_code.Doctor("A", "X")
        d2 = starter_code.Doctor("B", "X")
        
        w.assign_doctor(d1)
        w.assign_doctor(d2)
        
        self.assertEqual(len(w.doctors), 2)
        self.assertIn(d1, w.doctors)

    def test_doctor_data(self):
        d = starter_code.Doctor("Smith", "Surg")
        self.assertEqual(d.name, "Smith")

if __name__ == "__main__":
    unittest.main()
