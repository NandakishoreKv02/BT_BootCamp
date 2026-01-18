import unittest
import starter_code

class TestConstructorInheritance(unittest.TestCase):
    def test_super_call(self):
        m = starter_code.MRIScanner("Siemens", 3.0)
        self.assertEqual(m.model_name, "Siemens")
        self.assertEqual(m.tesla_rating, 3.0)

if __name__ == "__main__":
    unittest.main()
