import unittest
import starter_code

class TestPatientEntity(unittest.TestCase):
    def test_class_structure(self):
        p = starter_code.Patient("Test", 20, "MRN0")
        self.assertEqual(p.name, "Test")
        self.assertEqual(p.age, 20)
        self.assertEqual(p.mrn, "MRN0")

    def test_instantiation(self):
        p1 = starter_code.Patient("A", 1, "1")
        p2 = starter_code.Patient("B", 2, "2")
        self.assertNotEqual(p1, p2)

if __name__ == "__main__":
    unittest.main()
