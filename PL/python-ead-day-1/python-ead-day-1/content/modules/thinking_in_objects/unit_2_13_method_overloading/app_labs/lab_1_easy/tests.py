import unittest
import starter_code

class TestFlexibleRegistration(unittest.TestCase):
    def test_default_values(self):
        reg = starter_code.PatientRegistrar()
        res = reg.register("Alice")
        self.assertIn("Self-Pay", res)
        self.assertIn("Ward 0", res)
        
    def test_overridden_values(self):
        reg = starter_code.PatientRegistrar()
        res = reg.register("Bob", "Medicare", 101)
        self.assertIn("Medicare", res)
        self.assertIn("Ward 101", res)

if __name__ == "__main__":
    unittest.main()
