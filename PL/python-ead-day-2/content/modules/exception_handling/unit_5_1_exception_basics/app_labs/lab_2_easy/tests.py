import unittest
from starter_code import get_record_field

class TestLab2(unittest.TestCase):
    def setUp(self):
        self.db = {
            "101": {"name": "Alice", "diagnosis": "Flu"},
            "102": {"name": "Bob"}
        }

    def test_success(self):
        self.assertEqual(get_record_field(self.db, "101", "name"), "Alice")

    def test_missing_id(self):
        self.assertEqual(get_record_field(self.db, "999", "name"), "Data Not Found")

    def test_missing_field(self):
        self.assertEqual(get_record_field(self.db, "102", "diagnosis"), "Data Not Found")

if __name__ == "__main__":
    unittest.main()
