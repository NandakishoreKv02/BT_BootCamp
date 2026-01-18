import unittest
from starter_code import Patient

class TestWorkflow(unittest.TestCase):
    def test_prescribe(self):
        p = Patient("Alice")
        self.assertTrue(p.prescribe("Advil"))
        self.assertIn("Advil", p.active_meds)
        self.assertFalse(p.prescribe("Advil")) # Duplicate
        self.assertEqual(len(p.active_meds), 1)

    def test_status_empty(self):
        p = Patient("Bob")
        self.assertEqual(p.get_status(), "Bob currently taking no medications.")

    def test_status_full(self):
        p = Patient("Sara")
        p.prescribe("Drug A")
        p.prescribe("Drug B")
        self.assertIn("Drug A, Drug B", p.get_status())

if __name__ == "__main__":
    unittest.main()
