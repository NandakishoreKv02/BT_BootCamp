import unittest
import starter_code

class TestStaticUtilities(unittest.TestCase):
    def test_c_to_f(self):
        self.assertAlmostEqual(starter_code.HealthConverter.c_to_f(0), 32.0)
        self.assertAlmostEqual(starter_code.HealthConverter.c_to_f(100), 212.0)
        
    def test_f_to_c(self):
        self.assertAlmostEqual(starter_code.HealthConverter.f_to_c(32), 0.0)
        self.assertAlmostEqual(starter_code.HealthConverter.f_to_c(212), 100.0)

if __name__ == "__main__":
    unittest.main()
