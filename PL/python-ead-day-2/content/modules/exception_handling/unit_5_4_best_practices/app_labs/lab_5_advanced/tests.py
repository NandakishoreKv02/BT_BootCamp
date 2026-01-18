import unittest
from starter_code import secure_scheduler

class TestLab5(unittest.TestCase):
    def test_rejected_data(self):
        data = {"dose": -1, "drug": "", "freq": 1}
        res = secure_scheduler(data)
        self.assertEqual(res["status"], "rejected")
        self.assertTrue(len(res["errors"]) >= 2)

    def test_rejected_zero_div(self):
        data = {"dose": 10, "drug": "A", "freq": 0}
        res = secure_scheduler(data)
        self.assertEqual(res["status"], "rejected")
        self.assertIn("Frequency cannot be zero", res["errors"])

    def test_success(self):
        data = {"dose": 10, "drug": "A", "freq": 2}
        res = secure_scheduler(data)
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["data"], 5.0)

if __name__ == "__main__":
    unittest.main()
