import unittest
import starter_code

class TestIDGeneration(unittest.TestCase):
    def test_uniqueness(self):
        c1 = starter_code.MedicalCase("A")
        c2 = starter_code.MedicalCase("B")
        self.assertNotEqual(c1.case_id, c2.case_id)
        
    def test_sequential(self):
        c1 = starter_code.MedicalCase("C")
        c2 = starter_code.MedicalCase("D")
        self.assertEqual(c2.case_id, c1.case_id + 1)

if __name__ == "__main__":
    unittest.main()
