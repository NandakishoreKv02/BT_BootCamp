"""Lab 5: Tests"""
import unittest
from datetime import date, timedelta
from starter_code import TreatmentPlan

class TestTreatmentPlan(unittest.TestCase):
    def setUp(self):
        self.today = date.today()
        self.tomorrow = self.today + timedelta(days=1)
        self.next_week = self.today + timedelta(days=7)
        self.plan = TreatmentPlan("Aspirin", self.today, self.next_week, 100)
        
    def test_date_validation(self):
        # Try setting end date before start
        with self.assertRaises(ValueError):
            self.plan.end_date = self.today - timedelta(days=1)
            
        # Try setting start date after end
        with self.assertRaises(ValueError):
            self.plan.start_date = self.next_week + timedelta(days=1)
            
    def test_duration_calculation(self):
        # 7 days from today to next week (inclusive depends on logic, likely 8 days if inclusive: 0..7)
        # 0 to 7 is 8 days inclusive.
        # Solution impl: delta.days + 1
        expected = (self.next_week - self.today).days + 1
        self.assertEqual(self.plan.duration_days, expected)
        
    def test_dosage_validation(self):
        with self.assertRaises(ValueError):
            self.plan.daily_dosage_mg = 2000 # Too high
            
        with self.assertRaises(ValueError):
            self.plan.daily_dosage_mg = -10 # Negative
            
    def test_total_dosage(self):
        # 8 days * 100mg = 800mg
        expected_days = (self.next_week - self.today).days + 1
        self.assertEqual(self.plan.total_course_dosage_mg, expected_days * 100)
        
    def test_is_active(self):
        self.assertTrue(self.plan.is_active)
        
        # Future plan
        future_start = self.today + timedelta(days=30)
        future_end = future_start + timedelta(days=5)
        future_plan = TreatmentPlan("FutureMeds", future_start, future_end, 50)
        self.assertFalse(future_plan.is_active)

if __name__ == "__main__":
    unittest.main()
