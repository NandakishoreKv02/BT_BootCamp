import unittest
from starter_code import *

class TestIntegratedSystem(unittest.TestCase):
    def test_task_1_and_5_dict(self):
        d = {}
        update_patient_status(d, "P1", "Crit")
        res = batch_status_check(d, ["P1"])
        self.assertEqual(res, ["Crit"])
        self.assertIsInstance(d, dict)

    def test_task_2_list(self):
        h = []
        record_vitals(h, "10:00", 80)
        record_vitals(h, "10:05", 85)
        self.assertEqual(len(h), 2)
        self.assertEqual(h[0][1], 80, "Order must be preserved")

    def test_task_3_set(self):
        s = set()
        register_visit(s, "P1")
        register_visit(s, "P1")
        self.assertEqual(len(s), 1, "Sets must handle uniqueness")

    def test_task_4_frozenset(self):
        ids = [1, 2]
        res = lock_config(ids)
        self.assertIsInstance(res, frozenset)
        with self.assertRaises(AttributeError):
            res.add(3) # Verify immutability

if __name__ == "__main__":
    unittest.main()
