import unittest
from starter_code import process_order, dispense_medication, DrugInteractionError

class TestLab4(unittest.TestCase):
    def test_type_error(self):
        res = process_order("Statin", "5")
        self.assertEqual(res, "System Error: Bad Input")

    def test_interaction_error(self):
        res = process_order("Incompatible", 5)
        self.assertEqual(res, "Medical Alert: Safety Violation")

    def test_success(self):
        res = process_order("Statin", 5)
        self.assertEqual(res, "Dispensed")

if __name__ == "__main__":
    unittest.main()
