import unittest
import starter_code

class TestFactoryMethod(unittest.TestCase):
    def test_string_parsing(self):
        p = starter_code.Patient.from_legacy_string("John | 25 | A-")
        self.assertEqual(p.name, "John")
        self.assertEqual(p.age, "25")
        self.assertEqual(p.blood_type, "A-")
        self.assertTrue(isinstance(p, starter_code.Patient))

if __name__ == "__main__":
    unittest.main()
