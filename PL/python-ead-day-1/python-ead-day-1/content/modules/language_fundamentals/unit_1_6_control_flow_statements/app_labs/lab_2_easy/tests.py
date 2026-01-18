import unittest
import importlib.util
import sys

try:
    import starter_code
except ImportError:
    pass

class TestReminders(unittest.TestCase):
    def setUp(self):
        if 'starter_code' in sys.modules:
            importlib.reload(starter_code)

    def test_multi_reminders(self):
        names = ["Alice", "Bob"]
        time = "10:00 AM"
        expected = [
            "Reminder: Alice, your appointment is at 10:00 AM.",
            "Reminder: Bob, your appointment is at 10:00 AM."
        ]
        self.assertEqual(starter_code.generate_reminders(names, time), expected)

    def test_empty_list(self):
        self.assertEqual(starter_code.generate_reminders([], "10:00 AM"), [])

if __name__ == '__main__':
    unittest.main()
