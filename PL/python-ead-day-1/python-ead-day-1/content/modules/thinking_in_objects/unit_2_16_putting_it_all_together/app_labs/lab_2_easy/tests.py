import unittest
import starter_code

class TestPharmacy(unittest.TestCase):
    def test_stock_flow(self):
        pm = starter_code.PharmacyManager()
        pm.add_stock("Tylenol", 50)
        self.assertTrue(pm.dispense_stock("Tylenol", 20))
        self.assertFalse(pm.dispense_stock("Tylenol", 40)) # Only 30 left
        
    def test_unknown_drug(self):
        pm = starter_code.PharmacyManager()
        self.assertFalse(pm.dispense_stock("MysteryPill", 1))

if __name__ == "__main__":
    unittest.main()
