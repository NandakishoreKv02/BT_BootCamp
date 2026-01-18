import unittest
from starter_code import calculate_with_logging

class TestLab2(unittest.TestCase):
    def test_log_and_reraise(self):
        logs = []
        with self.assertRaises(ZeroDivisionError):
            calculate_with_logging(10, 0, logs)
        
        self.assertIn("Zero Division Detected", logs)

    def test_success(self):
        logs = []
        res = calculate_with_logging(10, 2, logs)
        self.assertEqual(res, 5.0)
        self.assertEqual(len(logs), 0)

if __name__ == "__main__":
    unittest.main()
