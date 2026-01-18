import unittest
import starter_code

class TestStaffModelling(unittest.TestCase):
    def test_hierarchy(self):
        dr = starter_code.Physician("Strange", "A-123", "Surgery")
        
        # Test Inheritance
        self.assertTrue(isinstance(dr, starter_code.HospitalStaff))
        self.assertEqual(dr.role, "Physician")
        
        # Test Composition
        self.assertTrue(hasattr(dr, "id_card"))
        self.assertEqual(dr.id_card.card_number, "A-123")

if __name__ == "__main__":
    unittest.main()
