import unittest
from starter_code import Patient

class TestVitalsUpdate(unittest.TestCase):
    def test_temp_validation(self):
        p = Patient("Test")
        self.assertTrue(p.update_temperature(37.0))
        self.assertEqual(p.temperature, 37.0)
        self.assertFalse(p.update_temperature(100.0))
        self.assertEqual(p.temperature, 37.0) # Unchanged

    def test_hr_validation(self):
        p = Patient("Test")
        self.assertTrue(p.update_heart_rate(72))
        self.assertEqual(p.heart_rate, 72)
        self.assertFalse(p.update_heart_rate(500))
        self.assertEqual(p.heart_rate, 72)

if __name__ == "__main__":
    unittest.main()
