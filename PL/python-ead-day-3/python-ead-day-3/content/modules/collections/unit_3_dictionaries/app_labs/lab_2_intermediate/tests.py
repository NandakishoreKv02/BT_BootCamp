import unittest
from starter_code import register_doctor, add_availability, book_appointment, find_doctors_by_specialty, get_doctor_workload

class TestDoctorSchedule(unittest.TestCase):
    
    def setUp(self):
        """Start with a fresh DB for each test."""
        self.db = {}

    def test_task_1_register(self):
        """Test doctor registration and structure."""
        register_doctor(self.db, 101, "Dr. Test", "General")
        self.assertIn(101, self.db)
        self.assertEqual(self.db[101]["name"], "Dr. Test")
        self.assertEqual(self.db[101]["specialty"], "General")
        self.assertEqual(self.db[101]["schedule"], {}, "Schedule should init empty")

    def test_task_2_availability(self):
        """Test adding availability slots."""
        register_doctor(self.db, 101, "Dr. Test", "General")
        result = add_availability(self.db, 101, "2023-01-01")
        
        self.assertTrue(result)
        schedule = self.db[101]["schedule"]
        self.assertIn("2023-01-01", schedule)
        self.assertIn("09:00", schedule["2023-01-01"])
        self.assertIsNone(schedule["2023-01-01"]["09:00"])
        
        # Test missing doc
        res_missing = add_availability(self.db, 999, "2023-01-01")
        self.assertFalse(res_missing)

    def test_task_3_booking(self):
        """Test booking logic."""
        register_doctor(self.db, 101, "Dr. Test", "General")
        add_availability(self.db, 101, "2023-01-01")
        
        # Success
        success = book_appointment(self.db, 101, "2023-01-01", "09:00", 555)
        self.assertTrue(success, "Booking should succeed")
        self.assertEqual(self.db[101]["schedule"]["2023-01-01"]["09:00"], 555)
        
        # Fail: Already taken
        fail = book_appointment(self.db, 101, "2023-01-01", "09:00", 666)
        self.assertFalse(fail, "Booking taken slot should fail")
        self.assertEqual(self.db[101]["schedule"]["2023-01-01"]["09:00"], 555, "Should not overwrite")
        
        # Fail: Invalid time
        fail_time = book_appointment(self.db, 101, "2023-01-01", "23:00", 777)
        self.assertFalse(fail_time)

    def test_task_4_find_specialty(self):
        """Test finding doctors."""
        register_doctor(self.db, 1, "Doc A", "Cardio")
        register_doctor(self.db, 2, "Doc B", "Neuro")
        register_doctor(self.db, 3, "Doc C", "Cardio")
        
        results = find_doctors_by_specialty(self.db, "Cardio")
        self.assertEqual(len(results), 2)
        self.assertIn("Doc A", results)
        self.assertIn("Doc C", results)
        self.assertNotIn("Doc B", results)

    def test_task_5_workload(self):
        """Test workload aggregation."""
        register_doctor(self.db, 1, "Doc A", "Cardio")
        add_availability(self.db, 1, "Day1")
        add_availability(self.db, 1, "Day2")
        
        # Book 2 on Day 1
        book_appointment(self.db, 1, "Day1", "09:00", 100)
        book_appointment(self.db, 1, "Day1", "10:00", 101)
        # Book 1 on Day 2
        book_appointment(self.db, 1, "Day2", "14:00", 102)
        
        count = get_doctor_workload(self.db, 1)
        self.assertEqual(count, 3)
        
        # Empty doc
        register_doctor(self.db, 2, "Doc B", "Neuro")
        self.assertEqual(get_doctor_workload(self.db, 2), 0)

if __name__ == '__main__':
    unittest.main()
