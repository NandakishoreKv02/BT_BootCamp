"""Lab 3: Tests"""
import unittest
from starter_code import PatientHealthMetrics

class TestComputedProperties(unittest.TestCase):
    def setUp(self):
        self.patient = PatientHealthMetrics("P001", 37.0, 70, 120, 80, 1.75, 70)
    
    def test_bmi_calculation(self):
        self.assertAlmostEqual(self.patient.bmi, 22.86, places=2)
    
    def test_bmi_read_only(self):
        with self.assertRaises(AttributeError):
            self.patient.bmi = 25.0
    
    def test_risk_level_normal(self):
        self.assertEqual(self.patient.risk_level, "NORMAL")
    
    def test_risk_level_critical(self):
        self.patient.temperature = 40.0
        self.assertEqual(self.patient.risk_level, "CRITICAL")
    
    def test_status_stable(self):
        self.assertEqual(self.patient.status, "Stable")
    
    def test_is_critical_false(self):
        self.assertFalse(self.patient.is_critical)
    
    def test_is_critical_true(self):
        self.patient.heart_rate = 150
        self.assertTrue(self.patient.is_critical)

if __name__ == "__main__":
    unittest.main()
