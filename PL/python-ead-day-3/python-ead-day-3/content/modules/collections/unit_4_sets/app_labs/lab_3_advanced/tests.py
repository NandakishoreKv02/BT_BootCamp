import unittest
from starter_code import *

class TestStaffingAudit(unittest.TestCase):
    def setUp(self):
        self.master = {101, 102, 103, 104, 105}

    def test_task_1_subset(self):
        valid_shift = {101, 103}
        invalid_shift = {101, 999}
        self.assertTrue(is_shift_compliant(valid_shift, self.master))
        self.assertFalse(is_shift_compliant(invalid_shift, self.master))

    def test_task_2_disjoint(self):
        morn = {101, 102}
        night = {104, 105}
        violation = {102, 103}
        self.assertTrue(no_double_shift_violations(morn, night))
        self.assertFalse(no_double_shift_violations(morn, violation))

    def test_task_3_frozenset(self):
        res = create_fixed_requirements(["CPR", "ACLS"])
        self.assertIsInstance(res, frozenset)
        self.assertEqual(res, frozenset({"CPR", "ACLS"}))

    def test_task_4_comprehension(self):
        data = [1000, 6000, 1000, 7000, 4000]
        res = get_senior_staff(data)
        self.assertEqual(res, {6000, 7000})
        self.assertIsInstance(res, set)

    def test_task_5_difference(self):
        ward = {101, 103, 777, 888}
        res = identify_unauthorized_ids(ward, self.master)
        self.assertEqual(res, {777, 888})

if __name__ == "__main__":
    unittest.main()
