import unittest
from starter_code import execute_transaction, MockDB

class TestLab1(unittest.TestCase):
    def test_cleanup_on_success(self):
        db = MockDB()
        execute_transaction(db, lambda: None)
        self.assertFalse(db.is_locked)

    def test_cleanup_on_failure(self):
        db = MockDB()
        def fail(): raise ValueError()
        try:
            execute_transaction(db, fail)
        except ValueError:
            pass
        self.assertFalse(db.is_locked, "DB remained locked after crash")

if __name__ == "__main__":
    unittest.main()
