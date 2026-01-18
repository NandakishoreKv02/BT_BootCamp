import unittest
from starter_code import Schedule, Doctor, Surgeon

class TestLab6(unittest.TestCase):
    def test_schedule_logic(self):
        s = Schedule(9, 17)
        self.assertTrue(s.is_available(10))
        self.assertFalse(s.is_available(18))

    def test_doctor_delegation(self):
        s = Schedule(9, 17)
        d = Doctor("Doc", s)
        # Should delegate
        self.assertTrue(d.check_availability(10))
        self.assertFalse(d.check_availability(20))

    def test_surgeon_inheritance(self):
        s = Schedule(9, 17)
        sg = Surgeon("Surg", s, "General")
        # Inherits logic
        self.assertTrue(sg.check_availability(10))
        self.assertTrue(isinstance(sg, Doctor))
        # Has access to schedule
        self.assertEqual(sg.schedule.start_hour, 9)

if __name__ == '__main__':
    unittest.main()
