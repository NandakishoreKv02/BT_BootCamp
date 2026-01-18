"""Lab 4: Tests"""
import unittest
from starter_code import PatientRecord

class TestAccessControl(unittest.TestCase):
    def setUp(self):
        self.record = PatientRecord("John Doe", "Male", "123456789", "INS123")
        
    def test_public_access(self):
        self.assertEqual(self.record.name, "John Doe")
        self.record.name = "Jane Doe"
        self.assertEqual(self.record.name, "Jane Doe")
        
    def test_protected_access(self):
        self.record.add_condition("Flu")
        self.assertIn("Flu", self.record.conditions)
        # Verify conditions property returns a copy
        conds = self.record.conditions
        conds.append("Broken Leg")
        self.assertNotIn("Broken Leg", self.record.conditions)
        
    def test_private_access(self):
        # Direct access should fail
        with self.assertRaises(AttributeError):
            _ = self.record.__ssn
            
        # Name mangling access should work (though strongly discouraged in practice)
        self.assertEqual(self.record._PatientRecord__ssn, "123456789")
        
    def test_masked_properties(self):
        self.assertEqual(self.record.ssn_last_4, "***-**-6789")
        
    def test_internal_debug(self):
        # The internal method can read the private attribute
        result = self.record._internal_debug()
        self.assertIn("123456789", str(result) if result else "")

if __name__ == "__main__":
    unittest.main()
