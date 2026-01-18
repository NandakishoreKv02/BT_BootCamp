import unittest
from starter_code import Patient

class TestInteractivePatient(unittest.TestCase):
    def setUp(self):
        self.patient = Patient("T001", "Test Subject", 25)

    def test_initial_vitals(self):
        """Verify vitals start empty."""
        self.assertEqual(self.patient.vitals, [])

    def test_add_vital(self):
        """Test recording vitals."""
        self.patient.add_vital(70)
        self.patient.add_vital(80)
        self.assertEqual(self.patient.vitals, [70, 80])

    def test_average_hr(self):
        """Test average calculation."""
        # Case: Empty
        self.assertEqual(self.patient.get_average_heart_rate(), 0)
        # Case: With data
        self.patient.add_vital(100)
        self.patient.add_vital(50)
        self.assertEqual(self.patient.get_average_heart_rate(), 75.0)

if __name__ == "__main__":
    unittest.main()
