import unittest
import starter_code

class TestMethodSignatures(unittest.TestCase):
    def test_signature(self):
        rx = starter_code.Prescription("Test")
        label = rx.set_instructions(5, "ml", "Daily")
        self.assertEqual(rx.dose, 5)
        self.assertEqual(rx.unit, "ml")
        self.assertEqual(rx.frequency, "Daily")
        self.assertIn("5ml", label)
        self.assertIn("Daily", label)

    def test_init_state(self):
        rx = starter_code.Prescription("Test")
        self.assertEqual(rx.dose, 0)

if __name__ == "__main__":
    unittest.main()
