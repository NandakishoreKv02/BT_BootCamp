import unittest
from starter_code import *

class TestSetRegistry(unittest.TestCase):
    def test_task_1_initialize(self):
        ids = [101, 102, 101, 103]
        res = initialize_registry(ids)
        self.assertIsInstance(res, set)
        self.assertEqual(res, {101, 102, 103})

    def test_task_2_check_in(self):
        reg = {1, 2}
        check_in_patient(reg, 3)
        self.assertIn(3, reg)
        check_in_patient(reg, 1) # Duplicate
        self.assertEqual(len(reg), 3)

    def test_task_3_remove_safe(self):
        reg = {10, 20}
        remove_record(reg, 10)
        self.assertNotIn(10, reg)
        # Should not raise error
        remove_record(reg, 99)
        self.assertEqual(len(reg), 1)

    def test_task_4_count(self):
        reg = {1, 2, 3, 4, 5}
        self.assertEqual(get_unique_count(reg), 5)
        self.assertEqual(get_unique_count(set()), 0)

if __name__ == "__main__":
    unittest.main()
