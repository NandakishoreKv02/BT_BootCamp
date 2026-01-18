import unittest
from starter_code import process_batch

class TestLab4(unittest.TestCase):
    def setUp(self):
        self.data = [{"id": 1, "val": 10}]

    def test_success(self):
        val, msg = process_batch(self.data, 0, "val")
        self.assertEqual(val, 10)
        self.assertEqual(msg, "Success")

    def test_lookup_error_index(self):
        val, msg = process_batch(self.data, 5, "val")
        self.assertIsNone(val)
        self.assertIn("Lookup Failed", msg)

    def test_lookup_error_key(self):
        val, msg = process_batch(self.data, 0, "bad_key")
        self.assertIsNone(val)
        self.assertIn("Lookup Failed", msg)

if __name__ == "__main__":
    unittest.main()
