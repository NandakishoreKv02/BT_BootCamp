import unittest
import starter_code

class TestGodObjectRefactoring(unittest.TestCase):
    def test_separation_of_concerns(self):
        p = starter_code.Patient("John")
        w = starter_code.Ward("ICU")
        b = starter_code.BillingEngine()
        
        self.assertEqual(p.name, "John")
        self.assertEqual(b.calculate(5, 100), 500)
        self.assertIn("101", w.assign_bed(p, 101))

    def test_non_god_nature(self):
        # Patient should NOT have billing methods
        self.assertFalse(hasattr(starter_code.Patient, "calculate"))

if __name__ == "__main__":
    unittest.main()
