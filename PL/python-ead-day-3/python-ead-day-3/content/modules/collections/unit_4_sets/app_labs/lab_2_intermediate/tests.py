import unittest
from starter_code import *

class TestSetMath(unittest.TestCase):
    def setUp(self):
        self.er = {1, 2, 3}
        self.icu = {3, 4, 5}

    def test_task_1_shared(self):
        res = get_shared_patients(self.er, self.icu)
        self.assertEqual(res, {3})

    def test_task_2_all(self):
        res = get_all_unique_patients(self.er, self.icu)
        self.assertEqual(res, {1, 2, 3, 4, 5})

    def test_task_3_difference(self):
        res = get_er_only_patients(self.er, self.icu)
        self.assertEqual(res, {1, 2})

    def test_task_4_symmetric_diff(self):
        res = get_single_dept_visitors(self.er, self.icu)
        self.assertEqual(res, {1, 2, 4, 5})

if __name__ == "__main__":
    unittest.main()
