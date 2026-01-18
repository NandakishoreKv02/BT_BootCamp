import unittest
import starter_code
import os

class TestAppointmentScheduler(unittest.TestCase):
    def test_create_schedule(self):
        schedule = starter_code.create_schedule()
        self.assertIsInstance(schedule, dict)

    def test_booking(self):
        schedule = starter_code.create_schedule()
        result = starter_code.book_appointment(schedule, "09:00", "Test Patient")
        self.assertTrue(result)
        self.assertFalse(starter_code.is_slot_available(schedule, "09:00"))

    def test_cancellation(self):
        schedule = starter_code.create_schedule()
        starter_code.book_appointment(schedule, "09:00", "Test")
        starter_code.cancel_appointment(schedule, "09:00")
        self.assertTrue(starter_code.is_slot_available(schedule, "09:00"))

    def test_file_persistence(self):
        schedule = starter_code.create_schedule()
        starter_code.book_appointment(schedule, "09:00", "Test")
        starter_code.save_schedule(schedule, "test_schedule.txt")
        loaded = starter_code.load_schedule("test_schedule.txt")
        self.assertEqual(loaded.get("09:00"), "Test")
        if os.path.exists("test_schedule.txt"):
            os.remove("test_schedule.txt")

if __name__ == '__main__':
    unittest.main()
