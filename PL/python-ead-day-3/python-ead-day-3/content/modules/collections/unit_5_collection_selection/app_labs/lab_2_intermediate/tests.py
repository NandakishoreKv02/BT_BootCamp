import unittest
from starter_code import *

class TestLogProcessing(unittest.TestCase):
    def test_task_1_deduplication(self):
        logs = [(1, "A", "L"), (1, "B", "U")]
        res = get_latest_activities(logs)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[1][1], "B", "Should preserve the LAST entry in the list")

    def test_task_2_sorting(self):
        mapping = {
            2: (2, "X"),
            1: (1, "Y")
        }
        res = format_sorted_report(mapping)
        self.assertEqual(res[0][0], 1, "List should be sorted by ID")
        self.assertEqual(res[1][0], 2)

if __name__ == "__main__":
    unittest.main()
