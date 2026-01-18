import unittest
import starter_code

class TestClinicalLogger(unittest.TestCase):
    def test_logger_creation(self):
        l = starter_code.make_logger("ICU")
        self.assertEqual(l['service'], "ICU")
        self.assertEqual(len(l['log_history']), 0)

    def test_log_event(self):
        l = starter_code.make_logger("Lab")
        starter_code.log_event(l, "Test Started")
        self.assertEqual(len(l['log_history']), 1)
        self.assertIn("Test Started", l['log_history'][0])

    def test_independence(self):
        l1 = starter_code.make_logger("A")
        l2 = starter_code.make_logger("B")
        starter_code.log_event(l1, "Event A")
        self.assertEqual(len(l1['log_history']), 1)
        self.assertEqual(len(l2['log_history']), 0)

if __name__ == "__main__":
    unittest.main()
