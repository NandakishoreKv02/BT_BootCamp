"""Lab 1: Tests - String Representations"""
import unittest
from starter_code import Patient


class TestPatientStringMethods(unittest.TestCase):
    def setUp(self):
        self.patient = Patient("P001", "Alice Smith", "1990-05-15", "O+", "2024-01-10")
    
    def test_str_format(self):
        """Test __str__ returns user-friendly format."""
        self.assertEqual(str(self.patient), "Patient: Alice Smith (ID: P001)")
    
    def test_str_contains_name(self):
        """Test __str__ contains patient name."""
        self.assertIn("Alice Smith", str(self.patient))
    
    def test_repr_format(self):
        """Test __repr__ returns constructor format."""
        expected = "Patient('P001', 'Alice Smith', '1990-05-15', 'O+', '2024-01-10')"
        self.assertEqual(repr(self.patient), expected)
    
    def test_repr_contains_all_fields(self):
        """Test __repr__ contains all constructor arguments."""
        r = repr(self.patient)
        self.assertIn("P001", r)
        self.assertIn("Alice Smith", r)
        self.assertIn("1990-05-15", r)
        self.assertIn("O+", r)
        self.assertIn("2024-01-10", r)
    
    def test_str_and_repr_different(self):
        """Test that __str__ and __repr__ are different."""
        self.assertNotEqual(str(self.patient), repr(self.patient))
    
    def test_multiple_patients(self):
        """Test with different patients."""
        p2 = Patient("P002", "Bob Jones", "1985-03-20", "A-", "2024-02-15")
        self.assertEqual(str(p2), "Patient: Bob Jones (ID: P002)")


if __name__ == "__main__":
    unittest.main()
