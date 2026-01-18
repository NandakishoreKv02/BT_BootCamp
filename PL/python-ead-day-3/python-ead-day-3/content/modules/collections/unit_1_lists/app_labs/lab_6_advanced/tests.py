import unittest

class TestSlicing(unittest.TestCase):
    def test_slices(self):
        from starter_code import morning_shift, afternoon_shift, express_line, last_three
        self.assertEqual(len(morning_shift), 12)
        self.assertEqual(len(afternoon_shift), 12)
        self.assertEqual(morning_shift[0], "00:00")
        self.assertEqual(afternoon_shift[0], "12:00")
        self.assertEqual(len(express_line), 8) # 24/3
        self.assertEqual(last_three, ["21:00", "22:00", "23:00"])

if __name__ == "__main__":
    unittest.main()
