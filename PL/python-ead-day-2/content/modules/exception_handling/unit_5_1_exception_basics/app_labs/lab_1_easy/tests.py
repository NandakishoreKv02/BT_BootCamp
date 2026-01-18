import unittest
from starter_code import process_intake

class TestLab1(unittest.TestCase):
    def test_valid_input(self):
        data, errors = process_intake({"age": "30", "weight": "70.5"})
        self.assertEqual(data["age"], 30)
        self.assertEqual(data["weight"], 70.5)
        self.assertEqual(len(errors), 0)

    def test_invalid_input(self):
        data, errors = process_intake({"age": "abc", "weight": "xyz"})
        self.assertIsNone(data)
        self.assertIn("Invalid Age", errors)
        self.assertIn("Invalid Weight", errors)

if __name__ == "__main__":
    unittest.main()
