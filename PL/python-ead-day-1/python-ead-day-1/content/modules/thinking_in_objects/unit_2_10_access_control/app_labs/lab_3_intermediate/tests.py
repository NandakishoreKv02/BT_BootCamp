import unittest
import starter_code

class TestDosageSetter(unittest.TestCase):
    def test_valid_update(self):
        req = starter_code.MedicationRequest(50)
        req.dose = 150
        self.assertEqual(req.dose, 150)
        
    def test_invalid_update_blocked(self):
        req = starter_code.MedicationRequest(50)
        req.dose = 999 
        self.assertEqual(req.dose, 50, "Setter failed to block illegal value")

if __name__ == "__main__":
    unittest.main()
