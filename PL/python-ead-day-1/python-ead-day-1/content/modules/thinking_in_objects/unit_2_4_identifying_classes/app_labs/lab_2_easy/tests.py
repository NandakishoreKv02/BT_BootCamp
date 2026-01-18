import unittest
import starter_code

class TestPharmacyBCE(unittest.TestCase):
    def test_bce_existence(self):
        p = starter_code.Prescription("Med", 10)
        c = starter_code.DispensingLogic()
        b = starter_code.PharmacyUI()
        
        self.assertTrue(c.verify(p))
        self.assertEqual(p.drug, "Med")

    def test_logic_validation(self):
        c = starter_code.DispensingLogic()
        p_invalid = starter_code.Prescription("Med", 0)
        self.assertFalse(c.verify(p_invalid))

if __name__ == "__main__":
    unittest.main()
