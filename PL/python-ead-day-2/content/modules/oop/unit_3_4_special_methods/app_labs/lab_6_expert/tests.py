"""Lab 6: Tests - Complete Patient Manager"""
import unittest
from starter_code import Patient, PatientManager


class TestPatientManager(unittest.TestCase):
    def setUp(self):
        self.manager = PatientManager()
        self.p1 = Patient("P001", "Alice", 30)
        self.p2 = Patient("P002", "Bob", 40)
        self.p3 = Patient("P003", "Charlie", 30)
    
    def test_collection_protocol(self):
        # Set
        self.manager["P001"] = self.p1
        self.manager["P002"] = self.p2
        
        # Len
        self.assertEqual(len(self.manager), 2)
        
        # Get
        self.assertEqual(self.manager["P001"], self.p1)
        
        # Contains
        self.assertTrue("P001" in self.manager)
        
        # Del
        del self.manager["P001"]
        self.assertEqual(len(self.manager), 1)
        self.assertFalse("P001" in self.manager)
    
    def test_validation_errors(self):
        with self.assertRaises(TypeError):
            self.manager["P001"] = "Not a Patient"
            
        with self.assertRaises(ValueError):
            # Key mismatch
            self.manager["WRONG_ID"] = self.p1
    
    def test_iteration_order(self):
        self.manager["P003"] = self.p3
        self.manager["P002"] = self.p2
        self.manager["P001"] = self.p1
        
        # Should iterate in name order: Alice, Bob, Charlie
        names = [p.name for p in self.manager]
        self.assertEqual(names, ["Alice", "Bob", "Charlie"])
    
    def test_filtering_call(self):
        self.manager["P001"] = self.p1
        self.manager["P002"] = self.p2
        self.manager["P003"] = self.p3
        
        # Filter by age=30 (Alice and Charlie)
        filtered = self.manager(age=30)
        self.assertEqual(len(filtered), 2)
        self.assertTrue("P001" in filtered)
        self.assertTrue("P003" in filtered)
    
    def test_audit_log(self):
        self.manager["P001"] = self.p1
        logs = self.manager._audit_log
        self.assertEqual(len(logs), 1)
        self.assertIn("CREATE", logs[0])


if __name__ == "__main__":
    unittest.main()
