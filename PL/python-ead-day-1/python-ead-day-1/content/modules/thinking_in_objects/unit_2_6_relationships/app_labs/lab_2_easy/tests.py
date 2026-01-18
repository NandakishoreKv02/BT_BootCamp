import unittest
import starter_code

class TestComposition(unittest.TestCase):
    def test_kit_composition(self):
        kit = starter_code.SurgicalKit("KIT-01")
        # Verify component exists
        self.assertTrue(hasattr(kit, "scalpel"))
        self.assertEqual(kit.scalpel.sharpness, 100)
    
    def test_sharpness_check(self):
        # Verify we can access it
        kit = starter_code.SurgicalKit("X")
        self.assertEqual(kit.scalpel.sharpness, 100)

if __name__ == "__main__":
    unittest.main()
