import unittest
from starter_code import Patient

class TestClinicAdmission(unittest.TestCase):
    def test_initial_state(self):
        p = Patient("Test")
        self.assertEqual(p.name, "Test")
        self.assertFalse(p.is_active)

    def test_admit(self):
        p = Patient("Test")
        msg = p.admit()
        self.assertTrue(p.is_active)
        self.assertIn("Test", msg)

    def test_discharge(self):
        p = Patient("Test")
        p.admit()
        msg = p.discharge()
        self.assertFalse(p.is_active)
        self.assertIn("Test", msg)

if __name__ == "__main__":
    unittest.main()
