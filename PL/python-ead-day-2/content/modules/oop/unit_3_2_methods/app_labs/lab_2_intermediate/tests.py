import unittest
from starter_code import Patient

class TestPatientFactories(unittest.TestCase):
    def test_from_string(self):
        """Test parsing legacy string."""
        p = Patient.from_string("Michael:62:Hypertension")
        self.assertEqual(p.name, "Michael")
        self.assertEqual(p.age, 62)
        self.assertEqual(p.condition, "Hypertension")

    def test_from_dict(self):
        """Test parsing dictionary data."""
        data = {"name": "Emma", "age": 4, "condition": "Rash"}
        p = Patient.from_dict(data)
        self.assertEqual(p.name, "Emma")
        self.assertEqual(p.age, 4)
        self.assertEqual(p.condition, "Rash")

    def test_init(self):
        """Test standard constructor."""
        p = Patient("Test", 10, "None")
        self.assertEqual(p.name, "Test")

if __name__ == "__main__":
    unittest.main()
