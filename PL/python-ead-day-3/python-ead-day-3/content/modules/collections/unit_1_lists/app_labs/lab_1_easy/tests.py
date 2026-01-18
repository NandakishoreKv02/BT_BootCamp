import unittest

class TestListBasics(unittest.TestCase):
    def test_appointments(self):
        from starter_code import appointments
        self.assertEqual(len(appointments), 3)
        self.assertEqual(appointments, ["Alice", "Bob", "Charlie"])

if __name__ == "__main__":
    unittest.main()
