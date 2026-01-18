import unittest
from starter_code import import_records, RecordImportError

class TestLab5(unittest.TestCase):
    def test_import_summary(self):
        ages = [10, -5, 20, 200]
        # Rows: 0 (ok), 1 (fail), 2 (ok), 3 (fail)
        count, errors = import_records(ages)
        self.assertEqual(count, 2)
        self.assertEqual(len(errors), 2)
        self.assertIn("Row 1: age - Age cannot be negative", errors[0])
        self.assertIn("Row 3: age - Age out of range", errors[1])

    def test_all_success(self):
        count, errors = import_records([1, 2, 3])
        self.assertEqual(count, 3)
        self.assertEqual(len(errors), 0)

if __name__ == "__main__":
    unittest.main()
