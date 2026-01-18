import unittest
import starter_code

class TestPharmacySentinel(unittest.TestCase):
    def test_list_independence(self):
        o1 = starter_code.PharmacyOrder()
        o2 = starter_code.PharmacyOrder()
        
        # Verify both have distinct lists
        self.assertIsNot(o1.medications, o2.medications, "Orders are sharing the same list! Use None sentinel.")
        
        if hasattr(o1, "add_drug"):
            o1.add_drug("Test")
            self.assertEqual(len(o1.medications), 1)
            self.assertEqual(len(o2.medications), 0)

if __name__ == "__main__":
    unittest.main()
