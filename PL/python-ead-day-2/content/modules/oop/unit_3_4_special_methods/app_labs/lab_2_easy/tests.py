"""Lab 2: Tests - Patient Registry"""
import unittest
from starter_code import Patient, PatientRegistry


class TestPatientRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = PatientRegistry()
        self.p1 = Patient("P001", "Alice")
        self.p2 = Patient("P002", "Bob")
        self.registry.register(self.p1)
        self.registry.register(self.p2)
    
    def test_len_returns_count(self):
        self.assertEqual(len(self.registry), 2)
    
    def test_len_empty(self):
        empty = PatientRegistry()
        self.assertEqual(len(empty), 0)
    
    def test_getitem_returns_patient(self):
        self.assertEqual(self.registry["P001"], self.p1)
    
    def test_getitem_raises_keyerror(self):
        with self.assertRaises(KeyError):
            _ = self.registry["P999"]
    
    def test_contains_true(self):
        self.assertTrue("P001" in self.registry)
    
    def test_contains_false(self):
        self.assertFalse("P999" in self.registry)


if __name__ == "__main__":
    unittest.main()
