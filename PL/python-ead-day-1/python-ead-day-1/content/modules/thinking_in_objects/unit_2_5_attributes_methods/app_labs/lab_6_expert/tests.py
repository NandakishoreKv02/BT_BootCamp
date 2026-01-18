import unittest
import starter_code

class TestClinicalAggregation(unittest.TestCase):
    def test_aggregation_math(self):
        # Reset counters
        starter_code.PatientMetric.all_hr_sum = 0
        starter_code.PatientMetric.total_patients = 0
        
        p1 = starter_code.PatientMetric("A")
        p2 = starter_code.PatientMetric("B")
        
        p1.record_heart_rate(100)
        p2.record_heart_rate(60)
        
        self.assertEqual(starter_code.PatientMetric.get_average_bpm(), 80.0)

    def test_zero_division_protection(self):
        starter_code.PatientMetric.total_patients = 0
        self.assertEqual(starter_code.PatientMetric.get_average_bpm(), 0)

if __name__ == "__main__":
    unittest.main()
