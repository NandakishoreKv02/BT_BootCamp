import unittest
from starter_code import parse_record

class TestLab5(unittest.TestCase):
    def test_success(self):
        res = parse_record("ID:101;AGE:45")
        self.assertEqual(res, {"id": 101, "age": 45})

    def test_invalid_format(self):
        # Missing ':' in first part
        self.assertEqual(parse_record("ID101;AGE:45"), "Invalid Format")

    def test_invalid_number(self):
        self.assertEqual(parse_record("ID:101;AGE:abc"), "Invalid Number")

if __name__ == "__main__":
    unittest.main()
