import unittest
import starter_code

class TestVitalsInitialization(unittest.TestCase):
    def test_alert_logic_positive(self):
        v = starter_code.VitalsReading("A", 120)
        self.assertTrue(v.critical_alert)
        
    def test_alert_logic_negative(self):
        v = starter_code.VitalsReading("B", 70)
        self.assertFalse(v.critical_alert)

if __name__ == "__main__":
    unittest.main()
