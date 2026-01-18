import unittest
from starter_code import fetch_data

class TestLab4(unittest.TestCase):
    def test_primary_works(self):
        self.assertEqual(fetch_data(lambda: "A", lambda: "B"), "A")

    def test_backup_works(self):
        def fail(): raise ValueError()
        self.assertEqual(fetch_data(fail, lambda: "B"), "B")

    def test_all_fail(self):
        def fail(): raise ValueError()
        with self.assertRaises(RuntimeError) as cm:
            fetch_data(fail, fail)
        self.assertEqual(str(cm.exception), "All sources failed")

if __name__ == "__main__":
    unittest.main()
