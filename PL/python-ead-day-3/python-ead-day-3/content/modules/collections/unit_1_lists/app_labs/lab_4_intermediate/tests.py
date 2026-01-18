import unittest

class TestSorting(unittest.TestCase):
    def test_sort(self):
        from starter_code import appointment_times, reverse_times
        self.assertEqual(appointment_times, ["08:15", "09:30", "11:00", "14:00"])
        self.assertEqual(reverse_times, ["14:00", "11:00", "09:30", "08:15"])

if __name__ == "__main__":
    unittest.main()
