import unittest
from starter_code import Patient

class TestWardManager(unittest.TestCase):
    def setUp(self):
        # Reset class variable before each test
        Patient.total_patients = 0

    def test_census_tracking(self):
        """Test class variable increments and decrements."""
        self.assertEqual(Patient.get_census(), 0)
        p1 = Patient("A", 10, 10)
        p2 = Patient("B", 20, 20)
        self.assertEqual(Patient.get_census(), 2)
        p1.discharge()
        self.assertEqual(Patient.get_census(), 1)

    def test_prescription(self):
        """Test returns and state changes."""
        p = Patient("James", 40, 80)
        msg = p.prescribe_medication("Statins", 50)
        self.assertIn("Statins", msg)
        self.assertEqual(len(p.records), 1)
        self.assertEqual(p.records[0]["med"], "Statins")

    def test_static_integration(self):
        """Test static method usage across instances."""
        p = Patient("Elderly", 80, 70)
        # (80 * 0.5) + (70 * 0.2) = 40 + 14 = 54
        self.assertEqual(p.get_priority(), 54.0)

    def test_safe_discharge(self):
        """Test boolean return and boundary safety."""
        p = Patient("Short Stay", 20, 70)
        self.assertTrue(p.discharge())
        self.assertFalse(p.discharge()) # Already inactive
        self.assertEqual(Patient.get_census(), 0)

if __name__ == "__main__":
    unittest.main()
