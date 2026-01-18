import unittest
from starter_code import sync_system, HealthNetworkError, DataStackError, DatabaseLockError

class TestLab6(unittest.TestCase):
    def test_data_failure(self):
        self.assertEqual(sync_system("database"), "Data Layer Failure")

    def test_network_failure(self):
        self.assertEqual(sync_system("network"), "Network Layer Failure")

    def test_hierarchy(self):
        # Full depth check
        self.assertTrue(issubclass(DatabaseLockError, DataStackError))
        self.assertTrue(issubclass(DataStackError, HealthNetworkError))

if __name__ == "__main__":
    unittest.main()
