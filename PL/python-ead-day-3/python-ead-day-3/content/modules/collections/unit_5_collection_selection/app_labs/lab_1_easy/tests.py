import unittest
from starter_code import *

class TestPerformanceOptimization(unittest.TestCase):
    def test_task_1_conversion(self):
        data = ["A", "B", "C"]
        res = optimize_registry(data)
        self.assertIsInstance(res, set, "Registry should be converted to a SET for O(1) lookup")
        self.assertEqual(res, {"A", "B", "C"})

    def test_task_2_lookup(self):
        reg = {"X", "Y", "Z"}
        self.assertTrue(is_id_inactive(reg, "X"))
        self.assertFalse(is_id_inactive(reg, "MISSING"))

if __name__ == "__main__":
    unittest.main()
