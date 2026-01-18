import unittest
import sys
import os

sys.path.append(os.path.dirname(__file__))

class TestClassVariables(unittest.TestCase):
    def test_counter_logic(self):
        try:
            from starter_code import Patient
            initial_count = Patient.total_patients
            p = Patient("Test")
            self.assertEqual(Patient.total_patients, initial_count + 1)
        except ImportError:
            self.fail("Could not find Patient class")

    def test_shared_state(self):
        from starter_code import Patient
        p1 = Patient("One")
        p2 = Patient("Two")
        self.assertEqual(p1.total_patients, p2.total_patients)
        self.assertEqual(p1.total_patients, Patient.total_patients)

if __name__ == "__main__":
    unittest.main()
