import unittest
import starter_code

class TestRefactoring(unittest.TestCase):
    def test_modular_architecture(self):
        platform = starter_code.EHRPlatform()
        
        # Verify decomposition
        self.assertTrue(hasattr(platform, "registry"))
        self.assertTrue(hasattr(platform, "notebook"))
        self.assertTrue(hasattr(platform, "billing"))
        
        # Verify functionality
        platform.process_new_patient("Alice", "MRN-1", "Vitals OK", 100.0)
        
        self.assertIn("MRN-1", platform.registry.patients)
        self.assertIn("MRN-1", platform.notebook.entries)
        self.assertEqual(platform.billing.fees["MRN-1"], 100.0)

if __name__ == "__main__":
    unittest.main()
