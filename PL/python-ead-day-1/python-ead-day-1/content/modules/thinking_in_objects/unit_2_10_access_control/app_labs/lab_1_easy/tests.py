import unittest
import starter_code

class TestBasicEncapsulation(unittest.TestCase):
    def test_prefixes(self):
        f = starter_code.PatientFile("Alice", "ID-1", "SSN-1")
        
        # Public
        self.assertEqual(f.name, "Alice")
        # Protected
        self.assertEqual(f._id_num, "ID-1")
        # Private (Mangled)
        with self.assertRaises(AttributeError):
            print(f.__ssn)
        
        self.assertEqual(f._PatientFile__ssn, "SSN-1")

if __name__ == "__main__":
    unittest.main()
