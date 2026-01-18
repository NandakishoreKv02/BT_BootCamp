import unittest
import sys
import os

sys.path.append(os.path.dirname(__file__))

class TestPatientConstructor(unittest.TestCase):
    def test_constructor_attributes(self):
        try:
            from starter_code import Patient
            p = Patient("Alice", 25)
            self.assertEqual(p.name, "Alice")
            self.assertEqual(p.age, 25)
        except ImportError:
            self.fail("Could not find Patient class")
        except AttributeError:
            self.fail("Patient class missing name or age attributes")

    def test_patient1_instance(self):
        try:
            from starter_code import patient1
            self.assertEqual(patient1.name, "John Doe")
            self.assertEqual(patient1.age, 30)
        except (ImportError, AttributeError):
            self.fail("patient1 instance missing or incorrect")

if __name__ == "__main__":
    unittest.main()
