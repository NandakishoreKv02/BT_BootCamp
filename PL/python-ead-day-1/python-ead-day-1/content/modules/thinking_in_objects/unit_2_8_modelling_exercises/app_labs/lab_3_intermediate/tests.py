import unittest
import starter_code

class TestScheduleModelling(unittest.TestCase):
    def test_composition_and_booking(self):
        times = ["9am", "10am"]
        sched = starter_code.DailySchedule("2025-01-01", times)
        
        # Test Composition
        self.assertEqual(len(sched.slots), 2)
        self.assertEqual(sched.slots[0].time_str, "9am")
        
        # Test Booking (Aggregation)
        p = starter_code.Patient("Alice")
        dr = starter_code.Physician("Smith")
        sched.schedule_appointment(0, p, dr)
        
        self.assertIs(sched.slots[0].booked_to, p)
        self.assertIs(sched.slots[0].assigned_dr, dr)

if __name__ == "__main__":
    unittest.main()
