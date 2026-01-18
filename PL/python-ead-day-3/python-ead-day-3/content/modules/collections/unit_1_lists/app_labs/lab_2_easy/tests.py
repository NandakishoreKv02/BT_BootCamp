import unittest

class TestListUpdates(unittest.TestCase):
    def test_updates(self):
        from starter_code import slots, current_patient
        # Initially: ["A", "B"]
        # Insert: ["EMERGENCY", "A", "B"]
        # Remove A: ["EMERGENCY", "B"]
        # Pop(0): EMERGENCY
        self.assertEqual(current_patient, "EMERGENCY")
        self.assertEqual(slots, ["Patient B"])

if __name__ == "__main__":
    unittest.main()
