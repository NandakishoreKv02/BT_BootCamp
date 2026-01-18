import unittest
import sys
import os

# Add the current directory to sys.path to import starter_code
sys.path.append(os.path.dirname(__file__))

class TestPatientClass(unittest.TestCase):
    def test_class_exists(self):
        try:
            from starter_code import Patient
            self.assertTrue(isinstance(Patient, type))
        except ImportError:
            self.fail("Could not find Patient class in starter_code.py")

    def test_instances_exist(self):
        try:
            from starter_code import Patient, patient1, patient2
            self.assertIsInstance(patient1, Patient)
            self.assertIsInstance(patient2, Patient)
            self.assertIsNot(patient1, patient2)
        except ImportError:
            self.fail("Could not find patient1 or patient2 instances in starter_code.py")

if __name__ == "__main__":
    unittest.main()
