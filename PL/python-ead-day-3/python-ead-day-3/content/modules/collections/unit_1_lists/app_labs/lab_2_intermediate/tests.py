import unittest
from starter_code import cancel_appointment, organize_schedule, get_morning_appointments, find_patient_slot

class TestScheduleOrganizer(unittest.TestCase):
    
    def test_cancel(self):
        data = ["10:00 - A", "11:00 - B"]
        # Success
        self.assertTrue(cancel_appointment(data, "10:00 - A"))
        self.assertEqual(data, ["11:00 - B"])
        # Fail
        self.assertFalse(cancel_appointment(data, "99:99 - Missing"))
        
    def test_organize(self):
        data = ["12:00 - B", "09:00 - A", "10:00 - C"]
        res = organize_schedule(data)
        self.assertEqual(data, ["09:00 - A", "10:00 - C", "12:00 - B"])
        self.assertEqual(res, data, "Should return the list too")
        
    def test_morning(self):
        data = ["09:00 - A", "11:59 - B", "12:00 - C", "14:00 - D"]
        morning = get_morning_appointments(data)
        self.assertEqual(morning, ["09:00 - A", "11:59 - B"])
        self.assertNotIn("12:00 - C", morning)
        
    def test_find(self):
        data = ["09:00 - John Doe", "10:00 - Jane Smith"]
        self.assertEqual(find_patient_slot(data, "Doe"), "09:00 - John Doe")
        self.assertEqual(find_patient_slot(data, "Jane"), "10:00 - Jane Smith")
        self.assertIsNone(find_patient_slot(data, "Zorg"))

if __name__ == '__main__':
    unittest.main()
