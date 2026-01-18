import unittest
import starter_code

class TestBedStateMachines(unittest.TestCase):
    def test_full_cycle(self):
        rx = starter_code.Prescription("Med", "10mg")
        self.assertTrue(rx.fill())
        self.assertEqual(rx.status, "FILLED")
        self.assertTrue(rx.dispense())
        self.assertEqual(rx.status, "DISPENSED")

    def test_invalid_transitions(self):
        rx = starter_code.Prescription("Med", "10mg")
        # Cannot dispense if pending
        self.assertFalse(rx.dispense())
        
        rx.fill()
        rx.dispense()
        # Cannot cancel if already dispensed
        self.assertFalse(rx.cancel())

if __name__ == "__main__":
    unittest.main()
