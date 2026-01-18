import unittest
import starter_code

class TestMultiLevelInheritance(unittest.TestCase):
    def test_chain_execution(self):
        s = starter_code.Surgeon("Gregory", "L7", "Neuro")
        
        # Check hierarchy
        self.assertTrue(isinstance(s, starter_code.Doctor))
        self.assertTrue(isinstance(s, starter_code.StaffMember))
        
        # Check attribute propagation
        self.assertEqual(s.name, "Gregory")
        self.assertEqual(s.license_id, "L7")
        self.assertEqual(s.surgical_specialty, "Neuro")

if __name__ == "__main__":
    unittest.main()
