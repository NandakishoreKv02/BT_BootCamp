import unittest
import starter_code

class TestBedManager(unittest.TestCase):
    def test_make_ward(self):
        w = starter_code.make_ward("ICU", 10)
        self.assertEqual(w['name'], "ICU")
        self.assertEqual(w['total'], 10)
        self.assertEqual(w['occupied'], 0)

    def test_independence(self):
        w1 = starter_code.make_ward("A", 10)
        w2 = starter_code.make_ward("B", 10)
        
        starter_code.admit_patient(w1)
        
        self.assertEqual(w1['occupied'], 1)
        self.assertEqual(w2['occupied'], 0) # w2 should stay 0

    def test_limits(self):
        w = starter_code.make_ward("Tiny", 1)
        starter_code.admit_patient(w)
        starter_code.admit_patient(w) # Should fail gracefully
        self.assertEqual(w['occupied'], 1)

        starter_code.discharge_patient(w)
        starter_code.discharge_patient(w) # Should fail gracefully
        self.assertEqual(w['occupied'], 0)

if __name__ == "__main__":
    unittest.main()
