import unittest
import starter_code

class TestMonitor(unittest.TestCase):
    def test_transitions(self):
        m = starter_code.make_monitor("Test")
        # Steps of +25
        # 70 -> 95 (Normal)
        starter_code.update_status(m)
        self.assertEqual(m['status'], "Normal")

        # 95 -> 120 (Warning)
        starter_code.update_status(m)
        self.assertEqual(m['status'], "Warning")

        # 120 -> 145 (Critical)
        starter_code.update_status(m)
        self.assertEqual(m['status'], "Critical")

if __name__ == "__main__":
    unittest.main()
